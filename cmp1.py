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

    def visitTable_declaration(self, ctx, builder=None):
        element_type = ctx.getChild(0).getText()
        array_name = ctx.ID().getText()
        size = int(ctx.NUMBER().getText())

        if element_type == "int":
            llvm_type = ir.IntType(32)
        elif element_type == "float":
            llvm_type = ir.DoubleType()
        elif element_type == "bool":
            llvm_type = ir.IntType(1)
        else:
            raise ValueError(f"Unsupported array type: {element_type}")

        array_type = ir.ArrayType(llvm_type, size)

        if builder:
            ptr = builder.alloca(array_type, name=array_name)
            self.local_symbol_table[self.current_function][array_name] = ptr
        else:
            global_array = ir.GlobalVariable(self.module, array_type, name=array_name)
            global_array.linkage = 'internal'
            global_array.initializer = ir.Constant(array_type, None)
            self.symbol_table[array_name] = global_array   
            
    def visitTable_assignment(self, ctx, builder=None):
        print(ctx.getText())
        var_name = ctx.ID().getText()

        if self.current_function:
            table_ptr = self.local_symbol_table[self.current_function].get(var_name)
        else:
            table_ptr = self.symbol_table.get(var_name)

        if table_ptr is None:
            raise ValueError(f"Table '{var_name}' is not declared")
        
        end_fun = False
        if not builder:
            end_fun = True
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_ass_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            print(f'new block: {end_fun}')

        if ctx.getChild(1).getText() == '=':  # Cała tablica
            values = ctx.expression()
            n = len(values)

            array_type = table_ptr.type.pointee
            if isinstance(array_type, ir.ArrayType) and n != array_type.count:
                raise ValueError(f"Wrong number of elements for table {var_name}")

            for i, val_ctx in enumerate(values):
                value = self.visitExpression(val_ctx, builder)
                ptr = builder.gep(table_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
                builder.store(value, ptr)

        else:  # Pojedynczy element
            index = self.visitExpression(ctx.expression(0), builder)
            value = self.visitExpression(ctx.expression(1), builder)
            ptr = builder.gep(table_ptr, [ir.Constant(ir.IntType(32), 0), index])
            builder.store(value, ptr)
            
        if end_fun:
            builder.ret_void()

    def visitMatrix_declaration(self, ctx: SimpleLangParser.Matrix_declarationContext, builder=None):
        matrix_name = ctx.ID().getText()
        element_type_str = ctx.type_().getText()
        rows = int(ctx.NUMBER(0).getText())
        cols = int(ctx.NUMBER(1).getText())

        llvm_element_type = None
        if element_type_str == "int":
            llvm_element_type = ir.IntType(32)
        elif element_type_str == "float":
            llvm_element_type = ir.DoubleType()
        elif element_type_str == "bool":
            llvm_element_type = ir.IntType(1)
        elif element_type_str == "string":
            llvm_element_type = ir.IntType(8).as_pointer()
        else:
            raise ValueError(f"Unsupported type: {element_type_str}")

        if rows <= 0 or cols <= 0:
            raise ValueError(f"Matrix dimensions must be positive for '{matrix_name}'")

        #llvm_element_type = self._get_llvm_type(element_type_str)
        matrix_type = ir.ArrayType(ir.ArrayType(llvm_element_type, cols), rows)

        is_local = builder is not None and self.current_function is not None
        target_table = self.local_symbol_table.setdefault(self.current_function, {}) if is_local else self.symbol_table

        if matrix_name in target_table:
             raise ValueError(f"Variable '{matrix_name}' already declared in this scope")

        initializer_value = None
        local_init_values = []
        if ctx.matrix_initializer():
            init_ctx = ctx.matrix_initializer()
            row_inits = init_ctx.row_initializer()
            if len(row_inits) != rows:
                raise ValueError(f"Initializer for matrix '{matrix_name}' has {len(row_inits)} rows, expected {rows}")

            matrix_rows_constants = []
            for r, row_init_ctx in enumerate(row_inits):
                col_exprs = row_init_ctx.expression()
                if len(col_exprs) != cols:
                    raise ValueError(f"Initializer for matrix '{matrix_name}' row {r} has {len(col_exprs)} columns, expected {cols}")

                matrix_cols_constants = []
                current_local_row_values = []
                for c, expr_ctx in enumerate(col_exprs):
                    val = self.visitExpression(expr_ctx, builder)
                    if not is_local and not isinstance(val, ir.Constant):
                         raise ValueError(f"Global matrix initializer element [{r}][{c}] for '{matrix_name}' must be constant.")
                    if val.type != llvm_element_type:
                         if isinstance(llvm_element_type, ir.DoubleType) and isinstance(val.type, ir.IntType):
                              if isinstance(val, ir.Constant):
                                   val = ir.Constant(ir.DoubleType(), float(val.constant))
                              elif is_local:
                                   val = builder.sitofp(val, ir.DoubleType())
                         else:
                              raise TypeError(f"Type mismatch in initializer for '{matrix_name}' at [{r}][{c}]. Expected {llvm_element_type}, got {val.type}")

                    if is_local:
                         current_local_row_values.append(val)
                    else:
                         matrix_cols_constants.append(val)

                if is_local:
                     local_init_values.append(current_local_row_values)
                else:
                     row_const = ir.Constant(ir.ArrayType(llvm_element_type, cols), matrix_cols_constants)
                     matrix_rows_constants.append(row_const)

            if not is_local:
                 initializer_value = ir.Constant(matrix_type, matrix_rows_constants)

        if is_local:
            ptr = builder.alloca(matrix_type, name=matrix_name)
            target_table[matrix_name] = ptr
            if ctx.matrix_initializer():
                 zero = ir.Constant(ir.IntType(32), 0)
                 for r in range(rows):
                      for c in range(cols):
                           row_idx = ir.Constant(ir.IntType(32), r)
                           col_idx = ir.Constant(ir.IntType(32), c)
                           elem_ptr = builder.gep(ptr, [zero, row_idx, col_idx], name=f"{matrix_name}_{r}_{c}_ptr")
                           value_to_store = local_init_values[r][c]
                           builder.store(value_to_store, elem_ptr)
        else:
            global_matrix = ir.GlobalVariable(self.module, matrix_type, name=matrix_name)
            global_matrix.linkage = 'internal'
            global_matrix.initializer = initializer_value
            target_table[matrix_name] = global_matrix


    def visitMatrix_assignment(self, ctx:SimpleLangParser.Matrix_assignmentContext, builder=None):
        matrix_name = ctx.ID().getText()

        var_ptr = None
        is_local = False
        if self.current_function and matrix_name in self.local_symbol_table.get(self.current_function, {}):
            var_ptr = self.local_symbol_table[self.current_function][matrix_name]
            is_local = True
        elif matrix_name in self.symbol_table:
            var_ptr = self.symbol_table[matrix_name]
            is_local = False
        else:
            raise ValueError(f"Matrix '{matrix_name}' is not declared")

        if not isinstance(var_ptr.type.pointee, ir.ArrayType) or \
           not isinstance(var_ptr.type.pointee.element, ir.ArrayType):
            raise TypeError(f"Variable '{matrix_name}' is not a matrix.")

        matrix_type = var_ptr.type.pointee
        row_type = matrix_type.element
        llvm_element_type = row_type.element
        rows = matrix_type.count
        cols = row_type.count

        target_builder = builder
        end_fun = False
        if not is_local and not target_builder:
            end_fun = True
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_massign_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(block)
            print(f'New dummy function for global matrix assignment: {func.name}')

        init_ctx = ctx.matrix_initializer()
        row_inits = init_ctx.row_initializer()
        if len(row_inits) != rows:
            raise ValueError(f"Initializer for matrix assignment '{matrix_name}' has {len(row_inits)} rows, expected {rows}")

        zero = ir.Constant(ir.IntType(32), 0)
        for r, row_init_ctx in enumerate(row_inits):
            col_exprs = row_init_ctx.expression()
            if len(col_exprs) != cols:
                raise ValueError(f"Initializer for matrix assignment '{matrix_name}' row {r} has {len(col_exprs)} columns, expected {cols}")

            row_idx = ir.Constant(ir.IntType(32), r)
            for c, expr_ctx in enumerate(col_exprs):
                value = self.visitExpression(expr_ctx, target_builder)
                if value.type != llvm_element_type:
                     if isinstance(llvm_element_type, ir.DoubleType) and isinstance(value.type, ir.IntType) and value.type.width == 32:
                          value = target_builder.sitofp(value, ir.DoubleType())
                     elif isinstance(llvm_element_type, ir.IntType) and llvm_element_type.width == 32 and isinstance(value.type, ir.DoubleType):
                          value = target_builder.fptosi(value, ir.IntType(32))
                     else:
                         raise TypeError(f"Type mismatch in matrix assignment initializer for '{matrix_name}' at [{r}][{c}]. Expected {llvm_element_type}, got {value.type}")

                col_idx = ir.Constant(ir.IntType(32), c)
                elem_ptr = target_builder.gep(var_ptr, [zero, row_idx, col_idx], name=f"{matrix_name}_{r}_{c}_ptr")
                target_builder.store(value, elem_ptr)

        if end_fun:
            target_builder.ret_void()


    def visitMatrix_element_assignment(self, ctx:SimpleLangParser.Matrix_element_assignmentContext, builder=None):
        matrix_name = ctx.ID().getText()

        var_ptr = None
        is_local = False
        if self.current_function and matrix_name in self.local_symbol_table.get(self.current_function, {}):
            var_ptr = self.local_symbol_table[self.current_function][matrix_name]
            is_local = True
        elif matrix_name in self.symbol_table:
            var_ptr = self.symbol_table[matrix_name]
            is_local = False
        else:
            raise ValueError(f"Matrix '{matrix_name}' is not declared")

        # Check type - must be pointer to array of array
        if not isinstance(var_ptr.type.pointee, ir.ArrayType) or \
           not isinstance(var_ptr.type.pointee.element, ir.ArrayType):
            raise TypeError(f"Variable '{matrix_name}' is not a matrix.")

        llvm_element_type = var_ptr.type.pointee.element.element

        target_builder = builder
        end_fun = False
        if not is_local and not target_builder:
            end_fun = True
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_melem_assign_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(block)
            print(f'New dummy function for global matrix element assignment: {func.name}')


        row_index_val = self.visitExpression(ctx.expression(0), target_builder)
        col_index_val = self.visitExpression(ctx.expression(1), target_builder)
        value_val = self.visitExpression(ctx.expression(2), target_builder)

        if not isinstance(row_index_val.type, ir.IntType):
             raise TypeError(f"Matrix row index for '{matrix_name}' must be an integer, got {row_index_val.type}")
        if row_index_val.type.width != 32:
             row_index_val = target_builder.sext(row_index_val, ir.IntType(32)) # Or zext

        if not isinstance(col_index_val.type, ir.IntType):
             raise TypeError(f"Matrix column index for '{matrix_name}' must be an integer, got {col_index_val.type}")
        if col_index_val.type.width != 32:
             col_index_val = target_builder.sext(col_index_val, ir.IntType(32)) # Or zext

        if value_val.type != llvm_element_type:
             if isinstance(llvm_element_type, ir.DoubleType) and isinstance(value_val.type, ir.IntType) and value_val.type.width == 32:
                  value_val = target_builder.sitofp(value_val, ir.DoubleType())
             elif isinstance(llvm_element_type, ir.IntType) and llvm_element_type.width == 32 and isinstance(value_val.type, ir.DoubleType):
                  value_val = target_builder.fptosi(value_val, ir.IntType(32))
             else:
                  raise TypeError(f"Type mismatch in matrix element assignment to '{matrix_name}'. Expected {llvm_element_type}, got {value_val.type}")

        zero = ir.Constant(ir.IntType(32), 0)
        elem_ptr = target_builder.gep(var_ptr, [zero, row_index_val, col_index_val], name=f"{matrix_name}_elem_ptr")

        target_builder.store(value_val, elem_ptr)

        if end_fun:
            target_builder.ret_void()
 

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
                
             # 📦 Obsługa tablic
            if isinstance(pointee_type, ir.ArrayType):
                elem_type = pointee_type.element
                length = pointee_type.count

                fmt = {
                    ir.IntType(32): "%d ",
                    ir.DoubleType(): "%f ",
                    ir.IntType(1): "%d ",
                }.get(elem_type, None)

                if fmt is None:
                    raise ValueError(f"Unsupported array element type: {elem_type}")

                fmt_var = self._create_global_format_str(fmt)
                fmt_ptr = builder.bitcast(fmt_var, ir.IntType(8).as_pointer())

                for i in range(length):
                    elem_ptr = builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
                    val = builder.load(elem_ptr)
                    if isinstance(val.type, ir.IntType) and val.type.width == 1:
                        val = builder.zext(val, ir.IntType(32))  # rozszerz bool do int32
                    builder.call(self.printf, [fmt_ptr, val])

                # nowa linia po tablicy
                newline_fmt = self._create_global_format_str("\n")
                newline_ptr = builder.bitcast(newline_fmt, ir.IntType(8).as_pointer())
                builder.call(self.printf, [newline_ptr])
                if end_fun:
                    builder.ret_void()
                return  # ⬅ uniknij dalszego kodu


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

        elif ctx.getChildCount() == 4 and \
                isinstance(ctx.getChild(0), TerminalNode) and ctx.getChild(0).symbol.type == SimpleLangLexer.ID and \
                ctx.getChild(1).getText() == '[' and \
                isinstance(ctx.getChild(2), SimpleLangParser.ExpressionContext) and \
                ctx.getChild(3).getText() == ']':

            print("Handling Table Element Access")  # Debug
            var_name = ctx.getChild(0).getText()
            index_expr = ctx.getChild(2)
            index_val = self.visitExpression(index_expr, builder)

            if not isinstance(index_val.type, ir.IntType):
                raise TypeError(f"Table index for '{var_name}' must be integer, got {index_val.type}")
            if index_val.type.width != 32:
                index_val = builder.sext(index_val, ir.IntType(32))

            array_ptr = None
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                array_ptr = self.local_symbol_table[self.current_function].get(var_name)
            elif var_name in self.symbol_table:
                array_ptr = self.symbol_table.get(var_name)

            if array_ptr is None:
                raise ValueError(f"Array/Table '{var_name}' is not declared")

            if not isinstance(array_ptr.type.pointee, ir.ArrayType):
                raise TypeError(f"Variable '{var_name}' is not an array/table")

            zero = ir.Constant(ir.IntType(32), 0)
            elem_ptr = builder.gep(array_ptr, [zero, index_val], name=f"{var_name}_elem_ptr")

            return builder.load(elem_ptr, name=f"{var_name}_elem")

        elif ctx.getChildCount() == 7 and \
                isinstance(ctx.getChild(0), TerminalNode) and ctx.getChild(0).symbol.type == SimpleLangLexer.ID and \
                ctx.getChild(1).getText() == '[' and \
                isinstance(ctx.getChild(2), SimpleLangParser.ExpressionContext) and \
                ctx.getChild(3).getText() == ']' and \
                ctx.getChild(4).getText() == '[' and \
                isinstance(ctx.getChild(5), SimpleLangParser.ExpressionContext) and \
                ctx.getChild(6).getText() == ']':

            print("Handling Matrix Element Access")  # Debug
            matrix_name = ctx.getChild(0).getText()
            row_expr = ctx.getChild(2)
            col_expr = ctx.getChild(5)

            row_val = self.visitExpression(row_expr, builder)
            col_val = self.visitExpression(col_expr, builder)

            if not isinstance(row_val.type, ir.IntType):
                raise TypeError(f"Matrix row index for '{matrix_name}' must be integer, got {row_val.type}")
            if row_val.type.width != 32:
                row_val = builder.sext(row_val, ir.IntType(32))

            if not isinstance(col_val.type, ir.IntType):
                raise TypeError(f"Matrix column index for '{matrix_name}' must be integer, got {col_val.type}")
            if col_val.type.width != 32:
                col_val = builder.sext(col_val, ir.IntType(32))

            matrix_ptr = None
            if self.current_function and matrix_name in self.local_symbol_table.get(self.current_function, {}):
                matrix_ptr = self.local_symbol_table[self.current_function].get(matrix_name)
            elif matrix_name in self.symbol_table:
                matrix_ptr = self.symbol_table.get(matrix_name)

            if matrix_ptr is None:
                raise ValueError(f"Matrix '{matrix_name}' is not declared")

            if not isinstance(matrix_ptr.type.pointee, ir.ArrayType) or \
                    not isinstance(matrix_ptr.type.pointee.element, ir.ArrayType):
                raise TypeError(f"Identifier '{matrix_name}' is not a matrix.")

            zero = ir.Constant(ir.IntType(32), 0)
            elem_ptr = builder.gep(matrix_ptr, [zero, row_val, col_val], name=f"{matrix_name}_elem_ptr")

            return builder.load(elem_ptr, name=f"{matrix_name}_elem")


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
      
    def visitLoop_for_iterator(self, ctx, builder=None):
        end_fun = False
        if not builder:
            end_fun = True        
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_for_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)

        index_name = ctx.ID(0).getText()       # ID przed przecinkiem
        value_name = ctx.ID(1).getText()       # ID po przecinku
        table_name = ctx.ID(2).getText()       # nazwa tablicy w iteratorze
        
        #sprawdzanie czy zmienne są zadeklarowane
        if self.current_function:
            var_ptr = self.local_symbol_table[self.current_function].get(index_name)
            # print(f"Local variable '{table_name}' found in function '{self.current_function}'")
        else:
            var_ptr = self.symbol_table.get(index_name)
        if var_ptr is not None:
            raise ValueError(f"Variable '{table_name}' is allredy declared")
        
        if self.current_function:
            var_ptr = self.local_symbol_table[self.current_function].get(value_name)
            # print(f"Local variable '{table_name}' found in function '{self.current_function}'")
        else:
            var_ptr = self.symbol_table.get(value_name)
        if var_ptr is not None:
            raise ValueError(f"Variable '{table_name}' is allredy declared")
        
        if self.current_function:
            var_ptr = self.local_symbol_table[self.current_function].get(table_name)
            print(f"Local variable '{table_name}' found in function '{self.current_function}'")
        else:
            var_ptr = self.symbol_table.get(table_name)
            print(f"Global variable '{table_name}' found")
            print(self.symbol_table)
            print(self.symbol_table.get(table_name))
            print(f"[{table_name}]") 
        if var_ptr is None:
            raise ValueError(f"Variable '{table_name}' is not declared")
        #sprawdzenie czy zmienna jest tablicą
        pointee_type = var_ptr.type.pointee
        if not isinstance(pointee_type, ir.ArrayType):
            raise ValueError(f"Variable '{table_name}' is not an array")
        
        table_len = pointee_type.count
        elem_type = pointee_type.element
        
        # Tworzenie indeksu pętli
        index_ptr = builder.alloca(ir.IntType(32), name=index_name)
        builder.store(ir.Constant(ir.IntType(32), 0), index_ptr)
        # Wskaźnik na aktualny element
        value_ptr = builder.alloca(elem_type, name=value_name)
        
        if self.current_function:
            self.local_symbol_table[self.current_function][index_name] = index_ptr
            self.local_symbol_table[self.current_function][value_name] = value_ptr
        else:
            self.symbol_table[index_name] = index_ptr
            self.symbol_table[value_name] = value_ptr            
        
        loop_cond_block = builder.append_basic_block('for_cond')
        loop_body_block = builder.append_basic_block('for_body')
        loop_inc_block = builder.append_basic_block('for_inc')
        loop_end_block = builder.append_basic_block('for_end')

        builder.branch(loop_cond_block)
        
        # Warunek pętli
        builder.position_at_end(loop_cond_block)
        index_val = builder.load(index_ptr, name="idx_val")
        end_val = ir.Constant(ir.IntType(32), table_len)
        cond = builder.icmp_signed('<', index_val, end_val, name="loop_cond")
        builder.cbranch(cond, loop_body_block, loop_end_block)
        
        # Ciało pętli
        builder.position_at_end(loop_body_block)

        # Załaduj element z tablicy
        elem_ptr = builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), index_val], name="elem_ptr")
        elem_val = builder.load(elem_ptr, name="elem_val")
        builder.store(elem_val, value_ptr)

        # Odwiedź ciało pętli
        self.visitCode_block(ctx.code_block(), builder)
        
         # Inkrementuj indeks
        if not builder.block.is_terminated:
            builder.branch(loop_inc_block)

        builder.position_at_end(loop_inc_block)
        current_idx = builder.load(index_ptr)
        incremented = builder.add(current_idx, ir.Constant(ir.IntType(32), 1))
        builder.store(incremented, index_ptr)
        builder.branch(loop_cond_block)

        # Blok końca
        builder.position_at_end(loop_end_block)
        
        # Usunięcie zmiennych lokalnych
        if self.current_function:
            del self.local_symbol_table[self.current_function][index_name]
            del self.local_symbol_table[self.current_function][value_name]
        else:
            del self.symbol_table[index_name]
            del self.symbol_table[value_name]

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
        elif ctx.table_declaration():
            self.visitTable_declaration(ctx.table_declaration(), builder)
        elif ctx.table_assignment():
            self.visitTable_assignment(ctx.table_assignment(), builder)
        elif ctx.loop_for_iterator():
            self.visitLoop_for_iterator(ctx.loop_for_iterator(), builder)
        elif ctx.matrix_declaration():
            self.visitMatrix_declaration(ctx.matrix_declaration(), builder)
        elif ctx.matrix_assignment():
            self.visitMatrix_assignment(ctx.matrix_assignment(), builder)
        elif ctx.matrix_element_assignment():
            self.visitMatrix_element_assignment(ctx.matrix_element_assignment(), builder)
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
        filepath = 'code1.txt'
    if os.path.exists(filepath):
        with open("code1.txt", "r") as f:
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
