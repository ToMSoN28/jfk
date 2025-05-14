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
        self.struct_types={}

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

    def _get_llvm_type_from_str(self, type_str):
        if type_str == 'int':
            return ir.IntType(32)
        elif type_str == 'float':
            return ir.DoubleType()
        elif type_str == 'bool':
            return ir.IntType(1)
        elif type_str == 'string':
            return ir.IntType(8).as_pointer()
        elif type_str in self.struct_types:
            return self.struct_types[type_str]['llvm_type']
        else:
            raise TypeError(f"Unknown type: {type_str}")

    def visitStruct_definition(self, ctx: SimpleLangParser.Struct_definitionContext):
        struct_name = ctx.ID().getText()
        if struct_name in self.struct_types:
            raise NameError(f"Struct type '{struct_name}' already defined.")

        field_llvm_types = []
        field_info = {}
        ordered_field_names = []
        field_idx = 0

        for field_decl_ctx in ctx.field_declaration():
            field_type_str = field_decl_ctx.type_().getText()
            field_name = field_decl_ctx.ID().getText()

            if field_name in field_info:
                raise NameError(f"Duplicate field name '{field_name}' in struct '{struct_name}'")

            llvm_field_type = self._get_llvm_type_from_str(field_type_str)

            field_llvm_types.append(llvm_field_type)
            field_info[field_name] = (field_idx, llvm_field_type)
            ordered_field_names.append(field_name)
            field_idx += 1

        llvm_struct_type = ir.LiteralStructType(field_llvm_types)

        self.struct_types[struct_name] = {
            'llvm_type': llvm_struct_type,
            'fields': field_info,
            'ordered_field_names': ordered_field_names
        }
        return None

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

    def visitVariable_declaration(self, ctx: SimpleLangParser.Variable_declarationContext, builder=None):
        var_name = None
        type_str_from_keyword = None  # For 'int', 'float', etc.
        type_str_from_id = None  # For struct type name like 'Point'
        llvm_type = None
        initializer = None
        line_number_info = ctx.start.line  # Default line info from the start of the rule

        # Determine which alternative of variable_declaration was matched
        if hasattr(ctx, 'type_name') and ctx.type_name:  # Matched: type_name=ID var_name=ID ';' (Struct declaration)
            type_name_node = ctx.type_name  # This is a Token object
            var_name_node = ctx.var_name  # This is a Token object

            type_str_from_id = type_name_node.text
            var_name = var_name_node.text
            # Use the token's line number directly
            line_number_info = type_name_node.line

            if var_name == "<missing ID>":  # This check might be redundant if parser enforces ID
                raise AttributeError(
                    f"Missing variable name for struct instance (line {var_name_node.line}).")  # Use .line
            if type_str_from_id == "<missing ID>":
                raise AttributeError(
                    f"Missing type name for struct instance (line {type_name_node.line}).")  # Use .line

            if type_str_from_id not in self.struct_types:
                # *** CORRECTED LINE HERE ***
                raise TypeError(
                    f"Unknown struct type: '{type_str_from_id}' (line {type_name_node.line if type_name_node else 'unknown'}).")

            llvm_type = self.struct_types[type_str_from_id]['llvm_type']
            initializer = ir.Constant(llvm_type, None) if not builder else None

        else:  # Matched one of the primitive type declarations
            var_name_node = ctx.var_name  # This is a Token object
            if not var_name_node:
                raise AttributeError(
                    f"Variable name ID node not found in declaration context (line {line_number_info}).")
            var_name = var_name_node.text
            # Use the token's line number directly
            line_number_info = var_name_node.line

            if var_name == "<missing ID>":
                raise AttributeError(f"Missing variable name (line {var_name_node.line}).")  # Use .line

            type_keyword_node = ctx.getChild(0)
            type_str_from_keyword = type_keyword_node.getText()

            if type_str_from_keyword == 'int':
                llvm_type = ir.IntType(32)
                if ctx.NUMBER():
                    initializer = ir.Constant(llvm_type, int(ctx.NUMBER().getText()))
                else:
                    initializer = ir.Constant(llvm_type, 0)
            elif type_str_from_keyword == 'float':
                llvm_type = ir.DoubleType()
                if ctx.FLOAT():
                    initializer = ir.Constant(llvm_type, float(ctx.FLOAT().getText()))
                else:
                    initializer = ir.Constant(llvm_type, 0.0)
            elif type_str_from_keyword == 'bool':
                llvm_type = ir.IntType(1)
                if ctx.boolean_expression():
                    init_val = self.visitBooleanExpression(ctx.boolean_expression(), builder if builder else None)
                    if isinstance(init_val, ir.Constant):
                        initializer = init_val
                    elif builder:
                        initializer = init_val
                    else:
                        print(
                            f"Warning: Non-constant initializer for global boolean '{var_name}'. Defaulting to false.")
                        initializer = ir.Constant(llvm_type, 0)
                else:
                    initializer = ir.Constant(llvm_type, 0)
            elif type_str_from_keyword == 'string':
                llvm_type = ir.IntType(8).as_pointer()
                if ctx.STRING():
                    text_content = ctx.STRING().getText()[1:-1] + '\0'
                    str_bytes = bytearray(text_content.encode("utf8"))
                    str_arr_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
                    global_str_name = f".str.decl.{var_name}.{self.module.name}.{self.function_counter}"
                    self.function_counter += 1

                    global_str_literal = ir.GlobalVariable(self.module, str_arr_type, name=global_str_name)
                    global_str_literal.linkage = 'internal'
                    global_str_literal.global_constant = True
                    global_str_literal.initializer = ir.Constant(str_arr_type, str_bytes)
                    initializer = global_str_literal.bitcast(llvm_type)
                else:
                    initializer = ir.Constant(llvm_type, None)
            else:
                # *** CORRECTED LINE HERE for var_name_node.line ***
                raise ValueError(
                    f"Unsupported type keyword '{type_str_from_keyword}' for variable: {var_name} (line {var_name_node.line if var_name_node else 'unknown'}).")

        # Allocation and storage logic
        if not builder:
            if var_name in self.symbol_table:
                raise ValueError(f"Global variable '{var_name}' already declared (line {line_number_info}).")
            global_var = ir.GlobalVariable(self.module, llvm_type, name=var_name)
            global_var.initializer = initializer
            global_var.linkage = 'internal'
            global_var.global_constant = False
            self.symbol_table[var_name] = global_var
        else:
            if self.current_function is None:
                raise Exception(
                    f"Trying to declare a local variable '{var_name}' outside a function context (line {line_number_info}).")
            if var_name in self.local_symbol_table.get(self.current_function, {}):
                raise ValueError(
                    f"Local variable '{var_name}' already declared in function '{self.current_function}' (line {line_number_info}).")

            ptr = builder.alloca(llvm_type, name=var_name)
            if type_str_from_id:  # Struct type
                pass
            elif initializer is not None:  # Primitive type
                builder.store(initializer, ptr)
            else:
                raise ValueError(
                    f"Internal error: No initializer for local primitive '{var_name}' (line {line_number_info})")
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

    def visitAssignment(self, ctx: SimpleLangParser.AssignmentContext, builder=None):
        if hasattr(ctx, 'struct_var') and ctx.struct_var:
            struct_var_name = ctx.struct_var.text
            if not hasattr(ctx, 'field_name') or not ctx.field_name:
                raise ValueError(
                    f"Malformed struct assignment: missing field_name label. Code: {ctx.getText()} at line {ctx.start.line}")
            field_name = ctx.field_name.text
            rhs_expr_ctx = ctx.expression()
            line_info = ctx.struct_var.line

            struct_ptr = None
            if self.current_function and struct_var_name in self.local_symbol_table.get(self.current_function, {}):
                struct_ptr = self.local_symbol_table[self.current_function][struct_var_name]
            elif struct_var_name in self.symbol_table:
                struct_ptr = self.symbol_table[struct_var_name]
            else:
                raise NameError(f"Struct instance '{struct_var_name}' not found for assignment (line {line_info}).")

            if not isinstance(struct_ptr.type.pointee, (ir.LiteralStructType, ir.IdentifiedStructType)):
                raise TypeError(f"Variable '{struct_var_name}' is not a struct instance (line {line_info}).")

            actual_llvm_struct_type = struct_ptr.type.pointee
            struct_type_name = None
            for s_name, s_def in self.struct_types.items():
                if s_def['llvm_type'] == actual_llvm_struct_type:
                    struct_type_name = s_name
                    break
            if not struct_type_name:
                raise TypeError(
                    f"Variable '{struct_var_name}' is not a recognized struct type for assignment (line {line_info}).")

            struct_def = self.struct_types[struct_type_name]
            if field_name not in struct_def['fields']:
                raise AttributeError(
                    f"Struct '{struct_type_name}' has no field named '{field_name}' (line {ctx.field_name.line}).")

            field_index, expected_field_llvm_type = struct_def['fields'][field_name]

            target_builder_struct = builder
            end_fun_struct = False
            if not target_builder_struct and not self.current_function:
                end_fun_struct = True
                dummy_func_name = f"__global_struct_assign_{self.function_counter}"
                self.function_counter += 1
                temp_func_ty = ir.FunctionType(ir.VoidType(), [])
                temp_func = ir.Function(self.module, temp_func_ty, name=dummy_func_name)
                temp_block = temp_func.append_basic_block(name="entry")
                target_builder_struct = ir.IRBuilder(temp_block)
                self.generated_funcs.append(dummy_func_name)

            if not target_builder_struct:
                raise Exception(
                    f"Builder not available for struct field assignment to '{struct_var_name}.{field_name}' (line {line_info}).")

            if not rhs_expr_ctx:
                raise ValueError(
                    f"Missing RHS expression in struct field assignment for '{struct_var_name}.{field_name}' (line {line_info})")
            rhs_value = self.visitExpression(rhs_expr_ctx, target_builder_struct)

            if rhs_value.type != expected_field_llvm_type:
                if isinstance(expected_field_llvm_type, ir.DoubleType) and isinstance(rhs_value.type, ir.IntType):
                    rhs_value = target_builder_struct.sitofp(rhs_value, ir.DoubleType(), name="int_to_float")
                elif isinstance(expected_field_llvm_type, ir.IntType) and isinstance(rhs_value.type,
                                                                                     ir.DoubleType) and expected_field_llvm_type.width == 32:  # Float to Int (example)
                    rhs_value = target_builder_struct.fptosi(rhs_value, expected_field_llvm_type, name="float_to_int")
                else:
                    raise TypeError(
                        f"Type mismatch assigning to field '{struct_var_name}.{field_name}'. Expected {expected_field_llvm_type}, got {rhs_value.type} (line {line_info}).")

            zero = ir.Constant(ir.IntType(32), 0)
            field_ptr = target_builder_struct.gep(struct_ptr, [zero, ir.Constant(ir.IntType(32), field_index)],
                                                  name=f"{struct_var_name}.{field_name}.ptr")
            target_builder_struct.store(rhs_value, field_ptr)

            if end_fun_struct:
                target_builder_struct.ret_void()
            return

        if not hasattr(ctx, 'var_name') or not ctx.var_name:
            raise ValueError(
                f"Malformed assignment context: missing var_name label (line {ctx.start.line}). Input: '{ctx.getText()}'")

        var_name = ctx.var_name.text
        line_info = ctx.var_name.line

        var_ptr_target = None
        if self.current_function:
            if var_name in self.local_symbol_table.get(self.current_function, {}):
                var_ptr_target = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                var_ptr_target = self.symbol_table[var_name]
            else:
                raise ValueError(f"Variable '{var_name}' is not declared (line {line_info}).")
        else:
            if var_name not in self.symbol_table:
                raise ValueError(f"Variable '{var_name}' is not declared globally (line {line_info}).")
            var_ptr_target = self.symbol_table[var_name]

        target_builder_simple = builder
        end_fun_simple = False
        if not target_builder_simple:
            end_fun_simple = True
            func_name = f"dummy_assign_func_{self.function_counter}"
            self.function_counter += 1
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            block = func.append_basic_block(name="entry")
            target_builder_simple = ir.IRBuilder(block)
            self.generated_funcs.append(func_name)

        value_to_store = None
        if ctx.expression():
            value_to_store = self.visitExpression(ctx.expression(), target_builder_simple)
        elif ctx.boolean_expression():
            value_to_store = self.visitBooleanExpression(ctx.boolean_expression(), target_builder_simple)
        else:
            raise ValueError(f"Invalid assignment RHS for '{var_name}' (line {line_info}). Code: {ctx.getText()}")

        expected_type = var_ptr_target.type.pointee
        if isinstance(expected_type, (ir.LiteralStructType, ir.IdentifiedStructType)):
            raise TypeError(
                f"Cannot assign directly to a struct variable '{var_name}'. Assign to its members (line {line_info}).")

        if expected_type != value_to_store.type:
            if isinstance(expected_type, ir.DoubleType) and isinstance(value_to_store.type, ir.IntType):
                value_to_store = target_builder_simple.sitofp(value_to_store, ir.DoubleType())
            elif isinstance(expected_type, ir.IntType) and isinstance(value_to_store.type,
                                                                      ir.DoubleType) and expected_type.width == 32:
                value_to_store = target_builder_simple.fptosi(value_to_store, expected_type)
            else:
                raise TypeError(
                    f"Type mismatch in assignment to '{var_name}'. Expected {expected_type}, got {value_to_store.type} (line {line_info}).")

        target_builder_simple.store(value_to_store, var_ptr_target)

        if end_fun_simple:
            target_builder_simple.ret_void()

    def visitPrint_statement(self, ctx: SimpleLangParser.Print_statementContext, builder=None):
        end_fun = False
        if not builder:
            end_fun = True
            # Ensure self.function_counter is available and used correctly
            func_name = f"dummy_print_func_{self.function_counter}"
            self.function_counter += 1
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            self.generated_funcs.append(func_name)

        value_to_print = None
        fmt_str = None

        # Determine what is being printed
        item_to_print_ctx = ctx.getChild(2)  # child 0 is 'print', 1 is '(', 2 is item, 3 is ')'

        if isinstance(item_to_print_ctx, TerminalNode) and item_to_print_ctx.symbol.type == SimpleLangLexer.STRING:
            text = item_to_print_ctx.getText()[1:-1] + '\0'
            str_bytes = bytearray(text.encode("utf8"))
            str_type = ir.ArrayType(ir.IntType(8), len(str_bytes))

            # Use a unique name for the global string literal for print
            global_str_name = f".str.printlit.{self.function_counter}"
            self.function_counter += 1

            global_str = ir.GlobalVariable(self.module, str_type, name=global_str_name)
            global_str.linkage = 'internal'
            global_str.global_constant = True
            global_str.initializer = ir.Constant(str_type, str_bytes)
            value_to_print = builder.bitcast(global_str, ir.IntType(8).as_pointer())
            fmt_str = "%s\n"

        elif isinstance(item_to_print_ctx, SimpleLangParser.ExpressionContext):
            value_to_print = self.visitExpression(item_to_print_ctx, builder)

        elif isinstance(item_to_print_ctx, SimpleLangParser.Boolean_expressionContext):
            value_to_print = self.visitBooleanExpression(item_to_print_ctx, builder)
            # Booleans will be i1, need to determine fmt later and possibly zext

        elif isinstance(item_to_print_ctx, TerminalNode) and item_to_print_ctx.symbol.type == SimpleLangLexer.ID:
            # This handles printing a simple ID directly (variable)
            var_name = item_to_print_ctx.getText()
            var_ptr = None
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                var_ptr = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                var_ptr = self.symbol_table[var_name]
            else:
                raise NameError(
                    f"Variable '{var_name}' not found in print statement (line {item_to_print_ctx.symbol.line}).")

            # Special handling for printing arrays/tables directly by ID
            if isinstance(var_ptr.type.pointee, ir.ArrayType):
                pointee_type = var_ptr.type.pointee
                elem_type = pointee_type.element
                length = pointee_type.count
                array_fmt_char = None
                if elem_type == ir.IntType(32):
                    array_fmt_char = "%d "
                elif elem_type == ir.DoubleType():
                    array_fmt_char = "%f "
                elif elem_type == ir.IntType(1):
                    array_fmt_char = "%d "  # Print bools as 0 or 1
                # Add other array element types if needed (e.g. i8* for array of strings)
                else:
                    raise ValueError(
                        f"Unsupported array element type for printing: {elem_type} (line {item_to_print_ctx.symbol.line}).")

                fmt_var_array = self._create_global_format_str(array_fmt_char)
                fmt_ptr_array = builder.bitcast(fmt_var_array, ir.IntType(8).as_pointer())

                for i in range(length):
                    elem_addr = builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
                    val_loaded = builder.load(elem_addr)
                    if isinstance(val_loaded.type, ir.IntType) and val_loaded.type.width == 1:  # Bool
                        val_loaded = builder.zext(val_loaded, ir.IntType(32))
                    builder.call(self.printf, [fmt_ptr_array, val_loaded])

                newline_fmt_var = self._create_global_format_str("\n")  # Print newline after array
                newline_fmt_ptr = builder.bitcast(newline_fmt_var, ir.IntType(8).as_pointer())
                builder.call(self.printf, [newline_fmt_ptr])

                if end_fun: builder.ret_void()
                return  # Handled array printing

            # For other ID types (int, float, bool, string var), load the value
            value_to_print = builder.load(var_ptr, name=var_name + "_val")
        else:
            raise ValueError(
                f"Unsupported item type in print statement: {type(item_to_print_ctx)} (line {ctx.start.line})")

        # Determine format specifier if not already set (e.g. for expressions or loaded IDs)
        if fmt_str is None:
            if value_to_print is None:  # Should have been set by one of the branches above
                raise ValueError("Internal error: value_to_print is None in print_statement.")

            val_type = value_to_print.type
            if isinstance(val_type, ir.IntType) and val_type.width == 32:  # int
                fmt_str = "%d\n"
            elif isinstance(val_type, ir.DoubleType):  # float
                fmt_str = "%f\n"
            elif isinstance(val_type, ir.IntType) and val_type.width == 1:  # bool
                fmt_str = "%d\n"
                value_to_print = builder.zext(value_to_print, ir.IntType(32))  # Promote bool to int for printf %d
            elif isinstance(val_type, ir.PointerType) and \
                    isinstance(val_type.pointee, ir.IntType) and \
                    val_type.pointee.width == 8:  # string (i8*)
                fmt_str = "%s\n"
            else:
                raise ValueError(f"Unsupported type for print: {value_to_print.type} (line {ctx.start.line})")

        # Create global format string and call printf
        fmt_var_final = self._create_global_format_str(fmt_str)
        fmt_ptr_final = builder.bitcast(fmt_var_final, ir.IntType(8).as_pointer())
        builder.call(self.printf, [fmt_ptr_final, value_to_print])

        if end_fun:
            builder.ret_void()

    def visitExpression(self, ctx: SimpleLangParser.ExpressionContext, builder: ir.IRBuilder):
        if ctx is None:
            raise ValueError("visitExpression called with ctx=None")

        # Check based on the #labeled alternatives from your grammar
        if isinstance(ctx, SimpleLangParser.StringExprContext):
            string_node = ctx.STRING()  # StringExprContext will have a STRING() method
            text = string_node.getText()[1:-1] + '\0'
            str_bytes = bytearray(text.encode("utf8"))
            str_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
            str_const_name = f".str.literal.{self.function_counter}"
            self.function_counter += 1

            global_str = self.module.globals.get(str_const_name)
            if global_str is None:
                global_str = ir.GlobalVariable(self.module, str_type, name=str_const_name)
                global_str.linkage = 'internal'
                global_str.global_constant = True
                global_str.initializer = ir.Constant(str_type, str_bytes)

            return builder.bitcast(global_str, ir.IntType(8).as_pointer(), name="str_ptr")

        elif isinstance(ctx, SimpleLangParser.NumberExprContext):
            return ir.Constant(ir.IntType(32), int(ctx.NUMBER().getText()))

        elif isinstance(ctx, SimpleLangParser.FloatExprContext):
            return ir.Constant(ir.DoubleType(), float(ctx.FLOAT().getText()))

        elif isinstance(ctx, SimpleLangParser.VariableExprContext):
            var_name = ctx.ID().getText()
            ptr = None
            line_info = ctx.ID().getSymbol().line
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                ptr = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                ptr = self.symbol_table[var_name]
            else:
                raise NameError(f"Variable '{var_name}' not found (line {line_info}).")

            if isinstance(ptr.type.pointee, (ir.LiteralStructType, ir.IdentifiedStructType)):
                raise TypeError(
                    f"Cannot use struct '{var_name}' directly as an expression. Access its members (line {line_info}).")
            return builder.load(ptr, name=var_name)

        elif isinstance(ctx, SimpleLangParser.MulDivContext) or \
                isinstance(ctx, SimpleLangParser.AddSubContext):
            # These contexts will have expression(0), expression(1), and op
            left_expr_ctx = ctx.expression(0)
            right_expr_ctx = ctx.expression(1)

            left = self.visitExpression(left_expr_ctx, builder)
            right = self.visitExpression(right_expr_ctx, builder)
            op_text = ctx.op.text  # op is a Token (the operator like '+' or '*')

            is_left_float = isinstance(left.type, ir.DoubleType)
            is_right_float = isinstance(right.type, ir.DoubleType)
            is_float_op = is_left_float or is_right_float

            if is_float_op:
                if not is_left_float: left = builder.sitofp(left, ir.DoubleType(), name="l_to_f")
                if not is_right_float: right = builder.sitofp(right, ir.DoubleType(), name="r_to_f")

                if op_text == '+':
                    return builder.fadd(left, right, name='faddtmp')
                elif op_text == '-':
                    return builder.fsub(left, right, name='fsubtmp')
                elif op_text == '*':
                    return builder.fmul(left, right, name='fmultmp')
                elif op_text == '/':
                    return builder.fdiv(left, right, name='fdivtmp')
                else:
                    raise ValueError(f"Unsupported float binary operator: {op_text} (line {ctx.op.line})")
            else:
                if op_text == '+':
                    return builder.add(left, right, name='addtmp')
                elif op_text == '-':
                    return builder.sub(left, right, name='subtmp')
                elif op_text == '*':
                    return builder.mul(left, right, name='multmp')
                elif op_text == '/':
                    return builder.sdiv(left, right, name='sdivtmp')
                else:
                    raise ValueError(f"Unsupported int binary operator: {op_text} (line {ctx.op.line})")

        elif isinstance(ctx, SimpleLangParser.ParensExprContext):
            # ParensExprContext will have an expression() method for the inner expression
            return self.visitExpression(ctx.expression(), builder)

        elif isinstance(ctx, SimpleLangParser.StructMemberAccessExprContext):
            # StructMemberAccessExprContext has expression() for the base and ID() for the field
            struct_instance_expr_ctx = ctx.expression()  # Note: ANTLR might make this expression(0) if multiple
            field_name = ctx.ID().getText()
            line_info = ctx.ID().getSymbol().line

            struct_ptr = None
            struct_type_name_for_access = None

            def get_var_ptr_for_struct_access(expr_ctx_local):  # Renamed to avoid clash
                nonlocal struct_type_name_for_access
                if isinstance(expr_ctx_local, SimpleLangParser.VariableExprContext):
                    var_name_local = expr_ctx_local.ID().getText()
                    ptr_local = None
                    if self.current_function and var_name_local in self.local_symbol_table.get(self.current_function,
                                                                                               {}):
                        ptr_local = self.local_symbol_table[self.current_function][var_name_local]
                    elif var_name_local in self.symbol_table:
                        ptr_local = self.symbol_table[var_name_local]

                    if ptr_local and isinstance(ptr_local.type.pointee,
                                                (ir.LiteralStructType, ir.IdentifiedStructType)):
                        actual_llvm_st_type = ptr_local.type.pointee
                        for s_name, s_def_local in self.struct_types.items():
                            if s_def_local['llvm_type'] == actual_llvm_st_type:
                                struct_type_name_for_access = s_name
                                break
                        return ptr_local
                    elif ptr_local:
                        raise TypeError(
                            f"Variable '{var_name_local}' used in member access is not a struct (line {expr_ctx_local.ID().getSymbol().line}).")
                    else:
                        raise NameError(
                            f"Struct variable '{var_name_local}' not found (line {expr_ctx_local.ID().getSymbol().line}).")
                # If base is another StructMemberAccessExpr or TableElemExpr, etc.
                elif isinstance(expr_ctx_local, SimpleLangParser.StructMemberAccessExprContext):
                    # This would be for p.q.r - requires careful pointer handling
                    # Base_ptr would be the GEP to p.q
                    # This needs careful implementation if you support chained access directly this way
                    raise NotImplementedError(
                        f"Chained struct member access like 'a.b.c' needs careful pointer handling via GEPs from intermediate field pointers.")

                raise NotImplementedError(
                    f"Struct member access for base expression '{expr_ctx_local.getText()}' not fully supported if not simple ID.")

            struct_ptr = get_var_ptr_for_struct_access(struct_instance_expr_ctx)

            if not struct_type_name_for_access or struct_type_name_for_access not in self.struct_types:
                raise TypeError(
                    f"Could not determine struct type for member access on '{struct_instance_expr_ctx.getText()}' (line {line_info}).")

            struct_def = self.struct_types[struct_type_name_for_access]
            if field_name not in struct_def['fields']:
                raise AttributeError(
                    f"Struct '{struct_type_name_for_access}' has no field '{field_name}' (line {line_info}).")

            field_idx, _ = struct_def['fields'][field_name]
            zero = ir.Constant(ir.IntType(32), 0)
            # struct_ptr is already the pointer to the struct instance (e.g. alloca for local, global var for global)
            field_llvm_ptr = builder.gep(struct_ptr, [zero, ir.Constant(ir.IntType(32), field_idx)],
                                         name=f"{field_name}_ptr")
            return builder.load(field_llvm_ptr, name=field_name)

        elif isinstance(ctx, SimpleLangParser.TableElemExprContext):
            var_name = ctx.ID().getText()  # TableElemExpr has ID() and expression()
            index_expr_ctx = ctx.expression()  # Assuming only one expression for index
            line_info_arr = ctx.ID().getSymbol().line

            base_ptr = None
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                base_ptr = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                base_ptr = self.symbol_table[var_name]
            else:
                raise NameError(f"Array '{var_name}' not declared (line {line_info_arr}).")

            if not isinstance(base_ptr.type.pointee, ir.ArrayType):
                raise TypeError(f"Variable '{var_name}' is not an array/table (line {line_info_arr}).")

            index_val = self.visitExpression(index_expr_ctx, builder)
            if not isinstance(index_val.type, ir.IntType):
                raise TypeError(f"Table index for '{var_name}' must be int (line {index_expr_ctx.start.line}).")

            indices = [ir.Constant(ir.IntType(32), 0), index_val]
            elem_ptr = builder.gep(base_ptr, indices, name=f"{var_name}_elem_ptr")
            return builder.load(elem_ptr, name=f"{var_name}_elem")

        elif isinstance(ctx, SimpleLangParser.MatrixElemExprContext):
            var_name = ctx.ID().getText()  # MatrixElemExpr has ID() and two expression()
            row_expr_ctx = ctx.expression(0)
            col_expr_ctx = ctx.expression(1)
            line_info_mat = ctx.ID().getSymbol().line

            base_ptr = None
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                base_ptr = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                base_ptr = self.symbol_table[var_name]
            else:
                raise NameError(f"Matrix '{var_name}' not declared (line {line_info_mat}).")

            if not (isinstance(base_ptr.type.pointee, ir.ArrayType) and \
                    isinstance(base_ptr.type.pointee.element, ir.ArrayType)):
                raise TypeError(f"Variable '{var_name}' is not a matrix (line {line_info_mat}).")

            row_val = self.visitExpression(row_expr_ctx, builder)
            col_val = self.visitExpression(col_expr_ctx, builder)
            if not isinstance(row_val.type, ir.IntType): raise TypeError(
                f"Matrix row index for '{var_name}' must be int.")
            if not isinstance(col_val.type, ir.IntType): raise TypeError(
                f"Matrix col index for '{var_name}' must be int.")

            indices = [ir.Constant(ir.IntType(32), 0), row_val, col_val]
            elem_ptr = builder.gep(base_ptr, indices, name=f"{var_name}_elem_ptr")
            return builder.load(elem_ptr, name=f"{var_name}_elem")

        elif isinstance(ctx, SimpleLangParser.FuncCallExprContext):
            # FuncCallExprContext should have a func_call() method/attribute
            func_call_node = ctx.func_call()
            return self.visit(func_call_node, builder)  # Dispatch to visitFunc_call

        error_line = ctx.start.line if hasattr(ctx, 'start') else 'unknown'
        raise NotImplementedError(
            f"visitExpression: Unhandled expression form: '{ctx.getText()}' (type: {type(ctx)}) at line {error_line}")


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

        if func_name not in self.local_symbol_table:
            self.local_symbol_table[func_name] = {}

        # Pobierz typy i nazwy parametrów
        params = []
        llvm_types = []
        i = 0
        while i < len(param_nodes):
            if param_nodes[i].getText() in ['int', 'float', 'bool', 'string']:
                typ_str = param_nodes[i].getText()
                # Ensure there is a next node for the name
                if i + 1 < len(param_nodes) and isinstance(param_nodes[i + 1], TerminalNode) and param_nodes[
                    i + 1].symbol.type == SimpleLangLexer.ID:
                    name = param_nodes[i + 1].getText()
                    llvm_type = None
                    if typ_str == 'int':
                        llvm_type = ir.IntType(32)
                    elif typ_str == 'float':
                        llvm_type = ir.DoubleType()
                    elif typ_str == 'bool':
                        llvm_type = ir.IntType(1)
                    elif typ_str == 'string':
                        llvm_type = ir.IntType(8).as_pointer()
                    else:
                        raise ValueError(f"Unknown param type: {typ_str}")

                    llvm_types.append(llvm_type)
                    params.append((name, llvm_type))
                    i += 2
                else:
                    raise SyntaxError(f"Expected parameter name after type '{typ_str}' in function {func_name}")
            elif param_nodes[i].getText() == ',':
                i += 1
            else:
                i += 1

        # Typ zwracany
        if return_type_str == 'int':
            return_type = ir.IntType(32)
        elif return_type_str == 'float':
            return_type = ir.DoubleType()
        elif return_type_str == 'bool':
            return_type = ir.IntType(1)
        elif return_type_str == 'string':
            return_type_str == 'string'
        else:
            raise ValueError(f"Unknown return type: {return_type_str}")

        # Stwórz funkcję
        func_type = ir.FunctionType(return_type, llvm_types)
        func = ir.Function(self.module, func_type, name=func_name)
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        # Zainicjalizuj parametry w symbol_table
        for i, (name, typ) in enumerate(params):
            if name in self.local_symbol_table[func_name]:
                raise ValueError(f"Parameter '{name}' redefined in function '{func_name}'")
            param_val = func.args[i]
            param_val.name = name
            ptr = builder.alloca(typ, name=name + ".addr")
            builder.store(param_val, ptr)
            self.local_symbol_table[func_name][name] = ptr

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
            elif isinstance(return_type, ir.PointerType):  # For string return
                builder.ret(ir.Constant(return_type, None))

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

    def visitProgram(self, ctx: SimpleLangParser.ProgramContext):
        for child_ctx in ctx.getChildren():
            if isinstance(child_ctx, SimpleLangParser.Struct_definitionContext):
                self.visitStruct_definition(child_ctx)

        for child_ctx in ctx.getChildren():
            if isinstance(child_ctx, SimpleLangParser.Function_definitionContext):
                self.visitFunction_definition(child_ctx)

        for child_ctx in ctx.getChildren():
            if isinstance(child_ctx, SimpleLangParser.StatementContext):
                self.visit(child_ctx)

        main_ty = ir.FunctionType(ir.IntType(32), [])
        main_fn = ir.Function(self.module, main_ty, name="main")
        block = main_fn.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)

        for func_name in self.generated_funcs:
            func = self.module.get_global(func_name)
            if func is None:
                print(f"Warning: Generated function '{func_name}' not found in module.")
            elif not isinstance(func, ir.Function):
                print(f"Warning: Global '{func_name}' is not a function.")
            else:
                if len(func.args) == 0 and isinstance(func.function_type.return_type, ir.VoidType):
                    builder.call(func, [])
                else:
                    print(f"Warning: Skipping call to generated function '{func_name}' due to unexpected signature.")

        builder.ret(ir.Constant(ir.IntType(32), 0))
        self.module.triple = "aarch64-apple-darwin" # Or your target triple
        self.module.data_layout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128" # Or your target data layout
        print("Generated LLVM IR:")
        print(str(self.module))
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
