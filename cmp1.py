import sys
from antlr4 import *
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from llvmlite import ir


class SimpleLangIRVisitor(SimpleLangVisitor):
    def __init__(self):
        self.module = ir.Module("SimpleLang")
        self.symbol_table = {}
        self.function_counter = 0 # Counter for unique function names

    def visitVariable_declaration(self, ctx):
        var_name = ctx.ID().getText()
        llvm_type = None
        initializer = None

        # Obsługa typu int
        if ctx.NUMBER():
            llvm_type = ir.IntType(32)  # 'i32' dla typu int
            initializer = ir.Constant(llvm_type, int(ctx.NUMBER().getText()))

        # Obsługa typu float
        elif ctx.FLOAT():
            llvm_type = ir.FloatType()  # 'float' dla typu float
            initializer = ir.Constant(llvm_type, float(ctx.FLOAT().getText()))
            
        # Obsługa typu bool
        elif ctx.boolean_expression():
            llvm_type = ir.IntType(1)  # 'i1' dla typu bool
            print(f"Boolean expression: {ctx.boolean_expression().getText()}")
            # bool_value = ctx.boolean_expression().getText()
            # initializer = ir.Constant(llvm_type, 1 if bool_value == "true" else 0)
            initializer = self.visitBooleanExpression(ctx.boolean_expression())

        if llvm_type is None or initializer is None:
            raise ValueError(f"Unsupported type for variable: {var_name}")

        # Deklaracja zmiennej globalnej
        global_var = ir.GlobalVariable(self.module, llvm_type, var_name)
        global_var.initializer = initializer

        # Dodanie zmiennej do tablicy symboli
        self.symbol_table[var_name] = global_var
        print(f"Declared variable: {var_name} = {initializer}")

    def visitAssignment(self, ctx):
        var_name = ctx.ID().getText()
        if ctx.expression():
            var_value = self.visitExpression(ctx.expression())  # Obsługa wyrażenia
        elif ctx.boolean_expression():
            var_value = self.visitBooleanExpression(ctx.boolean_expression())  # Obsługa wyrażenia logicznego
        else:
            raise ValueError("Invalid assignment")

        # Sprawdzenie, czy zmienna została zadeklarowana
        if var_name not in self.symbol_table:
            raise ValueError(f"Variable '{var_name}' is not declared")

        # Pobranie zmiennej globalnej
        global_var = self.symbol_table[var_name]

        # Sprawdzenie zgodności typów
        if isinstance(global_var.type.pointee, ir.IntType) and isinstance(var_value.type, ir.IntType):
            # Typy zgodne (int)
            pass
        elif isinstance(global_var.type.pointee, ir.FloatType) and isinstance(var_value.type, ir.FloatType):
            # Typy zgodne (float)
            pass
        elif isinstance(global_var.type.pointee, ir.FloatType) and isinstance(var_value.type, ir.IntType):
            # Rzutowanie int -> float
            unique_func_name = f"dummy_func_{self.function_counter}"
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
            block = dummy_func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            var_value = builder.sitofp(var_value, ir.FloatType())  # Rzutowanie int -> float
        elif isinstance(global_var.type.pointee, ir.IntType) and global_var.type.pointee.width == 1:  # Typ bool
            if isinstance(var_value.type, ir.IntType) and var_value.type.width == 1:
                pass  # Typy zgodne (bool)
            else:
                raise ValueError(f"Type mismatch for variable: {var_name}")
        else:
            raise ValueError(f"Type mismatch for variable: {var_name}")

        # Tworzenie instrukcji przypisania
        unique_func_name = f"dummy_func_{self.function_counter}"
        self.function_counter += 1
        dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
        block = dummy_func.append_basic_block(name="entry")
        builder = ir.IRBuilder(block)
        builder.store(var_value, global_var)
        print(f"Assigned {var_value} to {var_name}")
        
    def visitPrint_statement(self, ctx):
        expr_value = ctx.expression().getText()

        # Check if the expression is a variable or a number
        if expr_value.isdigit():
            value = int(expr_value)
        elif expr_value in self.symbol_table:
            # Load the value of the variable
            global_var = self.symbol_table[expr_value]
            unique_func_name = f"dummy_func_{self.function_counter}"
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
            block = dummy_func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            value = builder.load(global_var)
        else:
            raise ValueError(f"Unknown variable or invalid expression: {expr_value}")

        # Print the value (for simplicity, we just print it to the console)
        print(f"Print: {value}")

    def visitInput_statement(self, ctx):
        var_name = ctx.ID().getText()

        # Ensure the variable is declared
        if var_name not in self.symbol_table:
            raise ValueError(f"Variable '{var_name}' is not declared")

        # Simulate input (in a real scenario, this would involve runtime input handling)
        input_value = int(input(f"Enter value for {var_name}: "))

        # Retrieve the global variable from the symbol table
        global_var = self.symbol_table[var_name]

        # Ensure that the types match
        if isinstance(global_var.type.pointee, ir.IntType):  # Check if the type is 'i32'
            unique_func_name = f"dummy_func_{self.function_counter}"
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
            block = dummy_func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)

            # Create the store instruction
            value = ir.Constant(ir.IntType(32), input_value)
            builder.store(value, global_var)  # Use the builder to create the store instruction
            print(f"Input: {var_name} = {input_value}")
        else:
            raise ValueError(f"Type mismatch for variable: {var_name}")

    def visitExpression(self, ctx):
        if ctx.getChildCount() == 1:  # Pojedynczy element (liczba lub zmienna)
            text = ctx.getText()
            if text.isdigit():  # Jeśli to liczba całkowita
                return ir.Constant(ir.IntType(32), int(text))
            elif '.' in text:  # Jeśli to liczba zmiennoprzecinkowa
                try:
                    return ir.Constant(ir.FloatType(), float(text))
                except ValueError:
                    raise ValueError(f"Invalid float literal: {text}")
            elif text in self.symbol_table:  # Jeśli to zmienna
                var_name = text
                global_var = self.symbol_table[var_name]
                unique_func_name = f"dummy_func_{self.function_counter}"
                self.function_counter += 1
                dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
                block = dummy_func.append_basic_block(name="entry")
                builder = ir.IRBuilder(block)
                return builder.load(global_var)
            else:
                raise ValueError(f"Unknown variable or invalid expression: {text}")
        elif ctx.getChildCount() == 3:  # Wyrażenie binarne
            left = self.visitExpression(ctx.expression(0))
            right = self.visitExpression(ctx.expression(1))
            op = ctx.getChild(1).getText()  # Pobierz operator

            unique_func_name = f"dummy_func_{self.function_counter}"
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
            block = dummy_func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)

            # Obsługa operatorów dla int i float
            if isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
                if op == '+':
                    return builder.add(left, right)
                elif op == '-':
                    return builder.sub(left, right)
                elif op == '*':
                    return builder.mul(left, right)
                elif op == '/':
                    return builder.sdiv(left, right)  # Dzielimy całkowitoliczbowo
            elif isinstance(left.type, ir.FloatType) and isinstance(right.type, ir.FloatType):
                if op == '+':
                    return builder.fadd(left, right)
                elif op == '-':
                    return builder.fsub(left, right)
                elif op == '*':
                    return builder.fmul(left, right)
                elif op == '/':
                    return builder.fdiv(left, right)  # Dzielimy zmiennoprzecinkowo
            else:
                raise ValueError(f"Type mismatch in binary operation: {op}")
        else:
            raise ValueError("Invalid expression")
        
    def visitBooleanExpression(self, ctx):
        if ctx.getChildCount() == 1:  # Pojedynczy element (wartość logiczna lub zmienna)
            text = ctx.getText()
            if text == "true":
                return ir.Constant(ir.IntType(1), 1)
            elif text == "false":
                return ir.Constant(ir.IntType(1), 0)
            elif text in self.symbol_table:  # Jeśli to zmienna
                var_name = text
                global_var = self.symbol_table[var_name]
                unique_func_name = f"dummy_func_{self.function_counter}"
                self.function_counter += 1
                dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
                block = dummy_func.append_basic_block(name="entry")
                builder = ir.IRBuilder(block)
                return builder.load(global_var)
            else:
                raise ValueError(f"Unknown variable or invalid boolean expression: {text}")
        elif ctx.getChildCount() == 3:  # Wyrażenie logiczne binarne
            if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == "(" and ctx.getChild(2).getText() == ")":  # Nawiasy
            # Obsługa nawiasów
                return self.visitBooleanExpression(ctx.boolean_expression())  # Poprawne wywołanie dla nawiasów
            else:
                left = self.visitBooleanExpression(ctx.boolean_expression(0))
                right = self.visitBooleanExpression(ctx.boolean_expression(1))
                op = ctx.getChild(1).getText()  # Pobierz operator

                unique_func_name = f"dummy_func_{self.function_counter}"
                self.function_counter += 1
                dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
                block = dummy_func.append_basic_block(name="entry")
                builder = ir.IRBuilder(block)

                # Poprawna obsługa operatorów logicznych
                print(f"Left operand: {left}, Right operand: {right}, Operator: {op}")
                if op == "AND":
                    return builder.and_(left, right)
                elif op == "OR":
                    return builder.or_(left, right)
                elif op == "XOR":
                    return builder.xor(left, right)
                else:
                    raise ValueError(f"Unsupported boolean operator: {op}")
        elif ctx.getChildCount() == 2:  # Negacja logiczna
            operand = self.visitBooleanExpression(ctx.boolean_expression())
            unique_func_name = f"dummy_func_{self.function_counter}"
            self.function_counter += 1
            dummy_func = ir.Function(self.module, ir.FunctionType(ir.VoidType(), []), name=unique_func_name)
            block = dummy_func.append_basic_block(name="entry")
            builder = ir.IRBuilder(block)
            return builder.not_(operand)
        else:
            raise ValueError("Invalid boolean expression")
    
    def visitProgram(self, ctx):
        for statement in ctx.statement():
            self.visit(statement)

        # Set the ARM target triple and data layout for ARM (aarch64)
        self.module.triple = "x86_64-pc-windows-msvc"
        self.module.data_layout = "e-m:w-i64:64-f80:128-n8:16:32:64-S128"  # ARM64 layout

        print("Generated LLVM IR:")
        print(self.module)
        return self.module


def compile(input_text):
    input_stream = InputStream(input_text)
    lexer = SimpleLangLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SimpleLangParser(stream)
    tree = parser.program()
    
     # Drukowanie drzewa parsowania
    print("Parse Tree:")
    print(tree.toStringTree(recog=parser))  # Wypisuje drzewo parsowania

    visitor = SimpleLangIRVisitor()
    llvm_module = visitor.visitProgram(tree)
    return llvm_module


if __name__ == '__main__':
    input_text = """
    bool c = (true AND false) OR true;
    
    """
    llvm_module = compile(input_text)

    # Save LLVM IR to a file
    with open("output.ll", "w") as f:
        f.write(str(llvm_module))

    print("LLVM IR has been written to output.ll")