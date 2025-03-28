# Generated from SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete generic visitor for a parse tree produced by SimpleLangParser.

class SimpleLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SimpleLangParser#program.
    def visitProgram(self, ctx:SimpleLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#variable_declaration.
    def visitVariable_declaration(self, ctx:SimpleLangParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#print_statement.
    def visitPrint_statement(self, ctx:SimpleLangParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#input_statement.
    def visitInput_statement(self, ctx:SimpleLangParser.Input_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Variable.
    def visitVariable(self, ctx:SimpleLangParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Number.
    def visitNumber(self, ctx:SimpleLangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDiv.
    def visitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSub.
    def visitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#Parens.
    def visitParens(self, ctx:SimpleLangParser.ParensContext):
        return self.visitChildren(ctx)



del SimpleLangParser