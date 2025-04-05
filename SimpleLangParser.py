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
        4,1,22,143,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,48,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,65,8,3,1,4,1,4,1,4,1,4,1,4,3,4,72,8,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,3,6,91,8,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,99,8,6,10,6,12,6,102,
        9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,111,8,7,1,7,1,7,1,7,1,7,1,7,
        1,7,5,7,119,8,7,10,7,12,7,122,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,3,8,133,8,8,1,8,1,8,1,8,5,8,138,8,8,10,8,12,8,141,9,8,1,8,
        0,3,12,14,16,9,0,2,4,6,8,10,12,14,16,0,3,1,0,10,11,1,0,12,13,1,0,
        14,16,155,0,19,1,0,0,0,2,27,1,0,0,0,4,47,1,0,0,0,6,64,1,0,0,0,8,
        66,1,0,0,0,10,76,1,0,0,0,12,90,1,0,0,0,14,110,1,0,0,0,16,132,1,0,
        0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,1,1,0,0,0,23,28,3,4,2,0,24,28,3,6,3,0,25,28,3,8,4,0,26,
        28,3,10,5,0,27,23,1,0,0,0,27,24,1,0,0,0,27,25,1,0,0,0,27,26,1,0,
        0,0,28,3,1,0,0,0,29,30,5,1,0,0,30,31,5,19,0,0,31,32,5,2,0,0,32,33,
        3,12,6,0,33,34,5,3,0,0,34,48,1,0,0,0,35,36,5,4,0,0,36,37,5,19,0,
        0,37,38,5,2,0,0,38,39,3,14,7,0,39,40,5,3,0,0,40,48,1,0,0,0,41,42,
        5,5,0,0,42,43,5,19,0,0,43,44,5,2,0,0,44,45,3,16,8,0,45,46,5,3,0,
        0,46,48,1,0,0,0,47,29,1,0,0,0,47,35,1,0,0,0,47,41,1,0,0,0,48,5,1,
        0,0,0,49,50,5,19,0,0,50,51,5,2,0,0,51,52,3,14,7,0,52,53,5,3,0,0,
        53,65,1,0,0,0,54,55,5,19,0,0,55,56,5,2,0,0,56,57,3,12,6,0,57,58,
        5,3,0,0,58,65,1,0,0,0,59,60,5,19,0,0,60,61,5,2,0,0,61,62,3,16,8,
        0,62,63,5,3,0,0,63,65,1,0,0,0,64,49,1,0,0,0,64,54,1,0,0,0,64,59,
        1,0,0,0,65,7,1,0,0,0,66,67,5,6,0,0,67,71,5,7,0,0,68,72,3,14,7,0,
        69,72,3,12,6,0,70,72,3,16,8,0,71,68,1,0,0,0,71,69,1,0,0,0,71,70,
        1,0,0,0,72,73,1,0,0,0,73,74,5,8,0,0,74,75,5,3,0,0,75,9,1,0,0,0,76,
        77,5,19,0,0,77,78,5,2,0,0,78,79,5,9,0,0,79,80,5,7,0,0,80,81,5,8,
        0,0,81,82,5,3,0,0,82,11,1,0,0,0,83,84,6,6,-1,0,84,85,5,7,0,0,85,
        86,3,12,6,0,86,87,5,8,0,0,87,91,1,0,0,0,88,91,5,20,0,0,89,91,5,19,
        0,0,90,83,1,0,0,0,90,88,1,0,0,0,90,89,1,0,0,0,91,100,1,0,0,0,92,
        93,10,5,0,0,93,94,7,0,0,0,94,99,3,12,6,6,95,96,10,4,0,0,96,97,7,
        1,0,0,97,99,3,12,6,5,98,92,1,0,0,0,98,95,1,0,0,0,99,102,1,0,0,0,
        100,98,1,0,0,0,100,101,1,0,0,0,101,13,1,0,0,0,102,100,1,0,0,0,103,
        104,6,7,-1,0,104,105,5,7,0,0,105,106,3,14,7,0,106,107,5,8,0,0,107,
        111,1,0,0,0,108,111,5,21,0,0,109,111,5,19,0,0,110,103,1,0,0,0,110,
        108,1,0,0,0,110,109,1,0,0,0,111,120,1,0,0,0,112,113,10,5,0,0,113,
        114,7,0,0,0,114,119,3,14,7,6,115,116,10,4,0,0,116,117,7,1,0,0,117,
        119,3,14,7,5,118,112,1,0,0,0,118,115,1,0,0,0,119,122,1,0,0,0,120,
        118,1,0,0,0,120,121,1,0,0,0,121,15,1,0,0,0,122,120,1,0,0,0,123,124,
        6,8,-1,0,124,125,5,17,0,0,125,133,3,16,8,4,126,127,5,7,0,0,127,128,
        3,16,8,0,128,129,5,8,0,0,129,133,1,0,0,0,130,133,5,18,0,0,131,133,
        5,19,0,0,132,123,1,0,0,0,132,126,1,0,0,0,132,130,1,0,0,0,132,131,
        1,0,0,0,133,139,1,0,0,0,134,135,10,5,0,0,135,136,7,2,0,0,136,138,
        3,16,8,6,137,134,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,139,140,
        1,0,0,0,140,17,1,0,0,0,141,139,1,0,0,0,13,21,27,47,64,71,90,98,100,
        110,118,120,132,139
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'='", "';'", "'float'", "'bool'", 
                     "'print'", "'('", "')'", "'input'", "'*'", "'/'", "'+'", 
                     "'-'", "'AND'", "'OR'", "'XOR'", "'NEG'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "BOOLEAN", "ID", "NUMBER", 
                      "FLOAT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_variable_declaration = 2
    RULE_assignment = 3
    RULE_print_statement = 4
    RULE_input_statement = 5
    RULE_int_expression = 6
    RULE_float_expression = 7
    RULE_boolean_expression = 8

    ruleNames =  [ "program", "statement", "variable_declaration", "assignment", 
                   "print_statement", "input_statement", "int_expression", 
                   "float_expression", "boolean_expression" ]

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
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    BOOLEAN=18
    ID=19
    NUMBER=20
    FLOAT=21
    WS=22

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 524402) != 0)):
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
            self.state = 27
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
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

        def int_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Int_expressionContext,0)


        def float_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Float_expressionContext,0)


        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


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
            self.state = 47
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.match(SimpleLangParser.T__0)
                self.state = 30
                self.match(SimpleLangParser.ID)
                self.state = 31
                self.match(SimpleLangParser.T__1)
                self.state = 32
                self.int_expression(0)
                self.state = 33
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(SimpleLangParser.T__3)
                self.state = 36
                self.match(SimpleLangParser.ID)
                self.state = 37
                self.match(SimpleLangParser.T__1)
                self.state = 38
                self.float_expression(0)
                self.state = 39
                self.match(SimpleLangParser.T__2)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.match(SimpleLangParser.T__4)
                self.state = 42
                self.match(SimpleLangParser.ID)
                self.state = 43
                self.match(SimpleLangParser.T__1)
                self.state = 44
                self.boolean_expression(0)
                self.state = 45
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

        def float_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Float_expressionContext,0)


        def int_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Int_expressionContext,0)


        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


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
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(SimpleLangParser.ID)
                self.state = 50
                self.match(SimpleLangParser.T__1)
                self.state = 51
                self.float_expression(0)
                self.state = 52
                self.match(SimpleLangParser.T__2)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(SimpleLangParser.ID)
                self.state = 55
                self.match(SimpleLangParser.T__1)
                self.state = 56
                self.int_expression(0)
                self.state = 57
                self.match(SimpleLangParser.T__2)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 59
                self.match(SimpleLangParser.ID)
                self.state = 60
                self.match(SimpleLangParser.T__1)
                self.state = 61
                self.boolean_expression(0)
                self.state = 62
                self.match(SimpleLangParser.T__2)
                pass


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

        def float_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Float_expressionContext,0)


        def int_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Int_expressionContext,0)


        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


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
            self.state = 66
            self.match(SimpleLangParser.T__5)
            self.state = 67
            self.match(SimpleLangParser.T__6)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 68
                self.float_expression(0)
                pass

            elif la_ == 2:
                self.state = 69
                self.int_expression(0)
                pass

            elif la_ == 3:
                self.state = 70
                self.boolean_expression(0)
                pass


            self.state = 73
            self.match(SimpleLangParser.T__7)
            self.state = 74
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
            self.state = 76
            self.match(SimpleLangParser.ID)
            self.state = 77
            self.match(SimpleLangParser.T__1)
            self.state = 78
            self.match(SimpleLangParser.T__8)
            self.state = 79
            self.match(SimpleLangParser.T__6)
            self.state = 80
            self.match(SimpleLangParser.T__7)
            self.state = 81
            self.match(SimpleLangParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_int_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(Int_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Int_expressionContext
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


    class MulDivIntContext(Int_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Int_expressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def int_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Int_expressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Int_expressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivInt" ):
                listener.enterMulDivInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivInt" ):
                listener.exitMulDivInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivInt" ):
                return visitor.visitMulDivInt(self)
            else:
                return visitor.visitChildren(self)


    class AddSubIntContext(Int_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Int_expressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def int_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Int_expressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Int_expressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubInt" ):
                listener.enterAddSubInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubInt" ):
                listener.exitAddSubInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubInt" ):
                return visitor.visitAddSubInt(self)
            else:
                return visitor.visitChildren(self)


    class VariableIntContext(Int_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Int_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInt" ):
                listener.enterVariableInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInt" ):
                listener.exitVariableInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableInt" ):
                return visitor.visitVariableInt(self)
            else:
                return visitor.visitChildren(self)


    class ParensIntContext(Int_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Int_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Int_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensInt" ):
                listener.enterParensInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensInt" ):
                listener.exitParensInt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensInt" ):
                return visitor.visitParensInt(self)
            else:
                return visitor.visitChildren(self)



    def int_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.Int_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_int_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = SimpleLangParser.ParensIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 84
                self.match(SimpleLangParser.T__6)
                self.state = 85
                self.int_expression(0)
                self.state = 86
                self.match(SimpleLangParser.T__7)
                pass
            elif token in [20]:
                localctx = SimpleLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(SimpleLangParser.NUMBER)
                pass
            elif token in [19]:
                localctx = SimpleLangParser.VariableIntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 89
                self.match(SimpleLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivIntContext(self, SimpleLangParser.Int_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expression)
                        self.state = 92
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 93
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 94
                        self.int_expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubIntContext(self, SimpleLangParser.Int_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_int_expression)
                        self.state = 95
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 96
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 97
                        self.int_expression(5)
                        pass

             
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Float_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_float_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensFloatContext(Float_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Float_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def float_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Float_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensFloat" ):
                listener.enterParensFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensFloat" ):
                listener.exitParensFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensFloat" ):
                return visitor.visitParensFloat(self)
            else:
                return visitor.visitChildren(self)


    class AddSubFloatContext(Float_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Float_expressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def float_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Float_expressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Float_expressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSubFloat" ):
                listener.enterAddSubFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSubFloat" ):
                listener.exitAddSubFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSubFloat" ):
                return visitor.visitAddSubFloat(self)
            else:
                return visitor.visitChildren(self)


    class VariableFloatContext(Float_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Float_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableFloat" ):
                listener.enterVariableFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableFloat" ):
                listener.exitVariableFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableFloat" ):
                return visitor.visitVariableFloat(self)
            else:
                return visitor.visitChildren(self)


    class FloatNumberContext(Float_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Float_expressionContext
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


    class MulDivFloatContext(Float_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Float_expressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def float_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Float_expressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Float_expressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDivFloat" ):
                listener.enterMulDivFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDivFloat" ):
                listener.exitMulDivFloat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDivFloat" ):
                return visitor.visitMulDivFloat(self)
            else:
                return visitor.visitChildren(self)



    def float_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.Float_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_float_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                localctx = SimpleLangParser.ParensFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 104
                self.match(SimpleLangParser.T__6)
                self.state = 105
                self.float_expression(0)
                self.state = 106
                self.match(SimpleLangParser.T__7)
                pass
            elif token in [21]:
                localctx = SimpleLangParser.FloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(SimpleLangParser.FLOAT)
                pass
            elif token in [19]:
                localctx = SimpleLangParser.VariableFloatContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(SimpleLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 118
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivFloatContext(self, SimpleLangParser.Float_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expression)
                        self.state = 112
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 113
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 114
                        self.float_expression(6)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubFloatContext(self, SimpleLangParser.Float_expressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_float_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 116
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 117
                        self.float_expression(5)
                        pass

             
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Boolean_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_boolean_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class BoolNegationContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolNegation" ):
                listener.enterBoolNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolNegation" ):
                listener.exitBoolNegation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolNegation" ):
                return visitor.visitBoolNegation(self)
            else:
                return visitor.visitChildren(self)


    class BoolBinaryOpContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def boolean_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Boolean_expressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolBinaryOp" ):
                listener.enterBoolBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolBinaryOp" ):
                listener.exitBoolBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolBinaryOp" ):
                return visitor.visitBoolBinaryOp(self)
            else:
                return visitor.visitChildren(self)


    class BoolValueContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOLEAN(self):
            return self.getToken(SimpleLangParser.BOOLEAN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolValue" ):
                listener.enterBoolValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolValue" ):
                listener.exitBoolValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolValue" ):
                return visitor.visitBoolValue(self)
            else:
                return visitor.visitChildren(self)


    class BoolVariableContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolVariable" ):
                listener.enterBoolVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolVariable" ):
                listener.exitBoolVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolVariable" ):
                return visitor.visitBoolVariable(self)
            else:
                return visitor.visitChildren(self)


    class BoolParensContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolParens" ):
                listener.enterBoolParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolParens" ):
                listener.exitBoolParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolParens" ):
                return visitor.visitBoolParens(self)
            else:
                return visitor.visitChildren(self)



    def boolean_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.Boolean_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_boolean_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                localctx = SimpleLangParser.BoolNegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 124
                self.match(SimpleLangParser.T__16)
                self.state = 125
                self.boolean_expression(4)
                pass
            elif token in [7]:
                localctx = SimpleLangParser.BoolParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(SimpleLangParser.T__6)
                self.state = 127
                self.boolean_expression(0)
                self.state = 128
                self.match(SimpleLangParser.T__7)
                pass
            elif token in [18]:
                localctx = SimpleLangParser.BoolValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(SimpleLangParser.BOOLEAN)
                pass
            elif token in [19]:
                localctx = SimpleLangParser.BoolVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(SimpleLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleLangParser.BoolBinaryOpContext(self, SimpleLangParser.Boolean_expressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expression)
                    self.state = 134
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 135
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 136
                    self.boolean_expression(6) 
                self.state = 141
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self._predicates[6] = self.int_expression_sempred
        self._predicates[7] = self.float_expression_sempred
        self._predicates[8] = self.boolean_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def int_expression_sempred(self, localctx:Int_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def float_expression_sempred(self, localctx:Float_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

    def boolean_expression_sempred(self, localctx:Boolean_expressionContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         




