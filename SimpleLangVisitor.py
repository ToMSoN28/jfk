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


    # Visit a parse tree produced by SimpleLangParser#struct_definition.
    def visitStruct_definition(self, ctx:SimpleLangParser.Struct_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#field_declaration.
    def visitField_declaration(self, ctx:SimpleLangParser.Field_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#statement.
    def visitStatement(self, ctx:SimpleLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#if_statement.
    def visitIf_statement(self, ctx:SimpleLangParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#variable_declaration.
    def visitVariable_declaration(self, ctx:SimpleLangParser.Variable_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#table_declaration.
    def visitTable_declaration(self, ctx:SimpleLangParser.Table_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#assignment.
    def visitAssignment(self, ctx:SimpleLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#table_assignment.
    def visitTable_assignment(self, ctx:SimpleLangParser.Table_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#matrix_declaration.
    def visitMatrix_declaration(self, ctx:SimpleLangParser.Matrix_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#matrix_initializer.
    def visitMatrix_initializer(self, ctx:SimpleLangParser.Matrix_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#row_initializer.
    def visitRow_initializer(self, ctx:SimpleLangParser.Row_initializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#matrix_assignment.
    def visitMatrix_assignment(self, ctx:SimpleLangParser.Matrix_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#matrix_element_assignment.
    def visitMatrix_element_assignment(self, ctx:SimpleLangParser.Matrix_element_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#print_statement.
    def visitPrint_statement(self, ctx:SimpleLangParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#input_statement.
    def visitInput_statement(self, ctx:SimpleLangParser.Input_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#TableElemExpr.
    def visitTableElemExpr(self, ctx:SimpleLangParser.TableElemExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#StringExpr.
    def visitStringExpr(self, ctx:SimpleLangParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#FloatExpr.
    def visitFloatExpr(self, ctx:SimpleLangParser.FloatExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MatrixElemExpr.
    def visitMatrixElemExpr(self, ctx:SimpleLangParser.MatrixElemExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#NumberExpr.
    def visitNumberExpr(self, ctx:SimpleLangParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#MulDiv.
    def visitMulDiv(self, ctx:SimpleLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#AddSub.
    def visitAddSub(self, ctx:SimpleLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#StructMemberAccessExpr.
    def visitStructMemberAccessExpr(self, ctx:SimpleLangParser.StructMemberAccessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#ParensExpr.
    def visitParensExpr(self, ctx:SimpleLangParser.ParensExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#VariableExpr.
    def visitVariableExpr(self, ctx:SimpleLangParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#FuncCallExpr.
    def visitFuncCallExpr(self, ctx:SimpleLangParser.FuncCallExprContext):
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


    # Visit a parse tree produced by SimpleLangParser#FuncCallBool.
    def visitFuncCallBool(self, ctx:SimpleLangParser.FuncCallBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolCompareExpr.
    def visitBoolCompareExpr(self, ctx:SimpleLangParser.BoolCompareExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#BoolParens.
    def visitBoolParens(self, ctx:SimpleLangParser.BoolParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#comparizon_expression.
    def visitComparizon_expression(self, ctx:SimpleLangParser.Comparizon_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#loop_while.
    def visitLoop_while(self, ctx:SimpleLangParser.Loop_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#loop_for_iterator.
    def visitLoop_for_iterator(self, ctx:SimpleLangParser.Loop_for_iteratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#function_definition.
    def visitFunction_definition(self, ctx:SimpleLangParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#parametr_list.
    def visitParametr_list(self, ctx:SimpleLangParser.Parametr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#code_block.
    def visitCode_block(self, ctx:SimpleLangParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#func_call.
    def visitFunc_call(self, ctx:SimpleLangParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#argument_list.
    def visitArgument_list(self, ctx:SimpleLangParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#return_statement.
    def visitReturn_statement(self, ctx:SimpleLangParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SimpleLangParser#type.
    def visitType(self, ctx:SimpleLangParser.TypeContext):
        return self.visitChildren(ctx)



del SimpleLangParser