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
        4,1,36,215,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,4,0,39,8,0,11,0,
        12,0,40,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,
        2,3,2,57,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,75,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,
        4,87,8,4,1,5,1,5,1,5,1,5,3,5,93,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,114,8,7,1,7,
        1,7,1,7,1,7,1,7,1,7,5,7,122,8,7,10,7,12,7,125,9,7,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,138,8,8,1,8,1,8,1,8,5,8,143,8,
        8,10,8,12,8,146,9,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,3,11,161,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,5,12,172,8,12,10,12,12,12,175,9,12,1,13,1,13,4,13,179,
        8,13,11,13,12,13,180,1,13,1,13,1,14,1,14,1,14,3,14,188,8,14,1,14,
        1,14,1,15,1,15,3,15,194,8,15,1,15,1,15,1,15,3,15,199,8,15,5,15,201,
        8,15,10,15,12,15,204,9,15,1,16,1,16,1,16,3,16,209,8,16,1,16,1,16,
        1,17,1,17,1,17,0,2,14,16,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,0,5,1,0,12,13,1,0,14,15,1,0,16,18,1,0,20,25,2,0,3,3,
        6,7,230,0,38,1,0,0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,74,1,0,0,0,8,86,
        1,0,0,0,10,88,1,0,0,0,12,97,1,0,0,0,14,113,1,0,0,0,16,137,1,0,0,
        0,18,147,1,0,0,0,20,151,1,0,0,0,22,155,1,0,0,0,24,165,1,0,0,0,26,
        176,1,0,0,0,28,184,1,0,0,0,30,193,1,0,0,0,32,205,1,0,0,0,34,212,
        1,0,0,0,36,39,3,22,11,0,37,39,3,2,1,0,38,36,1,0,0,0,38,37,1,0,0,
        0,39,40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,1,1,0,0,0,42,50,3,
        6,3,0,43,50,3,8,4,0,44,50,3,10,5,0,45,50,3,12,6,0,46,50,3,4,2,0,
        47,50,3,20,10,0,48,50,3,32,16,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,
        1,0,0,0,49,45,1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,
        50,3,1,0,0,0,51,52,5,1,0,0,52,53,3,16,8,0,53,56,3,26,13,0,54,55,
        5,2,0,0,55,57,3,26,13,0,56,54,1,0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,
        58,59,5,3,0,0,59,60,5,33,0,0,60,61,5,4,0,0,61,62,5,34,0,0,62,75,
        5,5,0,0,63,64,5,6,0,0,64,65,5,33,0,0,65,66,5,4,0,0,66,67,5,35,0,
        0,67,75,5,5,0,0,68,69,5,7,0,0,69,70,5,33,0,0,70,71,5,4,0,0,71,72,
        3,16,8,0,72,73,5,5,0,0,73,75,1,0,0,0,74,58,1,0,0,0,74,63,1,0,0,0,
        74,68,1,0,0,0,75,7,1,0,0,0,76,77,5,33,0,0,77,78,5,4,0,0,78,79,3,
        14,7,0,79,80,5,5,0,0,80,87,1,0,0,0,81,82,5,33,0,0,82,83,5,4,0,0,
        83,84,3,16,8,0,84,85,5,5,0,0,85,87,1,0,0,0,86,76,1,0,0,0,86,81,1,
        0,0,0,87,9,1,0,0,0,88,89,5,8,0,0,89,92,5,9,0,0,90,93,3,14,7,0,91,
        93,3,16,8,0,92,90,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,5,10,
        0,0,95,96,5,5,0,0,96,11,1,0,0,0,97,98,5,33,0,0,98,99,5,4,0,0,99,
        100,5,11,0,0,100,101,5,9,0,0,101,102,5,10,0,0,102,103,5,5,0,0,103,
        13,1,0,0,0,104,105,6,7,-1,0,105,106,5,9,0,0,106,107,3,14,7,0,107,
        108,5,10,0,0,108,114,1,0,0,0,109,114,5,34,0,0,110,114,5,35,0,0,111,
        114,5,33,0,0,112,114,3,28,14,0,113,104,1,0,0,0,113,109,1,0,0,0,113,
        110,1,0,0,0,113,111,1,0,0,0,113,112,1,0,0,0,114,123,1,0,0,0,115,
        116,10,7,0,0,116,117,7,0,0,0,117,122,3,14,7,8,118,119,10,6,0,0,119,
        120,7,1,0,0,120,122,3,14,7,7,121,115,1,0,0,0,121,118,1,0,0,0,122,
        125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,15,1,0,0,0,125,123,
        1,0,0,0,126,127,6,8,-1,0,127,128,5,19,0,0,128,138,3,16,8,6,129,130,
        5,9,0,0,130,131,3,16,8,0,131,132,5,10,0,0,132,138,1,0,0,0,133,138,
        5,32,0,0,134,138,5,33,0,0,135,138,3,18,9,0,136,138,3,28,14,0,137,
        126,1,0,0,0,137,129,1,0,0,0,137,133,1,0,0,0,137,134,1,0,0,0,137,
        135,1,0,0,0,137,136,1,0,0,0,138,144,1,0,0,0,139,140,10,7,0,0,140,
        141,7,2,0,0,141,143,3,16,8,8,142,139,1,0,0,0,143,146,1,0,0,0,144,
        142,1,0,0,0,144,145,1,0,0,0,145,17,1,0,0,0,146,144,1,0,0,0,147,148,
        3,14,7,0,148,149,7,3,0,0,149,150,3,14,7,0,150,19,1,0,0,0,151,152,
        5,26,0,0,152,153,3,16,8,0,153,154,3,26,13,0,154,21,1,0,0,0,155,156,
        5,27,0,0,156,157,3,34,17,0,157,158,5,33,0,0,158,160,5,9,0,0,159,
        161,3,24,12,0,160,159,1,0,0,0,160,161,1,0,0,0,161,162,1,0,0,0,162,
        163,5,10,0,0,163,164,3,26,13,0,164,23,1,0,0,0,165,166,3,34,17,0,
        166,173,5,33,0,0,167,168,5,28,0,0,168,169,3,34,17,0,169,170,5,33,
        0,0,170,172,1,0,0,0,171,167,1,0,0,0,172,175,1,0,0,0,173,171,1,0,
        0,0,173,174,1,0,0,0,174,25,1,0,0,0,175,173,1,0,0,0,176,178,5,29,
        0,0,177,179,3,2,1,0,178,177,1,0,0,0,179,180,1,0,0,0,180,178,1,0,
        0,0,180,181,1,0,0,0,181,182,1,0,0,0,182,183,5,30,0,0,183,27,1,0,
        0,0,184,185,5,33,0,0,185,187,5,9,0,0,186,188,3,30,15,0,187,186,1,
        0,0,0,187,188,1,0,0,0,188,189,1,0,0,0,189,190,5,10,0,0,190,29,1,
        0,0,0,191,194,3,14,7,0,192,194,3,16,8,0,193,191,1,0,0,0,193,192,
        1,0,0,0,194,202,1,0,0,0,195,198,5,28,0,0,196,199,3,14,7,0,197,199,
        3,16,8,0,198,196,1,0,0,0,198,197,1,0,0,0,199,201,1,0,0,0,200,195,
        1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,203,31,1,
        0,0,0,204,202,1,0,0,0,205,208,5,31,0,0,206,209,3,14,7,0,207,209,
        3,16,8,0,208,206,1,0,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,
        1,0,0,0,210,211,5,5,0,0,211,33,1,0,0,0,212,213,7,4,0,0,213,35,1,
        0,0,0,20,38,40,49,56,74,86,92,113,121,123,137,144,160,173,180,187,
        193,198,202,208
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
                     "'while'", "'func'", "','", "'{'", "'}'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_loop_while = 10
    RULE_function_definition = 11
    RULE_parametr_list = 12
    RULE_code_block = 13
    RULE_func_call = 14
    RULE_argument_list = 15
    RULE_return_statement = 16
    RULE_type = 17

    ruleNames =  [ "program", "statement", "if_statement", "variable_declaration", 
                   "assignment", "print_statement", "input_statement", "expression", 
                   "boolean_expression", "comparizon_expression", "loop_while", 
                   "function_definition", "parametr_list", "code_block", 
                   "func_call", "argument_list", "return_statement", "type" ]

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
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    BOOLEAN=32
    ID=33
    NUMBER=34
    FLOAT=35
    WS=36

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

        def function_definition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Function_definitionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Function_definitionContext,i)


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
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [27]:
                    self.state = 36
                    self.function_definition()
                    pass
                elif token in [1, 3, 6, 7, 8, 26, 31, 33]:
                    self.state = 37
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 10938745290) != 0)):
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


        def loop_while(self):
            return self.getTypedRuleContext(SimpleLangParser.Loop_whileContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(SimpleLangParser.Return_statementContext,0)


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
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 45
                self.input_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 46
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 47
                self.loop_while()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.return_statement()
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
            self.state = 51
            self.match(SimpleLangParser.T__0)
            self.state = 52
            self.boolean_expression(0)
            self.state = 53
            self.code_block()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 54
                self.match(SimpleLangParser.T__1)
                self.state = 55
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
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(SimpleLangParser.T__2)
                self.state = 59
                self.match(SimpleLangParser.ID)
                self.state = 60
                self.match(SimpleLangParser.T__3)
                self.state = 61
                self.match(SimpleLangParser.NUMBER)
                self.state = 62
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.match(SimpleLangParser.T__5)
                self.state = 64
                self.match(SimpleLangParser.ID)
                self.state = 65
                self.match(SimpleLangParser.T__3)
                self.state = 66
                self.match(SimpleLangParser.FLOAT)
                self.state = 67
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.match(SimpleLangParser.T__6)
                self.state = 69
                self.match(SimpleLangParser.ID)
                self.state = 70
                self.match(SimpleLangParser.T__3)
                self.state = 71
                self.boolean_expression(0)
                self.state = 72
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
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(SimpleLangParser.ID)
                self.state = 77
                self.match(SimpleLangParser.T__3)
                self.state = 78
                self.expression(0)
                self.state = 79
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.match(SimpleLangParser.ID)
                self.state = 82
                self.match(SimpleLangParser.T__3)
                self.state = 83
                self.boolean_expression(0)
                self.state = 84
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
            self.state = 88
            self.match(SimpleLangParser.T__7)
            self.state = 89
            self.match(SimpleLangParser.T__8)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 90
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 91
                self.boolean_expression(0)
                pass


            self.state = 94
            self.match(SimpleLangParser.T__9)
            self.state = 95
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
            self.state = 97
            self.match(SimpleLangParser.ID)
            self.state = 98
            self.match(SimpleLangParser.T__3)
            self.state = 99
            self.match(SimpleLangParser.T__10)
            self.state = 100
            self.match(SimpleLangParser.T__8)
            self.state = 101
            self.match(SimpleLangParser.T__9)
            self.state = 102
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


    class FuncCallNumContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call(self):
            return self.getTypedRuleContext(SimpleLangParser.Func_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallNum" ):
                listener.enterFuncCallNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallNum" ):
                listener.exitFuncCallNum(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallNum" ):
                return visitor.visitFuncCallNum(self)
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
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 105
                self.match(SimpleLangParser.T__8)
                self.state = 106
                self.expression(0)
                self.state = 107
                self.match(SimpleLangParser.T__9)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.match(SimpleLangParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.FloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.match(SimpleLangParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.FuncCallNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 121
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 115
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 116
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 117
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 118
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 119
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==14 or _la==15):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 120
                        self.expression(7)
                        pass

             
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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


    class FuncCallBoolContext(Boolean_expressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.Boolean_expressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func_call(self):
            return self.getTypedRuleContext(SimpleLangParser.Func_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallBool" ):
                listener.enterFuncCallBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallBool" ):
                listener.exitFuncCallBool(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallBool" ):
                return visitor.visitFuncCallBool(self)
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
            self.state = 137
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.BoolNegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 127
                self.match(SimpleLangParser.T__18)
                self.state = 128
                self.boolean_expression(6)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.BoolParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 129
                self.match(SimpleLangParser.T__8)
                self.state = 130
                self.boolean_expression(0)
                self.state = 131
                self.match(SimpleLangParser.T__9)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.BoolValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 133
                self.match(SimpleLangParser.BOOLEAN)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.BoolVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.BoolCompareExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.comparizon_expression()
                pass

            elif la_ == 6:
                localctx = SimpleLangParser.FuncCallBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 136
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 144
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleLangParser.BoolBinaryOpContext(self, SimpleLangParser.Boolean_expressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expression)
                    self.state = 139
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 140
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 458752) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 141
                    self.boolean_expression(8) 
                self.state = 146
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
            self.state = 147
            self.expression(0)
            self.state = 148
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 149
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


        def code_block(self):
            return self.getTypedRuleContext(SimpleLangParser.Code_blockContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_loop_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_while" ):
                listener.enterLoop_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_while" ):
                listener.exitLoop_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoop_while" ):
                return visitor.visitLoop_while(self)
            else:
                return visitor.visitChildren(self)




    def loop_while(self):

        localctx = SimpleLangParser.Loop_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_loop_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(SimpleLangParser.T__25)
            self.state = 152
            self.boolean_expression(0)
            self.state = 153
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def code_block(self):
            return self.getTypedRuleContext(SimpleLangParser.Code_blockContext,0)


        def parametr_list(self):
            return self.getTypedRuleContext(SimpleLangParser.Parametr_listContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_function_definition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definition" ):
                listener.enterFunction_definition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definition" ):
                listener.exitFunction_definition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_definition" ):
                return visitor.visitFunction_definition(self)
            else:
                return visitor.visitChildren(self)




    def function_definition(self):

        localctx = SimpleLangParser.Function_definitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_function_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(SimpleLangParser.T__26)
            self.state = 156
            self.type_()
            self.state = 157
            self.match(SimpleLangParser.ID)
            self.state = 158
            self.match(SimpleLangParser.T__8)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 200) != 0):
                self.state = 159
                self.parametr_list()


            self.state = 162
            self.match(SimpleLangParser.T__9)
            self.state = 163
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Parametr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.TypeContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.TypeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(SimpleLangParser.ID)
            else:
                return self.getToken(SimpleLangParser.ID, i)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_parametr_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametr_list" ):
                listener.enterParametr_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametr_list" ):
                listener.exitParametr_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametr_list" ):
                return visitor.visitParametr_list(self)
            else:
                return visitor.visitChildren(self)




    def parametr_list(self):

        localctx = SimpleLangParser.Parametr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parametr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.type_()
            self.state = 166
            self.match(SimpleLangParser.ID)
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 167
                self.match(SimpleLangParser.T__27)
                self.state = 168
                self.type_()
                self.state = 169
                self.match(SimpleLangParser.ID)
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 26, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(SimpleLangParser.T__28)
            self.state = 178 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 177
                self.statement()
                self.state = 180 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 10804527562) != 0)):
                    break

            self.state = 182
            self.match(SimpleLangParser.T__29)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def argument_list(self):
            return self.getTypedRuleContext(SimpleLangParser.Argument_listContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_func_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc_call" ):
                listener.enterFunc_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc_call" ):
                listener.exitFunc_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_call" ):
                return visitor.visitFunc_call(self)
            else:
                return visitor.visitChildren(self)




    def func_call(self):

        localctx = SimpleLangParser.Func_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(SimpleLangParser.ID)
            self.state = 185
            self.match(SimpleLangParser.T__8)
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 64425034240) != 0):
                self.state = 186
                self.argument_list()


            self.state = 189
            self.match(SimpleLangParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Argument_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def boolean_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.Boolean_expressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_argument_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgument_list" ):
                listener.enterArgument_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgument_list" ):
                listener.exitArgument_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument_list" ):
                return visitor.visitArgument_list(self)
            else:
                return visitor.visitChildren(self)




    def argument_list(self):

        localctx = SimpleLangParser.Argument_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 191
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 192
                self.boolean_expression(0)
                pass


            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 195
                self.match(SimpleLangParser.T__27)
                self.state = 198
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 196
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 197
                    self.boolean_expression(0)
                    pass


                self.state = 204
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = SimpleLangParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(SimpleLangParser.T__30)
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 206
                self.expression(0)

            elif la_ == 2:
                self.state = 207
                self.boolean_expression(0)


            self.state = 210
            self.match(SimpleLangParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SimpleLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = SimpleLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 200) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

    def boolean_expression_sempred(self, localctx:Boolean_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




