# Generated from SimpleLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,16,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,1,1,1,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,36,8,2,1,3,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,64,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,72,8,6,
        10,6,12,6,75,9,6,1,6,0,1,12,7,0,2,4,6,8,10,12,0,2,1,0,9,10,1,0,11,
        12,79,0,15,1,0,0,0,2,23,1,0,0,0,4,35,1,0,0,0,6,37,1,0,0,0,8,42,1,
        0,0,0,10,48,1,0,0,0,12,63,1,0,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,
        17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,1,1,0,0,0,19,24,3,4,2,
        0,20,24,3,6,3,0,21,24,3,8,4,0,22,24,3,10,5,0,23,19,1,0,0,0,23,20,
        1,0,0,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,1,0,0,26,
        27,5,13,0,0,27,28,5,2,0,0,28,29,5,14,0,0,29,36,5,3,0,0,30,31,5,4,
        0,0,31,32,5,13,0,0,32,33,5,2,0,0,33,34,5,15,0,0,34,36,5,3,0,0,35,
        25,1,0,0,0,35,30,1,0,0,0,36,5,1,0,0,0,37,38,5,13,0,0,38,39,5,2,0,
        0,39,40,3,12,6,0,40,41,5,3,0,0,41,7,1,0,0,0,42,43,5,5,0,0,43,44,
        5,6,0,0,44,45,3,12,6,0,45,46,5,7,0,0,46,47,5,3,0,0,47,9,1,0,0,0,
        48,49,5,13,0,0,49,50,5,2,0,0,50,51,5,8,0,0,51,52,5,6,0,0,52,53,5,
        7,0,0,53,54,5,3,0,0,54,11,1,0,0,0,55,56,6,6,-1,0,56,57,5,6,0,0,57,
        58,3,12,6,0,58,59,5,7,0,0,59,64,1,0,0,0,60,64,5,14,0,0,61,64,5,15,
        0,0,62,64,5,13,0,0,63,55,1,0,0,0,63,60,1,0,0,0,63,61,1,0,0,0,63,
        62,1,0,0,0,64,73,1,0,0,0,65,66,10,6,0,0,66,67,7,0,0,0,67,72,3,12,
        6,7,68,69,10,5,0,0,69,70,7,1,0,0,70,72,3,12,6,6,71,65,1,0,0,0,71,
        68,1,0,0,0,72,75,1,0,0,0,73,71,1,0,0,0,73,74,1,0,0,0,74,13,1,0,0,
        0,75,73,1,0,0,0,6,17,23,35,63,71,73
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'='", "';'", "'float'", "'print'", 
                     "'('", "')'", "'input'", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "FLOAT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variable_declaration = 2
    RULE_assignment = 3
    RULE_print_statement = 4
    RULE_input_statement = 5
    RULE_expression = 6

    ruleNames =  [ "program", "statement", "variable_declaration", "assignment", 
                   "print_statement", "input_statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    ID=13
    NUMBER=14
    FLOAT=15
    WS=16

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.StatementContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = SimpleLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 8242) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(SimpleLangParser.Variable_declarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(SimpleLangParser.AssignmentContext,0)


        def print_statement(self):
            return self.getTypedRuleContext(SimpleLangParser.Print_statementContext,0)


        def input_statement(self):
            return self.getTypedRuleContext(SimpleLangParser.Input_statementContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = SimpleLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 23
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 21
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 22
                self.input_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def NUMBER(self):
            return self.getToken(SimpleLangParser.NUMBER, 0)

        def FLOAT(self):
            return self.getToken(SimpleLangParser.FLOAT, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_variable_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable_declaration" ):
                listener.enterVariable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable_declaration" ):
                listener.exitVariable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = SimpleLangParser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable_declaration)
        try:
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.match(SimpleLangParser.T__0)
                self.state = 26
                self.match(SimpleLangParser.ID)
                self.state = 27
                self.match(SimpleLangParser.T__1)
                self.state = 28
                self.match(SimpleLangParser.NUMBER)
                self.state = 29
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(SimpleLangParser.T__3)
                self.state = 31
                self.match(SimpleLangParser.ID)
                self.state = 32
                self.match(SimpleLangParser.T__1)
                self.state = 33
                self.match(SimpleLangParser.FLOAT)
                self.state = 34
                self.match(SimpleLangParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = SimpleLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(SimpleLangParser.ID)
            self.state = 38
            self.match(SimpleLangParser.T__1)
            self.state = 39
            self.expression(0)
            self.state = 40
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_print_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrint_statement" ):
                listener.enterPrint_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrint_statement" ):
                listener.exitPrint_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrint_statement" ):
                return visitor.visitPrint_statement(self)
            else:
                return visitor.visitChildren(self)




    def print_statement(self):

        localctx = SimpleLangParser.Print_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(SimpleLangParser.T__4)
            self.state = 43
            self.match(SimpleLangParser.T__5)
            self.state = 44
            self.expression(0)
            self.state = 45
            self.match(SimpleLangParser.T__6)
            self.state = 46
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Input_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_input_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput_statement" ):
                listener.enterInput_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput_statement" ):
                listener.exitInput_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInput_statement" ):
                return visitor.visitInput_statement(self)
            else:
                return visitor.visitChildren(self)




    def input_statement(self):

        localctx = SimpleLangParser.Input_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_input_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SimpleLangParser.ID)
            self.state = 49
            self.match(SimpleLangParser.T__1)
            self.state = 50
            self.match(SimpleLangParser.T__7)
            self.state = 51
            self.match(SimpleLangParser.T__5)
            self.state = 52
            self.match(SimpleLangParser.T__6)
            self.state = 53
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(SimpleLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class FloatNumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(SimpleLangParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloatNumber" ):
                listener.enterFloatNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloatNumber" ):
                listener.exitFloatNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatNumber" ):
                return visitor.visitFloatNumber(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = SimpleLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 56
                self.match(SimpleLangParser.T__5)
                self.state = 57
                self.expression(0)
                self.state = 58
                self.match(SimpleLangParser.T__6)
                pass
            elif token in [14]:
                localctx = SimpleLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(SimpleLangParser.NUMBER)
                pass
            elif token in [15]:
                localctx = SimpleLangParser.FloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(SimpleLangParser.FLOAT)
                pass
            elif token in [13]:
                localctx = SimpleLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 62
                self.match(SimpleLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 73
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 71
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 65
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 66
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 67
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 68
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 69
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 70
                        self.expression(6)
                        pass

             
                self.state = 75
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




