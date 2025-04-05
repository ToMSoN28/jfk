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
        self.function_counter = 0
        self.generated_funcs = []
        self.printf = None
        self._declare_printf()

    def _declare_printf(self):
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")

    def _create_global_format_str(self, fmt):
        fmt_bytes = bytearray(fmt.encode("utf8")) + b"\00"
        global_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_bytes)), name=f".fmt{self.function_counter}")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_bytes)), fmt_bytes)
        return global_fmt

    def visitVariable_declaration(self, ctx):
        var_name = ctx.ID().getText()

        if ctx.NUMBER():
            llvm_type = ir.IntType(32)
            initializer = ir.Constant(llvm_type, int(ctx.NUMBER().getText()))
        elif ctx.FLOAT():
            llvm_type = ir.FloatType()
            initializer = ir.Constant(llvm_type, float(ctx.FLOAT().getText()))
        elif ctx.boolean_expression():
            llvm_type = ir.IntType(1)
            initializer = self.visitBooleanExpression(ctx.boolean_expression())
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

        if ctx.expression():
            value = self.visitExpression(ctx.expression())
        elif ctx.boolean_expression():
            value = self.visitBooleanExpression(ctx.boolean_expression())
        else:
            raise ValueError("Invalid assignment")

        func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_func_{self.function_counter}")
        self.function_counter += 1
        self.generated_funcs.append(func.name)
        block = func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        builder.store(value, global_var)
        builder.ret_void()

    def visitPrint_statement(self, ctx):
        expr_text = ctx.expression().getText()
        if expr_text in self.symbol_table:
            global_var = self.symbol_table[expr_text]
            func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []),
                               name=f"dummy_func_{self.function_counter}")
            self.function_counter += 1
            self.generated_funcs.append(func.name)
            block = func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            value = builder.load(global_var)

            # Detect type and use proper format
            if value.type == ir.IntType(32):
                fmt = "%d\n"
            elif value.type == ir.FloatType():
                fmt = "%f\n"
            elif value.type == ir.IntType(1):
                fmt = "%d\n"
            else:
                raise ValueError(f"Unsupported type for print: {value.type}")

            fmt_var = self._create_global_format_str(fmt)
            fmt_ptr = builder.bitcast(fmt_var, ir.IntType(8).as_pointer())
            builder.call(self.printf, [fmt_ptr, value])
            builder.ret_void()

    def visitExpression(self, ctx):
        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if text.isdigit():
                return ir.Constant(ir.IntType(32), int(text))
            elif '.' in text:
                return ir.Constant(ir.FloatType(), float(text))
            elif text in self.symbol_table:
                global_var = self.symbol_table[text]
                func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_func_{self.function_counter}")
                self.function_counter += 1
                self.generated_funcs.append(func.name)
                block = func.append_basic_block(name="entry")
                builder = ir.IRBuilder(block)
                value = builder.load(global_var)
                builder.ret_void()
                return value
            else:
                raise ValueError(f"Unknown identifier: {text}")
        elif ctx.getChildCount() == 3:
            left = self.visitExpression(ctx.expression(0))
            right = self.visitExpression(ctx.expression(1))
            op = ctx.getChild(1).getText()

            if op == '+':
                return left + right if isinstance(left, ir.Constant) and isinstance(right, ir.Constant) else None
            elif op == '-':
                return left - right if isinstance(left, ir.Constant) and isinstance(right, ir.Constant) else None
            elif op == '*':
                return left * right if isinstance(left, ir.Constant) and isinstance(right, ir.Constant) else None
            elif op == '/':
                return left.sdiv(right) if isinstance(left.type, ir.IntType) else left.fdiv(right)
            else:
                raise ValueError(f"Unsupported binary operator: {op}")

    def visitBooleanExpression(self, ctx):
        if ctx.getChildCount() == 1:
            text = ctx.getText()
            if text == "true":
                return ir.Constant(ir.IntType(1), 1)
            elif text == "false":
                return ir.Constant(ir.IntType(1), 0)
            elif text in self.symbol_table:
                global_var = self.symbol_table[text]
                func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=f"dummy_func_{self.function_counter}")
                self.function_counter += 1
                self.generated_funcs.append(func.name)
                block = func.append_basic_block(name="entry")
                builder = ir.IRBuilder(block)
                value = builder.load(global_var)
                builder.ret_void()
                return value
            else:
                raise ValueError(f"Unknown boolean value: {text}")
        elif ctx.getChildCount() == 3:
            if ctx.getChild(0).getText() == "(" and ctx.getChild(2).getText() == ")":
                return self.visitBooleanExpression(ctx.getChild(1))
            else:
                left = self.visitBooleanExpression(ctx.getChild(0))
                right = self.visitBooleanExpression(ctx.getChild(2))
                op = ctx.getChild(1).getText()

                if op == "AND":
                    return ir.Constant(ir.IntType(1), int(bool(left.constant) and bool(right.constant)))
                elif op == "OR":
                    return ir.Constant(ir.IntType(1), int(bool(left.constant) or bool(right.constant)))
                elif op == "XOR":
                    return ir.Constant(ir.IntType(1), int(bool(left.constant) ^ bool(right.constant)))
                else:
                    raise ValueError(f"Unsupported boolean operator: {op}")

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
        # self.module.triple = "x86_64-pc-windows-msvc"
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
    bool c = (true AND false) OR true;
    int a = 10;
    float b = 10.1;
    print(a);
    print(b);
    """
    llvm_module = compile(input_text)

    with open("output.ll", "w") as f:
        f.write(str(llvm_module))
        

    print("LLVM IR has been written to output.ll")