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


    # Visit a parse tree produced by SimpleLangParser#Number.
    def visitNumber(self, ctx:SimpleLangParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDivInt.
    def visitMulDivInt(self, ctx:SimpleLangParser.MulDivIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSubInt.
    def visitAddSubInt(self, ctx:SimpleLangParser.AddSubIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#VariableInt.
    def visitVariableInt(self, ctx:SimpleLangParser.VariableIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ParensInt.
    def visitParensInt(self, ctx:SimpleLangParser.ParensIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ParensFloat.
    def visitParensFloat(self, ctx:SimpleLangParser.ParensFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSubFloat.
    def visitAddSubFloat(self, ctx:SimpleLangParser.AddSubFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#VariableFloat.
    def visitVariableFloat(self, ctx:SimpleLangParser.VariableFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#FloatNumber.
    def visitFloatNumber(self, ctx:SimpleLangParser.FloatNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDivFloat.
    def visitMulDivFloat(self, ctx:SimpleLangParser.MulDivFloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolNegation.
    def visitBoolNegation(self, ctx:SimpleLangParser.BoolNegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolBinaryOp.
    def visitBoolBinaryOp(self, ctx:SimpleLangParser.BoolBinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolValue.
    def visitBoolValue(self, ctx:SimpleLangParser.BoolValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolVariable.
    def visitBoolVariable(self, ctx:SimpleLangParser.BoolVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolParens.
    def visitBoolParens(self, ctx:SimpleLangParser.BoolParensContext):
        return self.visitChildren(ctx)



del SimpleLangParser