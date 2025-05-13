import sys, os
from zipfile import stringFileHeader

from antlr4 import *

from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser  
from SimpleLangVisitor import SimpleLangVisitor
from llvmlite import ir
from test import SimpleLangChecker

class SimpleLangIRVisitor(SimpleLangVisitor):
    def __init__(self):
        self.module = ir.Module(name="SimpleLangModule")  
        self.symbol_table = {}
        self.symbol_print = {}
        self.function_counter = 0
        self.generated_funcs = []
        self.local_symbol_table = {}
        self.current_function = None
        self.struct_types = {}

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

        llvm_struct_type_name = f"struct.{struct_name}"  
        llvm_struct_type = self.module.context.get_identified_type(llvm_struct_type_name)
        llvm_struct_type.set_body(*field_llvm_types)

        self.struct_types[struct_name] = {
            'llvm_type': llvm_struct_type,
            'fields': field_info,
            'ordered_field_names': ordered_field_names
        }
        return None

    def visitInput_statement(self, ctx):
        var_name = ctx.ID().getText()
        var_ptr = None
        line_info = ctx.ID().getSymbol().line

        if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
            var_ptr = self.local_symbol_table[self.current_function][var_name]
        elif var_name in self.symbol_table:
            var_ptr = self.symbol_table[var_name]
        else:
            raise ValueError(f"Variable '{var_name}' is not declared for input (line {line_info}).")

        target_builder = None
        owning_func = None
        is_global_var_input = False

        if self.current_function:
            target_builder = ir.IRBuilder(
                self.builder_stack[-1].block if self.builder_stack else None)  
        else:
            is_global_var_input = True
            owning_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []),
                                      name=f"dummy_input_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(owning_func.name)
            block = owning_func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(block)

        if target_builder is None:
            raise Exception("No valid IRBuilder for input statement.")

        loaded_value_type = var_ptr.type.pointee

        fmt = ""
        if isinstance(loaded_value_type, ir.IntType) and loaded_value_type.width == 32:
            fmt = "%d"
        elif isinstance(loaded_value_type, ir.DoubleType):
            fmt = "%lf"
        else:
            raise ValueError(
                f"Unsupported type for input variable '{var_name}': {loaded_value_type} (line {line_info}). String input not directly supported by scanf like this.")

        fmt_var = self._create_global_format_str(fmt)
        fmt_ptr = target_builder.bitcast(fmt_var, ir.IntType(8).as_pointer())

        target_builder.call(self.input, [fmt_ptr, var_ptr])

        if is_global_var_input:
            target_builder.ret_void()

    def _create_global_format_str(self, fmt):
        if fmt in self.symbol_print:
            return self.symbol_print[fmt]

        fmt_bytes = bytearray(fmt.encode("utf8")) + b"\00"
        const_array_type = ir.ArrayType(ir.IntType(8), len(fmt_bytes))

        safe_name = fmt.replace("%", "pct_").replace(" ", "_").replace(".", "_dot_").replace('\n',
                                                                                             '_nl_')  
        name = f".fmt.{safe_name}.{len(self.symbol_print)}"  

        global_fmt = ir.GlobalVariable(self.module, const_array_type, name=name)
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = ir.Constant(const_array_type, fmt_bytes)

        self.symbol_print[fmt] = global_fmt
        return global_fmt

    def visitVariable_declaration(self, ctx: SimpleLangParser.Variable_declarationContext, builder=None):
        var_name = None
        type_str_from_keyword = None
        type_str_from_id = None
        llvm_type = None
        initializer = None
        line_number_info = ctx.start.line

        if hasattr(ctx, 'type_name') and ctx.type_name:
            type_name_node = ctx.type_name
            var_name_node = ctx.var_name
            type_str_from_id = type_name_node.text
            var_name = var_name_node.text
            line_number_info = type_name_node.line

            if var_name == "<missing ID>":
                raise AttributeError(f"Missing variable name for struct instance (line {var_name_node.line}).")
            if type_str_from_id == "<missing ID>":
                raise AttributeError(f"Missing type name for struct instance (line {type_name_node.line}).")

            if type_str_from_id not in self.struct_types:
                raise TypeError(f"Unknown struct type: '{type_str_from_id}' (line {type_name_node.line}).")

            llvm_type = self.struct_types[type_str_from_id]['llvm_type']
            initializer = ir.Constant(llvm_type, None) if not builder else None

        else:
            var_name_node = ctx.var_name
            if not var_name_node:
                raise AttributeError(
                    f"Variable name ID node not found in declaration context (line {line_number_info}).")
            var_name = var_name_node.text
            line_number_info = var_name_node.line

            if var_name == "<missing ID>":
                raise AttributeError(f"Missing variable name (line {var_name_node.line}).")

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
                        initializer = ir.Constant(llvm_type, 0)
                else:
                    initializer = ir.Constant(llvm_type, 0)
            elif type_str_from_keyword == 'string':
                llvm_type = ir.IntType(8).as_pointer()
                if ctx.STRING():
                    text_content = ctx.STRING().getText()[1:-1] + '\0'
                    str_bytes = bytearray(text_content.encode("utf8"))
                    str_arr_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
                    global_str_name = f".str.decl.{var_name}.{self.function_counter}"
                    self.function_counter += 1
                    global_str_literal = ir.GlobalVariable(self.module, str_arr_type, name=global_str_name)
                    global_str_literal.linkage = 'internal'
                    global_str_literal.global_constant = True
                    global_str_literal.initializer = ir.Constant(str_arr_type, str_bytes)
                    initializer = global_str_literal.bitcast(llvm_type)
                else:
                    initializer = ir.Constant(llvm_type, None)
            else:
                raise ValueError(
                    f"Unsupported type keyword '{type_str_from_keyword}' for variable: {var_name} (line {var_name_node.line}).")

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
            if type_str_from_id:
                pass
            elif initializer is not None:
                builder.store(initializer, ptr)
            else:
                raise ValueError(
                    f"Internal error: No initializer for local primitive '{var_name}' (line {line_number_info})")
            self.local_symbol_table[self.current_function][var_name] = ptr

    def visitTable_declaration(self, ctx, builder=None):
        type_node = ctx.type_()  
        element_type_str = type_node.getText()
        array_name = ctx.ID().getText()
        size = int(ctx.NUMBER().getText())
        line_info = ctx.ID().getSymbol().line

        llvm_element_type = self._get_llvm_type_from_str(element_type_str)
        if llvm_element_type is None:  
            raise ValueError(f"Unsupported array element type: {element_type_str} (line {line_info})")

        array_type = ir.ArrayType(llvm_element_type, size)

        if builder:
            if self.current_function is None:
                raise Exception(f"Local table declaration for '{array_name}' outside function (line {line_info}).")
            ptr = builder.alloca(array_type, name=array_name)
            self.local_symbol_table[self.current_function][array_name] = ptr
        else:
            if array_name in self.symbol_table:
                raise ValueError(f"Global table '{array_name}' already declared (line {line_info}).")
            global_array = ir.GlobalVariable(self.module, array_type, name=array_name)
            global_array.linkage = 'internal'
            global_array.initializer = ir.Constant(array_type, None)  
            self.symbol_table[array_name] = global_array

    def visitTable_assignment(self, ctx: SimpleLangParser.Table_assignmentContext, builder=None):
        var_name_token = ctx.ID()  
        var_name = var_name_token.getText()
        line_info = var_name_token.getSymbol().line

        table_ptr = None
        if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
            table_ptr = self.local_symbol_table[self.current_function][var_name]
        elif var_name in self.symbol_table:
            table_ptr = self.symbol_table[var_name]
        else:
            raise ValueError(f"Table '{var_name}' is not declared (line {line_info}).")

        if not isinstance(table_ptr.type.pointee, ir.ArrayType):
            raise TypeError(f"Variable '{var_name}' is not a table/array (line {line_info}).")

        llvm_element_type = table_ptr.type.pointee.element

        target_builder = builder
        end_fun = False
        if not target_builder:
            end_fun = True
            func_name = f"dummy_table_assign_func_{self.function_counter}"
            self.function_counter += 1
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            block = func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(block)
            self.generated_funcs.append(func_name)

        is_whole_array_assignment = False
        if ctx.getChildCount() >= 5 and \
                ctx.getChild(1).getText() == '=' and \
                ctx.getChild(2).getText() == '[':
            is_whole_array_assignment = True

        is_single_element_assignment = False
        if ctx.getChildCount() == 7 and \
                ctx.getChild(1).getText() == '[' and \
                ctx.getChild(3).getText() == ']' and \
                ctx.getChild(4).getText() == '=':
            is_single_element_assignment = True

        if is_whole_array_assignment:
            
            expr_list_ctx = ctx.expression()  
            if not isinstance(expr_list_ctx, list):  
                expr_list_ctx = [expr_list_ctx] if expr_list_ctx else []

            if len(expr_list_ctx) != table_ptr.type.pointee.count:
                raise ValueError(
                    f"Incorrect number of initializers for table '{var_name}'. Expected {table_ptr.type.pointee.count}, got {len(expr_list_ctx)} (line {line_info}).")

            for i, val_ctx in enumerate(expr_list_ctx):
                value = self.visitExpression(val_ctx, target_builder)
                if value.type != llvm_element_type:
                    
                    if isinstance(llvm_element_type, ir.DoubleType) and isinstance(value.type, ir.IntType):
                        value = target_builder.sitofp(value, ir.DoubleType())
                    else:
                        raise TypeError(
                            f"Type mismatch for element {i} in table '{var_name}'. Expected {llvm_element_type}, got {value.type} (line {val_ctx.start.line}).")
                idx_const = [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)]
                elem_ptr_val = target_builder.gep(table_ptr, idx_const, name=f"{var_name}_{i}_ptr")
                target_builder.store(value, elem_ptr_val)

        elif is_single_element_assignment:
            
            if not (isinstance(ctx.expression(), list) and len(ctx.expression()) == 2):
                
                
                raise AttributeError(f"Parser inconsistency for single element table assignment: {ctx.getText()}")

            index_val_ctx = ctx.expression(0)
            value_val_ctx = ctx.expression(1)

            index = self.visitExpression(index_val_ctx, target_builder)
            value = self.visitExpression(value_val_ctx, target_builder)

            if not isinstance(index.type, ir.IntType):
                raise TypeError(
                    f"Table index for '{var_name}' must be an integer, got {index.type} (line {index_val_ctx.start.line}).")

            
            if value.type != llvm_element_type:
                if isinstance(llvm_element_type, ir.DoubleType) and isinstance(value.type, ir.IntType):
                    value = target_builder.sitofp(value, ir.DoubleType())
                elif isinstance(llvm_element_type, ir.IntType) and isinstance(value.type,
                                                                              ir.DoubleType) and llvm_element_type.width == 32:
                    value = target_builder.fptosi(value, llvm_element_type)
                else:
                    raise TypeError(
                        f"Type mismatch for element assignment to table '{var_name}'. Expected {llvm_element_type}, got {value.type} (line {value_val_ctx.start.line}).")

            idx_llvm_val = [ir.Constant(ir.IntType(32), 0), index]  
            elem_ptr_val = target_builder.gep(table_ptr, idx_llvm_val, name=f"{var_name}_elem_ptr")
            target_builder.store(value, elem_ptr_val)
        else:
            
            print(f"DEBUG Table Assignment Fallthrough: ctx.getText() = {ctx.getText()}")
            print(f"DEBUG Table Assignment: Child count = {ctx.getChildCount()}")
            for i_child in range(ctx.getChildCount()):
                child_debug = ctx.getChild(i_child)
                print(
                    f"DEBUG Table Assignment: Child {i_child} type: {type(child_debug)}, text: '{child_debug.getText()}'")
            if hasattr(ctx, 'expression') and callable(ctx.expression):
                expressions_found = ctx.expression()
                if isinstance(expressions_found, list):
                    print(f"DEBUG Table Assignment: Number of expressions found: {len(expressions_found)}")
                    for i_expr, expr_debug_ctx in enumerate(expressions_found):
                        print(f"DEBUG Table Assignment: Expr {i_expr} text: {expr_debug_ctx.getText()}")
                elif expressions_found is not None:
                    print(f"DEBUG Table Assignment: ctx.expression() is single: {expressions_found.getText()}")
                else:
                    print(f"DEBUG Table Assignment: ctx.expression() is None")

            raise SyntaxError(
                f"Malformed table assignment for '{var_name}' (line {line_info}). Code: '{ctx.getText()}'")

        if end_fun:
            target_builder.ret_void()

    def visitMatrix_declaration(self, ctx: SimpleLangParser.Matrix_declarationContext, builder=None):
        matrix_name = ctx.ID().getText()
        element_type_str = ctx.type_().getText()
        rows = int(ctx.NUMBER(0).getText())
        cols = int(ctx.NUMBER(1).getText())
        line_info = ctx.ID().getSymbol().line

        llvm_element_type = self._get_llvm_type_from_str(element_type_str)
        if llvm_element_type is None:
            raise ValueError(f"Unsupported matrix element type: {element_type_str} (line {line_info}).")

        if rows <= 0 or cols <= 0:
            raise ValueError(f"Matrix dimensions for '{matrix_name}' must be positive (line {line_info}).")

        matrix_type = ir.ArrayType(ir.ArrayType(llvm_element_type, cols), rows)
        is_local = builder is not None and self.current_function is not None
        target_symbol_map = self.local_symbol_table.get(self.current_function, {}) if is_local else self.symbol_table

        if matrix_name in target_symbol_map:
            raise ValueError(f"Variable '{matrix_name}' already declared in this scope (line {line_info}).")

        matrix_llvm_val_ptr = None
        if is_local:
            matrix_llvm_val_ptr = builder.alloca(matrix_type, name=matrix_name)
            if self.current_function not in self.local_symbol_table: self.local_symbol_table[self.current_function] = {}
            self.local_symbol_table[self.current_function][matrix_name] = matrix_llvm_val_ptr
        else:
            global_matrix = ir.GlobalVariable(self.module, matrix_type, name=matrix_name)
            global_matrix.linkage = 'internal'
            global_matrix.initializer = ir.Constant(matrix_type, None)  
            self.symbol_table[matrix_name] = global_matrix
            matrix_llvm_val_ptr = global_matrix

        if ctx.matrix_initializer():
            init_ctx = ctx.matrix_initializer()
            row_inits_ctx = init_ctx.row_initializer()
            if len(row_inits_ctx) != rows:
                raise ValueError(
                    f"Initializer for matrix '{matrix_name}' has {len(row_inits_ctx)} rows, expected {rows} (line {init_ctx.start.line}).")

            matrix_rows_constants_for_global = []

            for r_idx, row_init_ctx_val in enumerate(row_inits_ctx):
                col_exprs_ctx = row_init_ctx_val.expression()
                if len(col_exprs_ctx) != cols:
                    raise ValueError(
                        f"Initializer for matrix '{matrix_name}' row {r_idx} has {len(col_exprs_ctx)} columns, expected {cols} (line {row_init_ctx_val.start.line}).")

                matrix_cols_constants_for_global_row = []
                for c_idx, expr_ctx_val in enumerate(col_exprs_ctx):
                    val = self.visitExpression(expr_ctx_val,
                                               builder if is_local else None)  

                    if not is_local and not isinstance(val, ir.Constant):
                        raise ValueError(
                            f"Global matrix '{matrix_name}' initializer element [{r_idx}][{c_idx}] must be constant (line {expr_ctx_val.start.line}).")

                    if val.type != llvm_element_type:
                        if isinstance(llvm_element_type, ir.DoubleType) and isinstance(val.type, ir.IntType):
                            if isinstance(val, ir.Constant):
                                val = ir.Constant(ir.DoubleType(), float(val.constant))
                            elif is_local:
                                val = builder.sitofp(val, ir.DoubleType())
                            else:
                                raise TypeError("Cannot convert non-constant int to float for global matrix init.")
                        else:
                            raise TypeError(
                                f"Type mismatch for matrix '{matrix_name}' element [{r_idx}][{c_idx}]. Expected {llvm_element_type}, got {val.type} (line {expr_ctx_val.start.line}).")

                    if is_local:
                        zero_const = ir.Constant(ir.IntType(32), 0)
                        row_idx_const = ir.Constant(ir.IntType(32), r_idx)
                        col_idx_const = ir.Constant(ir.IntType(32), c_idx)
                        elem_ptr = builder.gep(matrix_llvm_val_ptr, [zero_const, row_idx_const, col_idx_const],
                                               name=f"{matrix_name}_{r_idx}_{c_idx}_ptr")
                        builder.store(val, elem_ptr)
                    else:
                        matrix_cols_constants_for_global_row.append(val)

                if not is_local:
                    row_const_val = ir.Constant(ir.ArrayType(llvm_element_type, cols),
                                                matrix_cols_constants_for_global_row)
                    matrix_rows_constants_for_global.append(row_const_val)

            if not is_local:
                matrix_llvm_val_ptr.initializer = ir.Constant(matrix_type, matrix_rows_constants_for_global)

    def visitMatrix_assignment(self, ctx: SimpleLangParser.Matrix_assignmentContext, builder=None):
        matrix_name = ctx.ID().getText()
        line_info = ctx.ID().getSymbol().line
        var_ptr = None
        is_local = False

        if self.current_function and matrix_name in self.local_symbol_table.get(self.current_function, {}):
            var_ptr = self.local_symbol_table[self.current_function][matrix_name]
            is_local = True
        elif matrix_name in self.symbol_table:
            var_ptr = self.symbol_table[matrix_name]
        else:
            raise ValueError(f"Matrix '{matrix_name}' is not declared (line {line_info}).")

        if not isinstance(var_ptr.type.pointee, ir.ArrayType) or \
                not isinstance(var_ptr.type.pointee.element, ir.ArrayType):
            raise TypeError(f"Variable '{matrix_name}' is not a matrix (line {line_info}).")

        matrix_llvm_type = var_ptr.type.pointee
        row_llvm_type = matrix_llvm_type.element
        llvm_element_type = row_llvm_type.element
        rows = matrix_llvm_type.count
        cols = row_llvm_type.count

        target_builder = builder
        end_fun = False
        if not is_local and not target_builder:
            end_fun = True
            func_name = f"dummy_massign_func_{self.function_counter}"
            self.function_counter += 1
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            block = func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(block)
            self.generated_funcs.append(func_name)

        if target_builder is None:
            raise Exception(f"No builder for matrix assignment '{matrix_name}' (line {line_info}).")

        init_ctx = ctx.matrix_initializer()
        row_inits_ctx = init_ctx.row_initializer()
        if len(row_inits_ctx) != rows:
            raise ValueError(
                f"Initializer for matrix '{matrix_name}' assignment has {len(row_inits_ctx)} rows, expected {rows} (line {init_ctx.start.line}).")

        zero_const = ir.Constant(ir.IntType(32), 0)
        for r_idx, row_init_ctx_val in enumerate(row_inits_ctx):
            col_exprs_ctx = row_init_ctx_val.expression()
            if len(col_exprs_ctx) != cols:
                raise ValueError(
                    f"Initializer for matrix '{matrix_name}' assignment row {r_idx} has {len(col_exprs_ctx)} columns, expected {cols} (line {row_init_ctx_val.start.line}).")

            row_idx_const = ir.Constant(ir.IntType(32), r_idx)
            for c_idx, expr_ctx_val in enumerate(col_exprs_ctx):
                value = self.visitExpression(expr_ctx_val, target_builder)
                if value.type != llvm_element_type:
                    if isinstance(llvm_element_type, ir.DoubleType) and isinstance(value.type,
                                                                                   ir.IntType) and value.type.width == 32:
                        value = target_builder.sitofp(value, ir.DoubleType())
                    elif isinstance(llvm_element_type, ir.IntType) and llvm_element_type.width == 32 and isinstance(
                            value.type, ir.DoubleType):
                        value = target_builder.fptosi(value, ir.IntType(32))
                    else:
                        raise TypeError(
                            f"Type mismatch in matrix '{matrix_name}' assignment initializer [{r_idx}][{c_idx}]. Expected {llvm_element_type}, got {value.type} (line {expr_ctx_val.start.line}).")

                col_idx_const = ir.Constant(ir.IntType(32), c_idx)
                elem_ptr = target_builder.gep(var_ptr, [zero_const, row_idx_const, col_idx_const],
                                              name=f"{matrix_name}_{r_idx}_{c_idx}_ptr")
                target_builder.store(value, elem_ptr)
        if end_fun:
            target_builder.ret_void()

    def visitMatrix_element_assignment(self, ctx: SimpleLangParser.Matrix_element_assignmentContext, builder=None):
        matrix_name = ctx.ID().getText()
        line_info = ctx.ID().getSymbol().line
        var_ptr = None
        is_local = False

        if self.current_function and matrix_name in self.local_symbol_table.get(self.current_function, {}):
            var_ptr = self.local_symbol_table[self.current_function][matrix_name]
            is_local = True
        elif matrix_name in self.symbol_table:
            var_ptr = self.symbol_table[matrix_name]
        else:
            raise ValueError(f"Matrix '{matrix_name}' is not declared (line {line_info}).")

        if not isinstance(var_ptr.type.pointee, ir.ArrayType) or \
                not isinstance(var_ptr.type.pointee.element, ir.ArrayType):
            raise TypeError(f"Variable '{matrix_name}' is not a matrix (line {line_info}).")
        llvm_element_type = var_ptr.type.pointee.element.element

        target_builder = builder
        end_fun = False
        if not is_local and not target_builder:
            end_fun = True
            func_name = f"dummy_melem_assign_func_{self.function_counter}"
            self.function_counter += 1
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            block = func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(block)
            self.generated_funcs.append(func_name)

        if target_builder is None:
            raise Exception(f"No builder for matrix element assignment '{matrix_name}' (line {line_info}).")

        row_index_val = self.visitExpression(ctx.expression(0), target_builder)
        col_index_val = self.visitExpression(ctx.expression(1), target_builder)
        value_val = self.visitExpression(ctx.expression(2), target_builder)

        if not isinstance(row_index_val.type, ir.IntType):
            raise TypeError(
                f"Matrix row index for '{matrix_name}' must be an integer, got {row_index_val.type} (line {ctx.expression(0).start.line}).")
        if row_index_val.type.width != 32:
            row_index_val = target_builder.sext(row_index_val, ir.IntType(32))

        if not isinstance(col_index_val.type, ir.IntType):
            raise TypeError(
                f"Matrix column index for '{matrix_name}' must be an integer, got {col_index_val.type} (line {ctx.expression(1).start.line}).")
        if col_index_val.type.width != 32:
            col_index_val = target_builder.sext(col_index_val, ir.IntType(32))

        if value_val.type != llvm_element_type:
            if isinstance(llvm_element_type, ir.DoubleType) and isinstance(value_val.type,
                                                                           ir.IntType) and value_val.type.width == 32:
                value_val = target_builder.sitofp(value_val, ir.DoubleType())
            elif isinstance(llvm_element_type, ir.IntType) and llvm_element_type.width == 32 and isinstance(
                    value_val.type, ir.DoubleType):
                value_val = target_builder.fptosi(value_val, ir.IntType(32))
            else:
                raise TypeError(
                    f"Type mismatch in matrix element assignment to '{matrix_name}'. Expected {llvm_element_type}, got {value_val.type} (line {ctx.expression(2).start.line}).")

        zero_const = ir.Constant(ir.IntType(32), 0)
        elem_ptr = target_builder.gep(var_ptr, [zero_const, row_index_val, col_index_val],
                                      name=f"{matrix_name}_elem_ptr")
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

            if not isinstance(struct_ptr.type.pointee, (
            ir.LiteralStructType, ir.IdentifiedStructType)):  
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
                                                                                     ir.DoubleType) and expected_field_llvm_type.width == 32:
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
            func_name = f"dummy_print_func_{self.function_counter}"
            self.function_counter += 1
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            self.generated_funcs.append(func_name)

        value_to_print = None
        fmt_str = None
        item_to_print_ctx = ctx.getChild(2)

        if isinstance(item_to_print_ctx, TerminalNode) and item_to_print_ctx.symbol.type == SimpleLangLexer.STRING:
            text = item_to_print_ctx.getText()[1:-1] + '\0'
            str_bytes = bytearray(text.encode("utf8"))
            str_type = ir.ArrayType(ir.IntType(8), len(str_bytes))
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

        elif isinstance(item_to_print_ctx, TerminalNode) and item_to_print_ctx.symbol.type == SimpleLangLexer.ID:
            var_name = item_to_print_ctx.getText()
            var_ptr = None
            line_info_print_id = item_to_print_ctx.symbol.line
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                var_ptr = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                var_ptr = self.symbol_table[var_name]
            else:
                raise NameError(f"Variable '{var_name}' not found in print statement (line {line_info_print_id}).")

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
                    array_fmt_char = "%d "
                else:
                    raise ValueError(
                        f"Unsupported array element type for printing: {elem_type} (line {line_info_print_id}).")

                fmt_var_array = self._create_global_format_str(array_fmt_char)
                fmt_ptr_array = builder.bitcast(fmt_var_array, ir.IntType(8).as_pointer())
                for i in range(length):
                    elem_addr = builder.gep(var_ptr, [ir.Constant(ir.IntType(32), 0), ir.Constant(ir.IntType(32), i)])
                    val_loaded = builder.load(elem_addr)
                    if isinstance(val_loaded.type, ir.IntType) and val_loaded.type.width == 1:
                        val_loaded = builder.zext(val_loaded, ir.IntType(32))
                    builder.call(self.printf, [fmt_ptr_array, val_loaded])

                newline_fmt_var = self._create_global_format_str("\n")
                newline_fmt_ptr = builder.bitcast(newline_fmt_var, ir.IntType(8).as_pointer())
                builder.call(self.printf, [newline_fmt_ptr])

                if end_fun: builder.ret_void()
                return

            value_to_print = builder.load(var_ptr, name=var_name + "_val")
        else:
            raise ValueError(
                f"Unsupported item type in print statement: {type(item_to_print_ctx)} (line {ctx.start.line})")

        if fmt_str is None:
            if value_to_print is None:
                raise ValueError("Internal error: value_to_print is None in print_statement.")
            val_type = value_to_print.type
            if isinstance(val_type, ir.IntType) and val_type.width == 32:
                fmt_str = "%d\n"
            elif isinstance(val_type, ir.DoubleType):
                fmt_str = "%f\n"
            elif isinstance(val_type, ir.IntType) and val_type.width == 1:
                fmt_str = "%d\n"
                value_to_print = builder.zext(value_to_print, ir.IntType(32))
            elif isinstance(val_type, ir.PointerType) and \
                    isinstance(val_type.pointee, ir.IntType) and \
                    val_type.pointee.width == 8:
                fmt_str = "%s\n"
            else:
                raise ValueError(f"Unsupported type for print: {value_to_print.type} (line {ctx.start.line})")

        fmt_var_final = self._create_global_format_str(fmt_str)
        fmt_ptr_final = builder.bitcast(fmt_var_final, ir.IntType(8).as_pointer())
        builder.call(self.printf, [fmt_ptr_final, value_to_print])

        if end_fun:
            builder.ret_void()

    def visitFunc_call(self, ctx: SimpleLangParser.Func_callContext, builder: ir.IRBuilder):
        func_name_token = ctx.ID()
        func_name = func_name_token.getText()
        line_info = func_name_token.getSymbol().line

        llvm_func = self.module.globals.get(func_name)

        if llvm_func is None:
            raise NameError(f"Function '{func_name}' is not defined (line {line_info}).")
        if not isinstance(llvm_func, ir.Function):
            raise TypeError(f"'{func_name}' is not a function (line {line_info}). It's a {type(llvm_func)}.")

        llvm_args_values = []
        if ctx.argument_list():
            arg_list_ctx = ctx.argument_list()
            for child_node in arg_list_ctx.getChildren():
                if isinstance(child_node, SimpleLangParser.ExpressionContext):
                    arg_val = self.visitExpression(child_node, builder)
                    llvm_args_values.append(arg_val)
                elif isinstance(child_node, SimpleLangParser.Boolean_expressionContext):
                    arg_val = self.visitBooleanExpression(child_node, builder)
                    llvm_args_values.append(arg_val)

        if len(llvm_func.args) != len(llvm_args_values):
            raise TypeError(
                f"Function '{func_name}' called with an incorrect number of arguments. "
                f"Expected {len(llvm_func.args)}, but got {len(llvm_args_values)} (line {line_info})."
            )

        processed_llvm_args = []
        for i, (expected_llvm_type, actual_arg_value) in enumerate(zip(llvm_func.function_type.args, llvm_args_values)):
            arg_source_text = "unknown_arg_source"
            arg_line = line_info  
            if ctx.argument_list():
                arg_nodes_for_err = [child for child in ctx.argument_list().getChildren() if
                                     not (isinstance(child, TerminalNode) and child.getText() == ',')]
                if i < len(arg_nodes_for_err):
                    arg_source_text = arg_nodes_for_err[i].getText()
                    arg_line = arg_nodes_for_err[i].start.line

            if actual_arg_value.type == expected_llvm_type:
                processed_llvm_args.append(actual_arg_value)
            elif isinstance(expected_llvm_type, ir.DoubleType) and isinstance(actual_arg_value.type, ir.IntType):
                converted_arg = builder.sitofp(actual_arg_value, ir.DoubleType(), name=f"arg{i}_conv_f")
                processed_llvm_args.append(converted_arg)
            elif isinstance(expected_llvm_type, ir.IntType) and expected_llvm_type.width == 32 and \
                    isinstance(actual_arg_value.type, ir.DoubleType):
                converted_arg = builder.fptosi(actual_arg_value, expected_llvm_type, name=f"arg{i}_conv_i")
                processed_llvm_args.append(converted_arg)
            elif isinstance(expected_llvm_type, ir.IntType) and expected_llvm_type.width == 32 and \
                    isinstance(actual_arg_value.type, ir.IntType) and actual_arg_value.type.width == 1:
                converted_arg = builder.zext(actual_arg_value, expected_llvm_type, name=f"arg{i}_bool_to_int")
                processed_llvm_args.append(converted_arg)
            else:
                raise TypeError(
                    f"Type mismatch for argument {i + 1} ('{arg_source_text}') of function '{func_name}'. "
                    f"Expected {expected_llvm_type}, but got {actual_arg_value.type} (line {arg_line})."
                )

        call_result_name = func_name + "_res" if llvm_func.function_type.return_type != ir.VoidType() else ""

        if isinstance(llvm_func.function_type.return_type, ir.VoidType):
            builder.call(llvm_func, processed_llvm_args)
            raise TypeError(
                f"Function '{func_name}' returns void and cannot be used in an expression (line {line_info}).")
        else:
            return builder.call(llvm_func, processed_llvm_args, name=call_result_name)

    def visitExpression(self, ctx: SimpleLangParser.ExpressionContext, builder: ir.IRBuilder):
        if ctx is None:
            raise ValueError("visitExpression called with ctx=None")

        if isinstance(ctx, SimpleLangParser.StringExprContext):
            string_node = ctx.STRING()
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
            left_expr_ctx = ctx.expression(0)
            right_expr_ctx = ctx.expression(1)
            left = self.visitExpression(left_expr_ctx, builder)
            right = self.visitExpression(right_expr_ctx, builder)
            op_text = ctx.op.text
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
            return self.visitExpression(ctx.expression(), builder)
        elif isinstance(ctx, SimpleLangParser.StructMemberAccessExprContext):
            struct_instance_expr_ctx = ctx.expression()
            field_name = ctx.ID().getText()
            line_info = ctx.ID().getSymbol().line
            struct_ptr = None
            struct_type_name_for_access = None

            def get_var_ptr_for_struct_access(expr_ctx_local):
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
                elif isinstance(expr_ctx_local, SimpleLangParser.StructMemberAccessExprContext):
                    raise NotImplementedError(
                        f"Chained struct member access like 'a.b.c' needs GEPs from intermediate field pointers.")
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
            field_llvm_ptr = builder.gep(struct_ptr, [zero, ir.Constant(ir.IntType(32), field_idx)],
                                         name=f"{field_name}_ptr")
            return builder.load(field_llvm_ptr, name=field_name)
        elif isinstance(ctx, SimpleLangParser.TableElemExprContext):
            var_name = ctx.ID().getText()
            index_expr_ctx = ctx.expression()
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
            var_name = ctx.ID().getText()
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
            func_call_node = ctx.func_call()
            return self.visitFunc_call(func_call_node, builder)
        error_line = ctx.start.line if hasattr(ctx, 'start') else 'unknown'
        raise NotImplementedError(
            f"visitExpression: Unhandled expression form: '{ctx.getText()}' (type: {type(ctx)}) at line {error_line}")

    def visitBooleanExpression(self, ctx: SimpleLangParser.Boolean_expressionContext, builder: ir.IRBuilder):
        if ctx is None:
            raise ValueError("visitBooleanExpression called with ctx=None")

        if isinstance(ctx, SimpleLangParser.BoolValueContext):
            text = ctx.BOOLEAN().getText()
            if text == "true":
                return ir.Constant(ir.IntType(1), 1)
            else:
                return ir.Constant(ir.IntType(1), 0)
        elif isinstance(ctx, SimpleLangParser.BoolVariableContext):
            var_name = ctx.ID().getText()
            ptr = None
            line_info = ctx.ID().getSymbol().line
            if self.current_function and var_name in self.local_symbol_table.get(self.current_function, {}):
                ptr = self.local_symbol_table[self.current_function][var_name]
            elif var_name in self.symbol_table:
                ptr = self.symbol_table[var_name]
            else:
                raise NameError(f"Boolean variable '{var_name}' not found (line {line_info}).")
            loaded_val = builder.load(ptr, name=var_name)
            if not (isinstance(loaded_val.type, ir.IntType) and loaded_val.type.width == 1):
                raise TypeError(f"Variable '{var_name}' is not a boolean (line {line_info}).")
            return loaded_val
        elif isinstance(ctx, SimpleLangParser.BoolCompareExprContext):
            return self.visitComparizon_expression(ctx.comparizon_expression(), builder)
        elif isinstance(ctx, SimpleLangParser.BoolBinaryOpContext):
            left = self.visitBooleanExpression(ctx.boolean_expression(0), builder)
            right = self.visitBooleanExpression(ctx.boolean_expression(1), builder)
            op = ctx.op.text
            if op == "AND":
                return builder.and_(left, right, name="andtmp")
            elif op == "OR":
                return builder.or_(left, right, name="ortmp")
            elif op == "XOR":
                return builder.xor(left, right, name="xortmp")
            else:
                raise ValueError(f"Unknown boolean binary operator: {op} (line {ctx.op.line})")
        elif isinstance(ctx, SimpleLangParser.BoolNegationContext):
            operand = self.visitBooleanExpression(ctx.boolean_expression(), builder)
            return builder.not_(operand, name="nottmp")  
        elif isinstance(ctx, SimpleLangParser.BoolParensContext):
            return self.visitBooleanExpression(ctx.boolean_expression(), builder)
        elif isinstance(ctx, SimpleLangParser.FuncCallBoolContext):
            func_call_node = ctx.func_call()
            call_result_value = self.visitFunc_call(func_call_node, builder)
            expected_return_type = ir.IntType(1)
            if call_result_value.type == expected_return_type:
                return call_result_value
            elif isinstance(call_result_value.type, ir.IntType) and call_result_value.type.width == 32:
                zero_i32 = ir.Constant(ir.IntType(32), 0)
                return builder.icmp_signed('!=', call_result_value, zero_i32, name="i32_to_bool")
            else:
                func_name_for_error = func_call_node.ID().getText()
                line_for_error = func_call_node.ID().getSymbol().line
                raise TypeError(
                    f"Function '{func_name_for_error}' used in a boolean context does not return a boolean (i1) or convertible i32. "
                    f"Got {call_result_value.type} (line {line_for_error})."
                )
        error_line = ctx.start.line if hasattr(ctx, 'start') else 'unknown'
        raise NotImplementedError(
            f"visitBooleanExpression: Unhandled form: '{ctx.getText()}' (type: {type(ctx)}) at line {error_line}")

    def visitComparizon_expression(self, ctx: SimpleLangParser.Comparizon_expressionContext, builder: ir.IRBuilder):
        left_expr_ctx = ctx.expression(0)
        right_expr_ctx = ctx.expression(1)
        op = ctx.op.text
        line_info = ctx.op.line

        left = self.visitExpression(left_expr_ctx, builder)
        right = self.visitExpression(right_expr_ctx, builder)

        
        if isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.IntType):
            right = builder.sitofp(right, ir.DoubleType(), name="cmp_r_to_f")
        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.DoubleType):
            left = builder.sitofp(left, ir.DoubleType(), name="cmp_l_to_f")

        if left.type != right.type:  
            raise TypeError(
                f"Type mismatch in comparison '{op}': {left.type} vs {right.type} (line {line_info}). String comparison not directly supported with these operators.")

        if isinstance(left.type, ir.IntType) and left.type.width == 32:
            return builder.icmp_signed(op, left, right, name="icmp_val")
        elif isinstance(left.type, ir.DoubleType):
            return builder.fcmp_ordered(op, left, right, name="fcmp_val")
        
        
        else:
            raise TypeError(f"Unsupported type for comparison '{op}': {left.type} (line {line_info}).")

    def visitIf_statement(self, ctx: SimpleLangParser.If_statementContext, builder=None):
        target_builder = builder
        is_dummy_func = False
        if not target_builder:
            is_dummy_func = True
            func_name = f"dummy_if_func_{self.function_counter}";
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            entry_block = dummy_func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(entry_block)
            self.generated_funcs.append(dummy_func.name)

        condition = self.visitBooleanExpression(ctx.boolean_expression(), target_builder)

        if_then_block = target_builder.append_basic_block('if_then')

        if ctx.getChildCount() > 3 and ctx.getChild(
                3).getText() == 'else':  
            if_else_block = target_builder.append_basic_block('if_else')
            if_merge_block = target_builder.append_basic_block('if_merge')
            target_builder.cbranch(condition, if_then_block, if_else_block)

            target_builder.position_at_end(if_then_block)
            self.visitCode_block(ctx.code_block(0), target_builder)
            if not target_builder.block.is_terminated: target_builder.branch(if_merge_block)

            target_builder.position_at_end(if_else_block)
            self.visitCode_block(ctx.code_block(1), target_builder)  
            if not target_builder.block.is_terminated: target_builder.branch(if_merge_block)

            target_builder.position_at_end(if_merge_block)
        else:  
            if_merge_block = target_builder.append_basic_block('if_merge')
            target_builder.cbranch(condition, if_then_block, if_merge_block)

            target_builder.position_at_end(if_then_block)
            self.visitCode_block(ctx.code_block(0), target_builder)  
            if not target_builder.block.is_terminated: target_builder.branch(if_merge_block)

            target_builder.position_at_end(if_merge_block)  

        if is_dummy_func:
            target_builder.ret_void()

    def visitLoop_while(self, ctx: SimpleLangParser.Loop_whileContext, builder=None):
        target_builder = builder
        is_dummy_func = False
        if not target_builder:
            is_dummy_func = True
            func_name = f"dummy_while_func_{self.function_counter}";
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            entry_block = dummy_func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(entry_block)
            self.generated_funcs.append(dummy_func.name)

        loop_header_block = target_builder.append_basic_block('loop_header')
        loop_body_block = target_builder.append_basic_block('loop_body')
        loop_exit_block = target_builder.append_basic_block('loop_exit')

        if not target_builder.block.is_terminated:  
            target_builder.branch(loop_header_block)

        target_builder.position_at_end(loop_header_block)
        condition = self.visitBooleanExpression(ctx.boolean_expression(), target_builder)
        target_builder.cbranch(condition, loop_body_block, loop_exit_block)

        target_builder.position_at_end(loop_body_block)
        self.visitCode_block(ctx.code_block(), target_builder)
        if not target_builder.block.is_terminated: target_builder.branch(loop_header_block)

        target_builder.position_at_end(loop_exit_block)
        if is_dummy_func:
            target_builder.ret_void()

    def visitLoop_for_iterator(self, ctx: SimpleLangParser.Loop_for_iteratorContext, builder=None):
        target_builder = builder
        is_dummy_func = False
        if not target_builder:
            is_dummy_func = True
            func_name = f"dummy_for_func_{self.function_counter}";
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=func_name)
            entry_block = dummy_func.append_basic_block(name="entry")
            target_builder = ir.IRBuilder(entry_block)
            self.generated_funcs.append(dummy_func.name)

        index_var_name = ctx.ID(0).getText()
        element_var_name = ctx.ID(1).getText()
        iterable_name = ctx.ID(2).getText()
        line_info = ctx.ID(0).getSymbol().line

        iterable_ptr = None
        if self.current_function and iterable_name in self.local_symbol_table.get(self.current_function, {}):
            iterable_ptr = self.local_symbol_table[self.current_function][iterable_name]
        elif iterable_name in self.symbol_table:
            iterable_ptr = self.symbol_table[iterable_name]
        else:
            raise NameError(f"Iterable '{iterable_name}' not declared for for-loop (line {line_info}).")

        if not isinstance(iterable_ptr.type.pointee, ir.ArrayType):
            raise TypeError(f"'{iterable_name}' is not an array/table, cannot iterate (line {line_info}).")

        array_llvm_type = iterable_ptr.type.pointee
        element_llvm_type = array_llvm_type.element
        array_len = array_llvm_type.count

        
        original_index_var_exists = False
        original_element_var_exists = False
        prev_index_val = None
        prev_element_val = None

        current_scope = self.local_symbol_table.get(self.current_function, self.symbol_table)

        if index_var_name in current_scope: original_index_var_exists = True; prev_index_val = current_scope[
            index_var_name]
        if element_var_name in current_scope: original_element_var_exists = True; prev_element_val = current_scope[
            element_var_name]

        index_ptr = target_builder.alloca(ir.IntType(32), name=index_var_name)
        target_builder.store(ir.Constant(ir.IntType(32), 0), index_ptr)
        element_ptr = target_builder.alloca(element_llvm_type, name=element_var_name)

        current_scope[index_var_name] = index_ptr
        current_scope[element_var_name] = element_ptr

        loop_header = target_builder.append_basic_block('for_header')
        loop_body = target_builder.append_basic_block('for_body')
        loop_exit = target_builder.append_basic_block('for_exit')

        if not target_builder.block.is_terminated: target_builder.branch(loop_header)

        target_builder.position_at_end(loop_header)
        current_idx_val = target_builder.load(index_ptr, name="current_idx")
        len_const = ir.Constant(ir.IntType(32), array_len)
        condition = target_builder.icmp_signed('<', current_idx_val, len_const, name="for_cond")
        target_builder.cbranch(condition, loop_body, loop_exit)

        target_builder.position_at_end(loop_body)
        actual_element_ptr = target_builder.gep(iterable_ptr, [ir.Constant(ir.IntType(32), 0), current_idx_val],
                                                name="actual_elem_ptr")
        actual_element_val = target_builder.load(actual_element_ptr, name="actual_elem_val")
        target_builder.store(actual_element_val, element_ptr)

        self.visitCode_block(ctx.code_block(), target_builder)

        if not target_builder.block.is_terminated:
            new_idx_val = target_builder.add(current_idx_val, ir.Constant(ir.IntType(32), 1), name="new_idx")
            target_builder.store(new_idx_val, index_ptr)
            target_builder.branch(loop_header)

        target_builder.position_at_end(loop_exit)

        if original_index_var_exists:
            current_scope[index_var_name] = prev_index_val
        else:
            del current_scope[index_var_name]
        if original_element_var_exists:
            current_scope[element_var_name] = prev_element_val
        else:
            del current_scope[element_var_name]

        if is_dummy_func:
            target_builder.ret_void()

    def visitFunction_definition(self, ctx: SimpleLangParser.Function_definitionContext):
        return_type_ctx = ctx.type_()
        func_name_token = ctx.ID()
        func_name = func_name_token.getText()
        line_info = func_name_token.getSymbol().line

        if func_name in self.module.globals:
            
            existing_global = self.module.globals[func_name]
            if isinstance(existing_global, ir.Function):
                raise NameError(f"Function '{func_name}' already defined (line {line_info}).")
            else:
                raise NameError(
                    f"Name '{func_name}' already defined as a global variable (line {line_info}). Cannot define function with same name.")

        self.current_function = func_name
        if func_name not in self.local_symbol_table:
            self.local_symbol_table[func_name] = {}

        param_llvm_types = []
        param_names_and_types = []
        if ctx.parametr_list():
            param_list_ctx = ctx.parametr_list()
            i = 0
            
            param_children_list = list(param_list_ctx.getChildren())  

            while i < len(param_children_list):  
                child_node = param_children_list[i]  
                if isinstance(child_node, SimpleLangParser.TypeContext):
                    param_type_str = child_node.getText()
                    
                    if i + 1 < len(param_children_list) and \
                            isinstance(param_children_list[i + 1], TerminalNode) and \
                            param_children_list[i + 1].symbol.type == SimpleLangLexer.ID:

                        param_name_str = param_children_list[i + 1].getText()
                        llvm_param_type = self._get_llvm_type_from_str(param_type_str)

                        if llvm_param_type is None:  
                            raise TypeError(
                                f"Unknown parameter type '{param_type_str}' for parameter '{param_name_str}' in function '{func_name}' (line {child_node.start.line}).")

                        param_llvm_types.append(llvm_param_type)
                        param_names_and_types.append((param_name_str, llvm_param_type))
                        i += 2  
                    else:
                        err_line = child_node.start.line if hasattr(child_node, 'start') else line_info
                        raise SyntaxError(
                            f"Expected parameter name (ID) after type '{param_type_str}' in function '{func_name}' (around line {err_line}).")
                elif isinstance(child_node, TerminalNode) and child_node.getText() == ',':
                    i += 1  
                else:
                    err_line = child_node.start.line if hasattr(child_node, 'start') else line_info
                    raise SyntaxError(
                        f"Unexpected token '{child_node.getText()}' in parameter list for '{func_name}' (around line {err_line}).")

        return_llvm_type_str = return_type_ctx.getText()
        return_llvm_type = self._get_llvm_type_from_str(return_llvm_type_str)
        if return_llvm_type is None:  
            raise TypeError(
                f"Unknown return type '{return_llvm_type_str}' for function '{func_name}' (line {return_type_ctx.start.line}).")

        func_llvm_type = ir.FunctionType(return_llvm_type, param_llvm_types)
        func_llvm = ir.Function(self.module, func_llvm_type, name=func_name)

        entry_block = func_llvm.append_basic_block(name="entry")
        builder = ir.IRBuilder(entry_block)
        for i_arg, (name, typ) in enumerate(param_names_and_types):  
            if name in self.local_symbol_table[func_name]:
                
                
                raise ValueError(
                    f"Parameter name '{name}' is duplicated or shadows another variable in function '{func_name}' (line {line_info}).")  

            func_llvm.args[i_arg].name = name
            param_ptr = builder.alloca(typ, name=name + ".addr")
            builder.store(func_llvm.args[i_arg], param_ptr)
            self.local_symbol_table[func_name][name] = param_ptr

        self.visitCode_block(ctx.code_block(), builder)

        if not builder.block.is_terminated:  
            if isinstance(return_llvm_type, ir.VoidType):  
                builder.ret_void()
            elif return_llvm_type == ir.IntType(32):
                builder.ret(ir.Constant(ir.IntType(32), 0))
            elif return_llvm_type == ir.DoubleType():
                builder.ret(ir.Constant(ir.DoubleType(), 0.0))
            elif return_llvm_type == ir.IntType(1):
                builder.ret(ir.Constant(ir.IntType(1), 0))
            elif isinstance(return_llvm_type, ir.PointerType):  
                builder.ret(ir.Constant(return_llvm_type, None))  
            else:
                
                raise SyntaxError(
                    f"Function '{func_name}' with non-void return type '{return_llvm_type}' must end with a return statement (line {ctx.stop.line if hasattr(ctx, 'stop') else line_info}).")

        self.current_function = None
        
        return None  

    def visitReturn_statement(self, ctx: SimpleLangParser.Return_statementContext, builder: ir.IRBuilder):
        if not self.current_function:
            raise SyntaxError(f"Return statement outside of function (line {ctx.start.line}).")

        current_func_llvm = self.module.globals.get(self.current_function)
        expected_return_type = current_func_llvm.function_type.return_type

        if ctx.expression():
            retval = self.visitExpression(ctx.expression(), builder)
            if retval.type != expected_return_type:
                if isinstance(expected_return_type, ir.DoubleType) and isinstance(retval.type, ir.IntType):
                    retval = builder.sitofp(retval, ir.DoubleType())
                elif isinstance(expected_return_type, ir.IntType) and expected_return_type.width == 32 and isinstance(
                        retval.type, ir.DoubleType):
                    retval = builder.fptosi(retval, expected_return_type)
                else:
                    raise TypeError(
                        f"Return type mismatch in function '{self.current_function}'. Expected {expected_return_type}, got {retval.type} (line {ctx.start.line}).")
            builder.ret(retval)
        elif ctx.boolean_expression():
            retval = self.visitBooleanExpression(ctx.boolean_expression(), builder)
            if retval.type != expected_return_type:
                if isinstance(expected_return_type,
                              ir.IntType) and expected_return_type.width == 32 and retval.type == ir.IntType(
                        1):  
                    retval = builder.zext(retval, expected_return_type)
                else:
                    raise TypeError(
                        f"Return type mismatch in function '{self.current_function}'. Expected {expected_return_type} (bool i1), got {retval.type} (line {ctx.start.line}).")
            builder.ret(retval)
        else:  
            if not isinstance(expected_return_type, ir.VoidType):
                raise TypeError(
                    f"Function '{self.current_function}' expects a return value of type {expected_return_type}, but return is void (line {ctx.start.line}).")
            builder.ret_void()

    def visitCode_block(self, ctx: SimpleLangParser.Code_blockContext, builder: ir.IRBuilder):
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if isinstance(child, SimpleLangParser.StatementContext):
                self.visitStatement_(child, builder)  
                if builder.block.is_terminated:  
                    break

    def visitStatement_(self, ctx: SimpleLangParser.StatementContext, builder: ir.IRBuilder):  
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
        elif ctx.input_statement():  
            self.visitInput_statement(ctx.input_statement())  
        else:
            raise ValueError(f"Unknown statement type: {ctx.getText()} (line {ctx.start.line})")

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
        self.module.triple = "aarch64-apple-darwin"  
        self.module.data_layout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"  
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