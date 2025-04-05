# Generated from SimpleLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SimpleLangParser import SimpleLangParser
else:
    from SimpleLangParser import SimpleLangParser

# This class defines a complete listener for a parse tree produced by SimpleLangParser.
class SimpleLangListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleLangParser#program.
    def enterProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#program.
    def exitProgram(self, ctx:SimpleLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#statement.
    def enterStatement(self, ctx:SimpleLangParser.StatementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#statement.
    def exitStatement(self, ctx:SimpleLangParser.StatementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#variable_declaration.
    def enterVariable_declaration(self, ctx:SimpleLangParser.Variable_declarationContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#variable_declaration.
    def exitVariable_declaration(self, ctx:SimpleLangParser.Variable_declarationContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#assignment.
    def enterAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#assignment.
    def exitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#print_statement.
    def enterPrint_statement(self, ctx:SimpleLangParser.Print_statementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#print_statement.
    def exitPrint_statement(self, ctx:SimpleLangParser.Print_statementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#input_statement.
    def enterInput_statement(self, ctx:SimpleLangParser.Input_statementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#input_statement.
    def exitInput_statement(self, ctx:SimpleLangParser.Input_statementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Number.
    def enterNumber(self, ctx:SimpleLangParser.NumberContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Number.
    def exitNumber(self, ctx:SimpleLangParser.NumberContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDivInt.
    def enterMulDivInt(self, ctx:SimpleLangParser.MulDivIntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDivInt.
    def exitMulDivInt(self, ctx:SimpleLangParser.MulDivIntContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSubInt.
    def enterAddSubInt(self, ctx:SimpleLangParser.AddSubIntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSubInt.
    def exitAddSubInt(self, ctx:SimpleLangParser.AddSubIntContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#VariableInt.
    def enterVariableInt(self, ctx:SimpleLangParser.VariableIntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#VariableInt.
    def exitVariableInt(self, ctx:SimpleLangParser.VariableIntContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ParensInt.
    def enterParensInt(self, ctx:SimpleLangParser.ParensIntContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ParensInt.
    def exitParensInt(self, ctx:SimpleLangParser.ParensIntContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#ParensFloat.
    def enterParensFloat(self, ctx:SimpleLangParser.ParensFloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#ParensFloat.
    def exitParensFloat(self, ctx:SimpleLangParser.ParensFloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSubFloat.
    def enterAddSubFloat(self, ctx:SimpleLangParser.AddSubFloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSubFloat.
    def exitAddSubFloat(self, ctx:SimpleLangParser.AddSubFloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#VariableFloat.
    def enterVariableFloat(self, ctx:SimpleLangParser.VariableFloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#VariableFloat.
    def exitVariableFloat(self, ctx:SimpleLangParser.VariableFloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#FloatNumber.
    def enterFloatNumber(self, ctx:SimpleLangParser.FloatNumberContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#FloatNumber.
    def exitFloatNumber(self, ctx:SimpleLangParser.FloatNumberContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDivFloat.
    def enterMulDivFloat(self, ctx:SimpleLangParser.MulDivFloatContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDivFloat.
    def exitMulDivFloat(self, ctx:SimpleLangParser.MulDivFloatContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolNegation.
    def enterBoolNegation(self, ctx:SimpleLangParser.BoolNegationContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolNegation.
    def exitBoolNegation(self, ctx:SimpleLangParser.BoolNegationContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolBinaryOp.
    def enterBoolBinaryOp(self, ctx:SimpleLangParser.BoolBinaryOpContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolBinaryOp.
    def exitBoolBinaryOp(self, ctx:SimpleLangParser.BoolBinaryOpContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolValue.
    def enterBoolValue(self, ctx:SimpleLangParser.BoolValueContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolValue.
    def exitBoolValue(self, ctx:SimpleLangParser.BoolValueContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolVariable.
    def enterBoolVariable(self, ctx:SimpleLangParser.BoolVariableContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolVariable.
    def exitBoolVariable(self, ctx:SimpleLangParser.BoolVariableContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolParens.
    def enterBoolParens(self, ctx:SimpleLangParser.BoolParensContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolParens.
    def exitBoolParens(self, ctx:SimpleLangParser.BoolParensContext):
        pass



del SimpleLangParser