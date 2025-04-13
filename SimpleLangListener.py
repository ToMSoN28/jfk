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


    # Enter a parse tree produced by SimpleLangParser#if_statement.
    def enterIf_statement(self, ctx:SimpleLangParser.If_statementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#if_statement.
    def exitIf_statement(self, ctx:SimpleLangParser.If_statementContext):
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


    # Enter a parse tree produced by SimpleLangParser#Variable.
    def enterVariable(self, ctx:SimpleLangParser.VariableContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Variable.
    def exitVariable(self, ctx:SimpleLangParser.VariableContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Number.
    def enterNumber(self, ctx:SimpleLangParser.NumberContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Number.
    def exitNumber(self, ctx:SimpleLangParser.NumberContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#FuncCallNum.
    def enterFuncCallNum(self, ctx:SimpleLangParser.FuncCallNumContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#FuncCallNum.
    def exitFuncCallNum(self, ctx:SimpleLangParser.FuncCallNumContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#MulDiv.
    def enterMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#MulDiv.
    def exitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#AddSub.
    def enterAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#AddSub.
    def exitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#Parens.
    def enterParens(self, ctx:SimpleLangParser.ParensContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#Parens.
    def exitParens(self, ctx:SimpleLangParser.ParensContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#FloatNumber.
    def enterFloatNumber(self, ctx:SimpleLangParser.FloatNumberContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#FloatNumber.
    def exitFloatNumber(self, ctx:SimpleLangParser.FloatNumberContext):
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


    # Enter a parse tree produced by SimpleLangParser#FuncCallBool.
    def enterFuncCallBool(self, ctx:SimpleLangParser.FuncCallBoolContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#FuncCallBool.
    def exitFuncCallBool(self, ctx:SimpleLangParser.FuncCallBoolContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolCompareExpr.
    def enterBoolCompareExpr(self, ctx:SimpleLangParser.BoolCompareExprContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolCompareExpr.
    def exitBoolCompareExpr(self, ctx:SimpleLangParser.BoolCompareExprContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#BoolParens.
    def enterBoolParens(self, ctx:SimpleLangParser.BoolParensContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#BoolParens.
    def exitBoolParens(self, ctx:SimpleLangParser.BoolParensContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#comparizon_expression.
    def enterComparizon_expression(self, ctx:SimpleLangParser.Comparizon_expressionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#comparizon_expression.
    def exitComparizon_expression(self, ctx:SimpleLangParser.Comparizon_expressionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#loop_while.
    def enterLoop_while(self, ctx:SimpleLangParser.Loop_whileContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#loop_while.
    def exitLoop_while(self, ctx:SimpleLangParser.Loop_whileContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#function_definition.
    def enterFunction_definition(self, ctx:SimpleLangParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#function_definition.
    def exitFunction_definition(self, ctx:SimpleLangParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#parametr_list.
    def enterParametr_list(self, ctx:SimpleLangParser.Parametr_listContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#parametr_list.
    def exitParametr_list(self, ctx:SimpleLangParser.Parametr_listContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#code_block.
    def enterCode_block(self, ctx:SimpleLangParser.Code_blockContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#code_block.
    def exitCode_block(self, ctx:SimpleLangParser.Code_blockContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#func_call.
    def enterFunc_call(self, ctx:SimpleLangParser.Func_callContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#func_call.
    def exitFunc_call(self, ctx:SimpleLangParser.Func_callContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#argument_list.
    def enterArgument_list(self, ctx:SimpleLangParser.Argument_listContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#argument_list.
    def exitArgument_list(self, ctx:SimpleLangParser.Argument_listContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#return_statement.
    def enterReturn_statement(self, ctx:SimpleLangParser.Return_statementContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#return_statement.
    def exitReturn_statement(self, ctx:SimpleLangParser.Return_statementContext):
        pass


    # Enter a parse tree produced by SimpleLangParser#type.
    def enterType(self, ctx:SimpleLangParser.TypeContext):
        pass

    # Exit a parse tree produced by SimpleLangParser#type.
    def exitType(self, ctx:SimpleLangParser.TypeContext):
        pass



del SimpleLangParser