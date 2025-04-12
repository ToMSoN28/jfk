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
        4,1,32,141,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,3,2,40,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,58,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,70,8,4,1,5,
        1,5,1,5,1,5,3,5,76,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,96,8,7,1,7,1,7,1,7,1,7,1,7,1,7,
        5,7,104,8,7,10,7,12,7,107,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,3,8,119,8,8,1,8,1,8,1,8,5,8,124,8,8,10,8,12,8,127,9,8,1,9,
        1,9,1,9,1,9,1,10,1,10,4,10,135,8,10,11,10,12,10,136,1,10,1,10,1,
        10,0,2,14,16,11,0,2,4,6,8,10,12,14,16,18,20,0,4,1,0,12,13,1,0,14,
        15,1,0,16,18,1,0,20,25,150,0,23,1,0,0,0,2,32,1,0,0,0,4,34,1,0,0,
        0,6,57,1,0,0,0,8,69,1,0,0,0,10,71,1,0,0,0,12,80,1,0,0,0,14,95,1,
        0,0,0,16,118,1,0,0,0,18,128,1,0,0,0,20,132,1,0,0,0,22,24,3,2,1,0,
        23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,
        0,0,27,33,3,6,3,0,28,33,3,8,4,0,29,33,3,10,5,0,30,33,3,12,6,0,31,
        33,3,4,2,0,32,27,1,0,0,0,32,28,1,0,0,0,32,29,1,0,0,0,32,30,1,0,0,
        0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,1,0,0,35,36,3,16,8,0,36,39,
        3,20,10,0,37,38,5,2,0,0,38,40,3,20,10,0,39,37,1,0,0,0,39,40,1,0,
        0,0,40,5,1,0,0,0,41,42,5,3,0,0,42,43,5,29,0,0,43,44,5,4,0,0,44,45,
        5,30,0,0,45,58,5,5,0,0,46,47,5,6,0,0,47,48,5,29,0,0,48,49,5,4,0,
        0,49,50,5,31,0,0,50,58,5,5,0,0,51,52,5,7,0,0,52,53,5,29,0,0,53,54,
        5,4,0,0,54,55,3,16,8,0,55,56,5,5,0,0,56,58,1,0,0,0,57,41,1,0,0,0,
        57,46,1,0,0,0,57,51,1,0,0,0,58,7,1,0,0,0,59,60,5,29,0,0,60,61,5,
        4,0,0,61,62,3,14,7,0,62,63,5,5,0,0,63,70,1,0,0,0,64,65,5,29,0,0,
        65,66,5,4,0,0,66,67,3,16,8,0,67,68,5,5,0,0,68,70,1,0,0,0,69,59,1,
        0,0,0,69,64,1,0,0,0,70,9,1,0,0,0,71,72,5,8,0,0,72,75,5,9,0,0,73,
        76,3,14,7,0,74,76,3,16,8,0,75,73,1,0,0,0,75,74,1,0,0,0,76,77,1,0,
        0,0,77,78,5,10,0,0,78,79,5,5,0,0,79,11,1,0,0,0,80,81,5,29,0,0,81,
        82,5,4,0,0,82,83,5,11,0,0,83,84,5,9,0,0,84,85,5,10,0,0,85,86,5,5,
        0,0,86,13,1,0,0,0,87,88,6,7,-1,0,88,89,5,9,0,0,89,90,3,14,7,0,90,
        91,5,10,0,0,91,96,1,0,0,0,92,96,5,30,0,0,93,96,5,31,0,0,94,96,5,
        29,0,0,95,87,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,
        105,1,0,0,0,97,98,10,6,0,0,98,99,7,0,0,0,99,104,3,14,7,7,100,101,
        10,5,0,0,101,102,7,1,0,0,102,104,3,14,7,6,103,97,1,0,0,0,103,100,
        1,0,0,0,104,107,1,0,0,0,105,103,1,0,0,0,105,106,1,0,0,0,106,15,1,
        0,0,0,107,105,1,0,0,0,108,109,6,8,-1,0,109,110,5,19,0,0,110,119,
        3,16,8,5,111,112,5,9,0,0,112,113,3,16,8,0,113,114,5,10,0,0,114,119,
        1,0,0,0,115,119,5,28,0,0,116,119,5,29,0,0,117,119,3,18,9,0,118,108,
        1,0,0,0,118,111,1,0,0,0,118,115,1,0,0,0,118,116,1,0,0,0,118,117,
        1,0,0,0,119,125,1,0,0,0,120,121,10,6,0,0,121,122,7,2,0,0,122,124,
        3,16,8,7,123,120,1,0,0,0,124,127,1,0,0,0,125,123,1,0,0,0,125,126,
        1,0,0,0,126,17,1,0,0,0,127,125,1,0,0,0,128,129,3,14,7,0,129,130,
        7,3,0,0,130,131,3,14,7,0,131,19,1,0,0,0,132,134,5,26,0,0,133,135,
        3,2,1,0,134,133,1,0,0,0,135,136,1,0,0,0,136,134,1,0,0,0,136,137,
        1,0,0,0,137,138,1,0,0,0,138,139,5,27,0,0,139,21,1,0,0,0,12,25,32,
        39,57,69,75,95,103,105,118,125,136
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'int'", "'='", "';'", 
                     "'float'", "'bool'", "'print'", "'('", "')'", "'input'", 
                     "'*'", "'/'", "'+'", "'-'", "'AND'", "'OR'", "'XOR'", 
                     "'NEG'", "'>'", "'<'", "'=='", "'!='", "'<='", "'>='", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "BOOLEAN", "ID", "NUMBER", "FLOAT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_if_statement = 2
    RULE_variable_declaration = 3
    RULE_assignment = 4
    RULE_print_statement = 5
    RULE_input_statement = 6
    RULE_expression = 7
    RULE_boolean_expression = 8
    RULE_comparizon_expression = 9
    RULE_code_block = 10

    ruleNames =  [ "program", "statement", "if_statement", "variable_declaration", 
                   "assignment", "print_statement", "input_statement", "expression", 
                   "boolean_expression", "comparizon_expression", "code_block" ]

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
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    BOOLEAN=28
    ID=29
    NUMBER=30
    FLOAT=31
    WS=32

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
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 536871370) != 0)):
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


        def if_statement(self):
            return self.getTypedRuleContext(SimpleLangParser.If_statementContext,0)


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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 30
                self.input_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.if_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


        def code_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Code_blockContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Code_blockContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = SimpleLangParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_if_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(SimpleLangParser.T__0)
            self.state = 35
            self.boolean_expression(0)
            self.state = 36
            self.code_block()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 37
                self.match(SimpleLangParser.T__1)
                self.state = 38
                self.code_block()


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
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        try:
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(SimpleLangParser.T__2)
                self.state = 42
                self.match(SimpleLangParser.ID)
                self.state = 43
                self.match(SimpleLangParser.T__3)
                self.state = 44
                self.match(SimpleLangParser.NUMBER)
                self.state = 45
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.match(SimpleLangParser.T__5)
                self.state = 47
                self.match(SimpleLangParser.ID)
                self.state = 48
                self.match(SimpleLangParser.T__3)
                self.state = 49
                self.match(SimpleLangParser.FLOAT)
                self.state = 50
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(SimpleLangParser.T__6)
                self.state = 52
                self.match(SimpleLangParser.ID)
                self.state = 53
                self.match(SimpleLangParser.T__3)
                self.state = 54
                self.boolean_expression(0)
                self.state = 55
                self.match(SimpleLangParser.T__4)
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
        self.enterRule(localctx, 8, self.RULE_assignment)
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self.match(SimpleLangParser.ID)
                self.state = 60
                self.match(SimpleLangParser.T__3)
                self.state = 61
                self.expression(0)
                self.state = 62
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(SimpleLangParser.ID)
                self.state = 65
                self.match(SimpleLangParser.T__3)
                self.state = 66
                self.boolean_expression(0)
                self.state = 67
                self.match(SimpleLangParser.T__4)
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

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


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
        self.enterRule(localctx, 10, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(SimpleLangParser.T__7)
            self.state = 72
            self.match(SimpleLangParser.T__8)
            self.state = 75
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 73
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 74
                self.boolean_expression(0)
                pass


            self.state = 77
            self.match(SimpleLangParser.T__9)
            self.state = 78
            self.match(SimpleLangParser.T__4)
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
        self.enterRule(localctx, 12, self.RULE_input_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(SimpleLangParser.ID)
            self.state = 81
            self.match(SimpleLangParser.T__3)
            self.state = 82
            self.match(SimpleLangParser.T__10)
            self.state = 83
            self.match(SimpleLangParser.T__8)
            self.state = 84
            self.match(SimpleLangParser.T__9)
            self.state = 85
            self.match(SimpleLangParser.T__4)
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                localctx = SimpleLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 88
                self.match(SimpleLangParser.T__8)
                self.state = 89
                self.expression(0)
                self.state = 90
                self.match(SimpleLangParser.T__9)
                pass
            elif token in [30]:
                localctx = SimpleLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 92
                self.match(SimpleLangParser.NUMBER)
                pass
            elif token in [31]:
                localctx = SimpleLangParser.FloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 93
                self.match(SimpleLangParser.FLOAT)
                pass
            elif token in [29]:
                localctx = SimpleLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 94
                self.match(SimpleLangParser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 105
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 103
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 97
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 98
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 99
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 100
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 101
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 102
                        self.expression(6)
                        pass

             
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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


    class BoolCompareExprContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def comparizon_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Comparizon_expressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolCompareExpr" ):
                listener.enterBoolCompareExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolCompareExpr" ):
                listener.exitBoolCompareExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolCompareExpr" ):
                return visitor.visitBoolCompareExpr(self)
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
            self.state = 118
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.BoolNegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 109
                self.match(SimpleLangParser.T__18)
                self.state = 110
                self.boolean_expression(5)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.BoolParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(SimpleLangParser.T__8)
                self.state = 112
                self.boolean_expression(0)
                self.state = 113
                self.match(SimpleLangParser.T__9)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.BoolValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(SimpleLangParser.BOOLEAN)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.BoolVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.BoolCompareExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 117
                self.comparizon_expression()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 125
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleLangParser.BoolBinaryOpContext(self, SimpleLangParser.Boolean_expressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expression)
                    self.state = 120
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 121
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 122
                    self.boolean_expression(7) 
                self.state = 127
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Comparizon_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_comparizon_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparizon_expression" ):
                listener.enterComparizon_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparizon_expression" ):
                listener.exitComparizon_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparizon_expression" ):
                return visitor.visitComparizon_expression(self)
            else:
                return visitor.visitChildren(self)




    def comparizon_expression(self):

        localctx = SimpleLangParser.Comparizon_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_comparizon_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.expression(0)
            self.state = 129
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 130
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
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
            return SimpleLangParser.RULE_code_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCode_block" ):
                listener.enterCode_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCode_block" ):
                listener.exitCode_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = SimpleLangParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(SimpleLangParser.T__25)
            self.state = 134 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 133
                self.statement()
                self.state = 136 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 536871370) != 0)):
                    break

            self.state = 138
            self.match(SimpleLangParser.T__26)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        self._predicates[8] = self.boolean_expression_sempred
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
         

    def boolean_expression_sempred(self, localctx:Boolean_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         




