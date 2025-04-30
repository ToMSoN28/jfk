import sys, os
from zipfile import stringFileHeader

from antlr4 import *
import sys
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from llvmlite import ir

from test import SimpleLangChecker


class SimpleLangIRVisitor(SimpleLangVisitor):
    def __init__(self):
        self.module = ir.Module(name="SimpleLang")
        self.symbol_table = {}
        self.symbol_print = {}
        self.function_counter = 0
        self.generated_funcs = []
        self.local_symbol_table = {}  # dict: nazwa_funkcji -> {nazwa_zmiennej: ptr}
        self.current_function = None  # aktualnie odwiedzana funkcja

        self.printf = None
        self._declare_printf()
        self._declare_scanf()

    def _declare_printf(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    def _declare_scanf(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        input_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.input = ir.Function(self.module, input_ty, name="scanf")

    def visitInput_statement(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            raise ValueError(f"Variable '{var_name}' is not declared")

        global_var = self.symbol_table[var_name]

        # Create a dummy function to hold the input operation
        func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []),
                           name=f"dummy_input_func_{self.function_counter}")
        self.function_counter += 1
        self.generated_funcs.append(func.name)
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        value = builder.load(global_var)
        # Handle user input based on variable type
        if isinstance(value.type, ir.IntType):
            fmt = "%d"  # Input format for integer
        elif isinstance(value.type, ir.DoubleType):
            fmt = "%lf"  # Input format for float
        else:
            raise ValueError(f"Unsupported type for input: {global_var.type}")

        # Create the format string for input
        fmt_var = self._create_global_format_str(fmt)
        fmt_ptr = builder.bitcast(fmt_var, ir.IntType(8).as_pointer())

        # Call the external input function to read input
        builder.call(self.input, [fmt_ptr, global_var])
        builder.ret_void()

    def _create_global_format_str(self, fmt):
        if fmt in self.symbol_print:
            return self.symbol_print[fmt]

        # Debug: wypisz format, jeśli jeszcze nie istnieje
        # print(f"Creating global format string for: {fmt}")

        # Zakoduj jako UTF-8 + null terminator
        fmt_bytes = bytearray(fmt.encode("utf8")) + b"\00"
        const_array = ir.ArrayType(ir.IntType(8), len(fmt_bytes))

        # Zadbaj o bezpieczną nazwę
        safe_name = fmt.replace("%", "").replace(" ", "_").replace(".", "_").replace('\n','')
        name = f".fmt_{safe_name}"

        global_fmt = ir.GlobalVariable(self.module, const_array, name=name)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = ir.Constant(const_array, fmt_bytes)

        # Zapisz w słowniku, żeby nie duplikować
        self.symbol_print[fmt] = global_fmt

        return global_fmt

    def visitVariable_declaration(self, ctx, builder=None):
        var_name = ctx.ID().getText()
        if var_name == "<missing ID>":
            raise AttributeError("No variable name")

        if ctx.NUMBER():
            llvm_type = ir.IntType(32)
            initializer = ir.Constant(llvm_type, int(ctx.NUMBER().getText()))
        elif ctx.FLOAT():
            llvm_type = ir.DoubleType()
            initializer = ir.Constant(llvm_type, float(ctx.FLOAT().getText()))
        elif ctx.boolean_expression():
            llvm_type = ir.IntType(1)
            initializer = self.visitBooleanExpression(ctx.boolean_expression(), None)
            if not isinstance(initializer, ir.Constant):
                initializer = ir.Constant(llvm_type, 0)
        elif ctx.STRING():  # 🔧 ZMIANA
            text = ctx.STRING().getText()[1:-1] + '\0'
            str_bytes = bytearray(text.encode("utf8"))
            str_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
            global_str = ir.GlobalVariable(self.module, str_type, name=f".str.{var_name}.{self.function_counter}")
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = ir.Constant(str_type, str_bytes)

            llvm_type = ir.IntType(8).as_pointer()
            initializer = global_str.bitcast(llvm_type)
        else:
            raise ValueError(f"Unsupported type for variable: {var_name}")

        if not builder:
            global_var = ir.GlobalVariable(self.module, llvm_type, name=var_name)
            global_var.initializer = initializer
            global_var.linkage = 'internal'
            global_var.global_constant = False
            self.symbol_table[var_name] = global_var
        else:
            ptr = builder.alloca(llvm_type, name=var_name)
            builder.store(initializer, ptr)
            self.local_symbol_table[self.current_function][var_name] = ptr

        

    def visitAssignment(self, ctx, builder=None):
        var_name = ctx.ID().getText()
        if self.current_function:
            if var_name not in self.local_symbol_table.get(self.current_function, {}):
                raise ValueError(f"Variable '{var_name}' is not declared in function {self.current_function}")
            var_ptr = self.local_symbol_table[self.current_function][var_name]
        else:
            if var_name not in self.symbol_table:
                raise ValueError(f"Variable '{var_name}' is not declared")
            var_ptr = self.symbol_table[var_name]

        end_fun = False
        if not builder:
            end_fun = True
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_ass_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)

        if ctx.STRING():  # 🔧 ZMIANA
            text = ctx.STRING().getText()[1:-1] + '\0'
            str_bytes = bytearray(text.encode("utf8"))
            str_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
            global_str = ir.GlobalVariable(self.module, str_type, name=f".str.{var_name}.{self.function_counter}")
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = ir.Constant(str_type, str_bytes)
            value = builder.bitcast(global_str, ir.IntType(8).as_pointer())
        elif ctx.expression():
            value = self.visitExpression(ctx.expression(), builder)
        elif ctx.boolean_expression():
            value = self.visitBooleanExpression(ctx.boolean_expression(), builder)
        else:
            raise ValueError("Invalid assignment")

        builder.store(value, var_ptr)

        if end_fun:
            builder.ret_void()


    def visitPrint_statement(self, ctx, builder=None):
        end_fun = False
        if not builder:
            end_fun = True
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_print_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)

        value = None
        fmt = None

        if ctx.STRING():  # 🔧 ZMIANA
            text = ctx.STRING().getText()[1:-1] + '\0'
            str_bytes = bytearray(text.encode("utf8"))
            str_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
            global_str = ir.GlobalVariable(self.module, str_type, name=f".str.print.{self.function_counter}")
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = ir.Constant(str_type, str_bytes)
            value = builder.bitcast(global_str, ir.IntType(8).as_pointer())
            fmt = "%s\n"

        elif ctx.ID():  # 🔧 ZMIANA
            var_name = ctx.ID().getText()
            print(self.current_function)
            if self.current_function:
                var_ptr = self.local_symbol_table[self.current_function].get(var_name)
                print(f"Local variable '{var_name}' found in function '{self.current_function}'")
            else:
                var_ptr = self.symbol_table.get(var_name)
            if var_ptr is None:
                raise ValueError(f"Variable '{var_name}' is not declared")

            pointee_type = var_ptr.type.pointee
            is_string = (
                isinstance(pointee_type, ir.PointerType) and isinstance(pointee_type.pointee, ir.IntType) and pointee_type.pointee.width == 8
            )
            print(f"Variable '{var_name}' is_string: {is_string}")
            if is_string:
                value = builder.load(var_ptr)
                fmt = "%s\n"

        elif ctx.boolean_expression():
            value = self.visitBooleanExpression(ctx.boolean_expression(), builder)
            fmt = "%d\n"
            value = builder.zext(value, ir.IntType(32))

        if ctx.expression() or fmt is None:
            if ctx.expression():
                value = self.visitExpression(ctx.expression(), builder)
            else:
                value = self.visitExpression(ctx.ID(), builder)
            print(value)
            if isinstance(value.type, ir.IntType) and value.type.width == 32:
                fmt = "%d\n"
            elif isinstance(value.type, ir.DoubleType):
                fmt = "%f\n"
            elif isinstance(value.type, ir.IntType) and value.type.width == 1:
                fmt = "%d\n"
                value = builder.zext(value, ir.IntType(32))
            else:
                raise ValueError(f"Unsupported type for print: {value.type}")

        fmt_var = self._create_global_format_str(fmt)
        fmt_ptr = builder.bitcast(fmt_var, ir.IntType(8).as_pointer())
        builder.call(self.printf, [fmt_ptr, value])

        if end_fun:
            builder.ret_void()


    def visitExpression(self, ctx, builder):
        print(ctx.getText())
        if ctx.getChildCount() == 1 or ctx.getChildCount() == 0:
            text = ctx.getText()
            if text.isdigit():
                return ir.Constant(ir.IntType(32), int(text))
            elif '.' in text:
                return ir.Constant(ir.DoubleType(), float(text))
            elif self.current_function and text in self.local_symbol_table.get(self.current_function, {}):
                ptr = self.local_symbol_table[self.current_function][text]
                return builder.load(ptr)
            elif text in self.symbol_table:
                global_var = self.symbol_table[text]
                return builder.load(global_var)
            elif ctx.func_call():
                name = ctx.func_call().ID().getText()
                args = []
                call = ctx.func_call()
                if call.argument_list():
                    for expr in call.argument_list().expression():
                        args.append(self.visitExpression(expr, builder))
                    for bexpr in call.argument_list().boolean_expression():
                        args.append(self.visitBooleanExpression(bexpr, builder))
                func = self.module.get_global(name)
                return builder.call(func, args)
            else:
                raise ValueError(f"Unknown identifier: {text}")

        elif ctx.getChildCount() == 3:
            left = self.visitExpression(ctx.expression(0), builder)
            right = self.visitExpression(ctx.expression(1), builder)
            op = ctx.getChild(1).getText()

            if left.type != right.type:
                raise ValueError(f"Type mismatch in expression: {left.type} vs {right.type}")

            is_int = isinstance(left.type, ir.IntType)
            is_float = isinstance(left.type, ir.DoubleType)

            if op == '+':
                return builder.add(left, right) if is_int else builder.fadd(left, right)
            elif op == '-':
                return builder.sub(left, right) if is_int else builder.fsub(left, right)
            elif op == '*':
                return builder.mul(left, right) if is_int else builder.fmul(left, right)
            elif op == '/':
                return builder.sdiv(left, right) if is_int else builder.fdiv(left, right)
            else:
                raise ValueError(f"Unsupported binary operator: {op}")

    def visitBooleanExpression(self, ctx, builder):
        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if text == "true":
                return ir.Constant(ir.IntType(1), 1)
            elif text == "false":
                return ir.Constant(ir.IntType(1), 0)
            elif self.current_function and text in self.local_symbol_table.get(self.current_function, {}):
                ptr = self.local_symbol_table[self.current_function][text]
                return builder.load(ptr)
            elif text in self.symbol_table:
                global_var = self.symbol_table[text]
                if builder:
                    return builder.load(global_var)
                else:
                    # Try to extract the constant initializer
                    if hasattr(global_var, "initializer") and isinstance(global_var.initializer, ir.Constant):
                        return global_var.initializer
                    else:
                        return ir.Constant(ir.IntType(1), 0)  # Fallback if no initializer
            elif ctx.getChild(0) == ctx.comparizon_expression():
                return self.visitComparizon_expression(ctx.comparizon_expression(), builder)
            elif ctx.func_call():
                name = ctx.func_call().ID().getText()
                args = []
                call = ctx.func_call()
                if call.argument_list():
                    for expr in call.argument_list().expression():
                        args.append(self.visitExpression(expr, builder))
                    for bexpr in call.argument_list().boolean_expression():
                        args.append(self.visitBooleanExpression(bexpr, builder))

                func = self.module.get_global(name)
                if not builder:
                    raise ValueError("Builder is required for function calls")
                return builder.call(func, args)
            else:
                raise ValueError(f"Unknown boolean value: {text}")

        elif ctx.getChildCount() == 2:
            if ctx.getChild(0).getText() == "NEG":
                operand = self.visitBooleanExpression(ctx.getChild(1), builder)
                if builder:
                    return builder.xor(operand, ir.Constant(ir.IntType(1), 1))
                else:
                    if isinstance(operand, ir.Constant):
                        return ir.Constant(ir.IntType(1), 1 - operand.constant)
                    return ir.Constant(ir.IntType(1), 0)  # Fallback

        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(" and ctx.getChild(2).getText() == ")":
                return self.visitBooleanExpression(ctx.getChild(1), builder)
            else:
                left = self.visitBooleanExpression(ctx.getChild(0), builder)
                op = ctx.getChild(1).getText()
                if isinstance(left, ir.Constant):
                    if left.constant == 0 and op == 'AND':
                        return ir.Constant(ir.IntType(1), 0)
                    if left.constant == 1 and op == 'OR':
                        return ir.Constant(ir.IntType(1), 1)
                right = self.visitBooleanExpression(ctx.getChild(2), builder)
                # print(f"Left: {left}, Op: {op}, Right: {right} -> {ctx.getText()}")
                if isinstance(left, ir.Constant):
                    print(f"Left value (constant): {left.constant}")
                else:
                    print(f"Left value (non-constant): {left}")

                if builder:
                    if op == "OR":
                        result = builder.alloca(ir.IntType(1), name="or_result")
                        then_block = builder.append_basic_block(name="or_true")
                        else_block = builder.append_basic_block(name="or_rhs")
                        merge_block = builder.append_basic_block(name="or_merge")

                        builder.cbranch(left, then_block, else_block)

                        # then block (left is true)
                        builder.position_at_start(then_block)
                        builder.store(ir.Constant(ir.IntType(1), 1), result)
                        builder.branch(merge_block)

                        # else block (evaluate right)
                        builder.position_at_start(else_block)
                        right_val = self.visitBooleanExpression(ctx.getChild(2), builder)
                        builder.store(right_val, result)
                        builder.branch(merge_block)

                        # merge block
                        builder.position_at_start(merge_block)
                        return builder.load(result)

                    elif op == "AND":
                        result = builder.alloca(ir.IntType(1), name="and_result")
                        then_block = builder.append_basic_block(name="and_rhs")
                        else_block = builder.append_basic_block(name="and_false")
                        merge_block = builder.append_basic_block(name="and_merge")

                        builder.cbranch(left, then_block, else_block)

                        # then block (left is true, need to evaluate right)
                        builder.position_at_start(then_block)
                        right_val = self.visitBooleanExpression(ctx.getChild(2), builder)
                        builder.store(right_val, result)
                        builder.branch(merge_block)

                        # else block (left is false => whole AND is false)
                        builder.position_at_start(else_block)
                        builder.store(ir.Constant(ir.IntType(1), 0), result)
                        builder.branch(merge_block)

                        # merge block
                        builder.position_at_start(merge_block)
                        return builder.load(result)
                    elif op == "XOR":
                        return builder.xor(left, right)
                else:
                    # Evaluate statically if both sides are constants
                    if isinstance(left, ir.Constant) and isinstance(right, ir.Constant):
                        a, b = bool(left.constant), bool(right.constant)
                        if op == "AND":
                            return ir.Constant(ir.IntType(1), int(a and b))
                        elif op == "OR":
                            return ir.Constant(ir.IntType(1), int(a or b))
                        elif op == "XOR":
                            return ir.Constant(ir.IntType(1), int(a ^ b))

                return ir.Constant(ir.IntType(1), 0)  # Fallback

        raise ValueError("Invalid boolean expression")
    
    def visitComparizon_expression(self, ctx, builder):
        left = self.visitExpression(ctx.getChild(0), builder)
        right = self.visitExpression(ctx.getChild(2), builder)
        op = ctx.getChild(1).getText()

        if left.type != right.type:
            raise ValueError(f"Type mismatch in comparison: {left.type} vs {right.type}")

        if builder:
            if left.type == ir.IntType(32):
                if op == "<":
                    return builder.icmp_signed("<", left, right)
                elif op == "<=":
                    return builder.icmp_signed("<=", left, right)
                elif op == ">":
                    return builder.icmp_signed(">", left, right)
                elif op == ">=":
                    return builder.icmp_signed(">=", left, right)
                elif op == "==":
                    return builder.icmp_signed("==", left, right)
                elif op == "!=":
                    return builder.icmp_signed("!=", left, right)
            elif left.type == ir.DoubleType():
                if op == "<":
                    return builder.fcmp_ordered("<", left, right)
                elif op == "<=":
                    return builder.fcmp_ordered("<=", left, right)
                elif op == ">":
                    return builder.fcmp_ordered(">", left, right)
                elif op == ">=":
                    return builder.fcmp_ordered(">=", left, right)
                elif op == "==":
                    return builder.fcmp_ordered("==", left, right)
                elif op == "!=":
                    return builder.fcmp_ordered("!=", left, right)
            else:
                raise TypeError(f"Unsupported type for comparison: {left.type}")
        else:
        # Tryb interpretacyjny (np. bez buildera)
            if op == '==':
                result = left.value == right.value
            elif op == '!=':
                result = left.value != right.value
            elif op == '<=':
                result = left.value <= right.value
            elif op == '>=':
                result = left.value >= right.value
            elif op == '<':
                result = left.value < right.value
            elif op == '>':
                result = left.value > right.value
            else:
                raise NotImplementedError(f"Unsupported operator: {op}")

            return ir.Constant(ir.IntType(1), int(result))
            
    def visitIf_statement(self, ctx, builder=None):
        end_fun = False
        if not builder:
            end_fun = True        
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_if_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
        
        has_else_block = 'else' in ctx.getText() 
        
        # Stwórz nowy blok dla "if"
        if_block = builder.append_basic_block('if')
        # Stwórz nowy blok dla "else"
        else_block = builder.append_basic_block('else')
        # Stwórz nowy blok dla kontynuacji po "if"
        merge_block = builder.append_basic_block('merge')

        # Warunkowe przejście
        builder.cbranch(self.visitBooleanExpression(ctx.getChild(1), builder), if_block, else_block)

        # Wykonaj kod dla "if"
        builder.position_at_end(if_block)
        self.visitCode_block(ctx.getChild(2), builder)  # Jeśli warunek spełniony
        if not builder.block.is_terminated:
            builder.branch(merge_block)
        # builder.branch(merge_block)  # Przejdź do "merge_block" po wykonaniu kodu w if

        # Wykonaj kod dla "else"
        builder.position_at_end(else_block)
        if ctx.getChildCount() > 3:
            self.visitCode_block(ctx.getChild(4), builder)   # Jeśli warunek niespełniony
        if not builder.block.is_terminated:
            builder.branch(merge_block)
        # builder.branch(merge_block)  # Po wykonaniu kodu w else, przejdź do "merge_block"

        # Po zakończeniu obu gałęzi, kontynuacja
        builder.position_at_end(merge_block)
        if end_fun:
            builder.ret_void()

    def visitLoop_while(self, ctx, builder=None):
        end_fun = False
        if not builder:
            end_fun = True        
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_while_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            
        loop_cond_block = builder.append_basic_block('loop_condition')  # Blok warunku
        loop_body_block = builder.append_basic_block('loop_body')  # Blok ciała pętli
        loop_end_block = builder.append_basic_block('loop_end')  # Blok końca pętli
        
        builder.branch(loop_cond_block)
        
        # Warunek pętli
        builder.position_at_end(loop_cond_block)
        condition = self.visitBooleanExpression(ctx.getChild(1), builder)
        builder.cbranch(condition, loop_body_block, loop_end_block)  # Jeśli warunek prawdziwy, przechodzimy do ciała pętli, w przeciwnym razie kończymy pętlę

        builder.position_at_end(loop_body_block)
        self.visitCode_block(ctx.getChild(2), builder)  # Wykonaj instrukcje w ciele pętli
        
        # Po wykonaniu ciała pętli, skaczemy z powrotem do bloku warunkowego
        if not builder.block.is_terminated:
            builder.branch(loop_cond_block)
        # builder.branch(loop_cond_block)
        
        builder.position_at_end(loop_end_block)
        if end_fun:
            builder.ret_void()
        
    def visitFunction_definition(self, ctx):
        return_type_str = ctx.getChild(1).getText()
        func_name = ctx.ID().getText()
        param_nodes = ctx.parametr_list().children if ctx.parametr_list() else []
        self.current_function = func_name
        self.local_symbol_table[func_name] = {} 

        # Pobierz typy i nazwy parametrów
        params = []
        llvm_types = []
        i = 0
        while i < len(param_nodes):
            if param_nodes[i].getText() in ['int', 'float', 'bool']:
                typ = param_nodes[i].getText()
                name = param_nodes[i + 1].getText()
                if typ == 'int':
                    llvm_type = ir.IntType(32)
                elif typ == 'float':
                    llvm_type = ir.DoubleType()
                elif typ == 'bool':
                    llvm_type = ir.IntType(1)
                else:
                    raise ValueError(f"Unknown param type: {typ}")
                llvm_types.append(llvm_type)
                params.append((name, llvm_type))
                i += 2
            else:
                i += 1

        # Typ zwracany
        if return_type_str == 'int':
            return_type = ir.IntType(32)
        elif return_type_str == 'float':
            return_type = ir.DoubleType()
        elif return_type_str == 'bool':
            return_type = ir.IntType(1)
        else:
            raise ValueError(f"Unknown return type: {return_type_str}")

        # Stwórz funkcję
        func_type = ir.FunctionType(return_type, llvm_types)
        func = ir.Function(self.module, func_type, name=func_name)
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        # Zainicjalizuj parametry w symbol_table
        for i, (name, typ) in enumerate(params):
            ptr = builder.alloca(typ, name=name)
            builder.store(func.args[i], ptr)
            self.symbol_table[name] = ptr

        # Zbuduj ciało funkcji
        ret_val = self.visitCode_block(ctx.code_block(), builder)

        # Jeśli nie ma jawnego return, domyślnie zwróć 0/0.0/false
        if not builder.block.is_terminated:
            if return_type == ir.IntType(32):
                builder.ret(ir.Constant(ir.IntType(32), 0))
            elif return_type == ir.DoubleType():
                builder.ret(ir.Constant(ir.DoubleType(), 0.0))
            elif return_type == ir.IntType(1):
                builder.ret(ir.Constant(ir.IntType(1), 0))

        self.current_function = None  # Resetuj aktualną funkcję
        return func
    
    def visitReturn_statement(self, ctx, builder):
        if ctx.expression():
            retval = self.visitExpression(ctx.expression(), builder)
            builder.ret(retval)
        elif ctx.boolean_expression():
            retval = self.visitBooleanExpression(ctx.boolean_expression(), builder)
            builder.ret(retval)
        else:
            builder.ret_void()
        
    def visitCode_block(self, ctx, builder):
        # print(ctx.getText())
        for i in range(1, ctx.getChildCount() - 1):
            statement = ctx.getChild(i)
            self.visitStatement_(statement, builder)
               
    def visitStatement_(self, ctx, builder):
        # print(ctx.getText())
        if ctx.variable_declaration():
            self.visitVariable_declaration(ctx.variable_declaration(), builder)
        elif ctx.assignment():
            self.visitAssignment(ctx.assignment(), builder)
        elif ctx.if_statement():
            self.visitIf_statement(ctx.if_statement(), builder)
        elif ctx.print_statement():
            self.visitPrint_statement(ctx.print_statement(), builder)
        elif ctx.loop_while():
            self.visitLoop_while(ctx.loop_while(), builder)
        elif ctx.return_statement():
            self.visitReturn_statement(ctx.return_statement(), builder)
        else:
            raise ValueError(f"Unknown statement: {ctx.getText()}")
        

    def visitProgram(self, ctx):
        for func_def in ctx.function_definition():
            self.visitFunction_definition(func_def)
        
        for statement in ctx.statement():
            self.visit(statement)

        main_ty = ir.FunctionType(ir.IntType(32), [])
        main_fn = ir.Function(self.module, main_ty, name="main")
        block = main_fn.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        for func_name in self.generated_funcs:
            func = self.module.get_global(func_name)
            builder.call(func, [])

        builder.ret(ir.Constant(ir.IntType(32), 0))
        self.module.triple = "aarch64-apple-darwin"
        #self.module.triple = "x86_64-pc-windows-msvc"
        self.module.data_layout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"
        print("Generated LLVM IR:")
        print(self.module)
        return self.module


def compile(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)

    tree = parser.program()
    print(tree.toStringTree(recog=parser))

    visitor = SimpleLangIRVisitor()
    llvm_module = visitor.visitProgram(tree)
    return llvm_module



DEFAULT_SOURCE = """
float a = 1.0;
float b = 2.0;
float c = 3.14;
print(c);
c = a + b;
print(c);
int x = 1;
print(x);
bool aa = true OR (false AND true);
print(aa);
bool bb = false;
print(bb);
bool dd = true;
bool cc = true
cc = false OR (bb AND dd);
print(cc);
cc = dd OR (bb AND dd);
print(cc);
"""

if __name__ == '__main__':
    filepath = ''
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'code.txt'
    if os.path.exists(filepath):
        with open("code.txt", "r") as f:
            input_text = f.read()
    else:
        print(f'[INFO] Plik {filepath} nie znaleziony — używam domyślnego kodu.')
        input_text = DEFAULT_SOURCE

    checker = SimpleLangChecker(filepath)
    checker.check()
    llvm_module = compile(input_text)

    with open("output.ll", "w") as f:
        f.write(str(llvm_module))
    print("LLVM IR has been written to output.ll")
