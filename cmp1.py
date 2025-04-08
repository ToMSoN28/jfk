import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from llvmlite import ir


class SimpleLangIRVisitor(SimpleLangVisitor):
    def __init__(self):
        self.module = ir.Module(name="SimpleLang")
        self.symbol_table = {}
        self.symbol_print = {}
        self.function_counter = 0
        self.generated_funcs = []
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
        print(f"Creating global format string for: {fmt}")

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

    def visitVariable_declaration(self, ctx):
        var_name = ctx.ID().getText()

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
        else:
            raise ValueError(f"Unsupported type for variable: {var_name}")

        global_var = ir.GlobalVariable(self.module, llvm_type, var_name)
        global_var.initializer = initializer
        global_var.linkage = 'internal'
        global_var.global_constant = False
        self.symbol_table[var_name] = global_var

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        if var_name not in self.symbol_table:
            raise ValueError(f"Variable '{var_name}' is not declared")

        global_var = self.symbol_table[var_name]

        func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_ass_func_{self.function_counter}")
        self.function_counter += 1
        self.generated_funcs.append(func.name)
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        value = None
        if ctx.expression():
            value = self.visitExpression(ctx.expression(), builder)
        elif ctx.boolean_expression():
            value = self.visitBooleanExpression(ctx.boolean_expression(), builder)

        if value is not None:
            builder.store(value, global_var)

        builder.ret_void()

    def visitPrint_statement(self, ctx):
        expr_text = ctx.expression().getText()

        func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_print_func_{self.function_counter}")
        self.function_counter += 1
        self.generated_funcs.append(func.name)
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        if expr_text in self.symbol_table:
            global_var = self.symbol_table[expr_text]
            value = builder.load(global_var)

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
        else:
            fallback = ir.Constant(ir.IntType(32), 999)
            fmt = "%d\n"
            fmt_var = self._create_global_format_str(fmt)
            fmt_ptr = builder.bitcast(fmt_var, ir.IntType(8).as_pointer())
            builder.call(self.printf, [fmt_ptr, fallback])

        builder.ret_void()

    def visitExpression(self, ctx, builder):
        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if text.isdigit():
                return ir.Constant(ir.IntType(32), int(text))
            elif '.' in text:
                return ir.Constant(ir.DoubleType(), float(text))
            elif text in self.symbol_table:
                global_var = self.symbol_table[text]
                return builder.load(global_var)
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
                print(f"Left: {left}, Op: {op}, Right: {right} -> {ctx.getText()}")
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

    def visitProgram(self, ctx):
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

    print("Parse Tree:")
    print(tree.toStringTree(recog=parser))

    visitor = SimpleLangIRVisitor()
    llvm_module = visitor.visitProgram(tree)
    return llvm_module


if __name__ == '__main__':
    input_text = """
    float a = 1.0;
    a = input();
    print(a);
    """
    llvm_module = compile(input_text)

    with open("output.ll", "w") as f:
        f.write(str(llvm_module))

    print("LLVM IR has been written to output.ll")
