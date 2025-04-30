# Generated from ./SimpleLang.g4 by ANTLR 4.13.2
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
        4,1,38,226,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,4,0,39,8,0,11,0,
        12,0,40,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,50,8,1,1,2,1,2,1,2,1,2,1,
        2,3,2,57,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,80,8,3,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,96,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,3,5,104,8,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,
        1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,125,8,7,1,7,1,7,1,7,1,7,1,7,1,7,
        5,7,133,8,7,10,7,12,7,136,9,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,3,8,149,8,8,1,8,1,8,1,8,5,8,154,8,8,10,8,12,8,157,9,8,
        1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,3,11,
        172,8,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,12,1,12,5,12,183,8,
        12,10,12,12,12,186,9,12,1,13,1,13,4,13,190,8,13,11,13,12,13,191,
        1,13,1,13,1,14,1,14,1,14,3,14,199,8,14,1,14,1,14,1,15,1,15,3,15,
        205,8,15,1,15,1,15,1,15,3,15,210,8,15,5,15,212,8,15,10,15,12,15,
        215,9,15,1,16,1,16,1,16,3,16,220,8,16,1,16,1,16,1,17,1,17,1,17,0,
        2,14,16,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,5,
        1,0,13,14,1,0,15,16,1,0,17,19,1,0,21,26,2,0,3,3,6,8,245,0,38,1,0,
        0,0,2,49,1,0,0,0,4,51,1,0,0,0,6,79,1,0,0,0,8,95,1,0,0,0,10,97,1,
        0,0,0,12,108,1,0,0,0,14,124,1,0,0,0,16,148,1,0,0,0,18,158,1,0,0,
        0,20,162,1,0,0,0,22,166,1,0,0,0,24,176,1,0,0,0,26,187,1,0,0,0,28,
        195,1,0,0,0,30,204,1,0,0,0,32,216,1,0,0,0,34,223,1,0,0,0,36,39,3,
        22,11,0,37,39,3,2,1,0,38,36,1,0,0,0,38,37,1,0,0,0,39,40,1,0,0,0,
        40,38,1,0,0,0,40,41,1,0,0,0,41,1,1,0,0,0,42,50,3,6,3,0,43,50,3,8,
        4,0,44,50,3,10,5,0,45,50,3,12,6,0,46,50,3,4,2,0,47,50,3,20,10,0,
        48,50,3,32,16,0,49,42,1,0,0,0,49,43,1,0,0,0,49,44,1,0,0,0,49,45,
        1,0,0,0,49,46,1,0,0,0,49,47,1,0,0,0,49,48,1,0,0,0,50,3,1,0,0,0,51,
        52,5,1,0,0,52,53,3,16,8,0,53,56,3,26,13,0,54,55,5,2,0,0,55,57,3,
        26,13,0,56,54,1,0,0,0,56,57,1,0,0,0,57,5,1,0,0,0,58,59,5,3,0,0,59,
        60,5,35,0,0,60,61,5,4,0,0,61,62,5,36,0,0,62,80,5,5,0,0,63,64,5,6,
        0,0,64,65,5,35,0,0,65,66,5,4,0,0,66,67,5,37,0,0,67,80,5,5,0,0,68,
        69,5,7,0,0,69,70,5,35,0,0,70,71,5,4,0,0,71,72,3,16,8,0,72,73,5,5,
        0,0,73,80,1,0,0,0,74,75,5,8,0,0,75,76,5,35,0,0,76,77,5,4,0,0,77,
        78,5,33,0,0,78,80,5,5,0,0,79,58,1,0,0,0,79,63,1,0,0,0,79,68,1,0,
        0,0,79,74,1,0,0,0,80,7,1,0,0,0,81,82,5,35,0,0,82,83,5,4,0,0,83,84,
        3,14,7,0,84,85,5,5,0,0,85,96,1,0,0,0,86,87,5,35,0,0,87,88,5,4,0,
        0,88,89,3,16,8,0,89,90,5,5,0,0,90,96,1,0,0,0,91,92,5,35,0,0,92,93,
        5,4,0,0,93,94,5,33,0,0,94,96,5,5,0,0,95,81,1,0,0,0,95,86,1,0,0,0,
        95,91,1,0,0,0,96,9,1,0,0,0,97,98,5,9,0,0,98,103,5,10,0,0,99,104,
        5,35,0,0,100,104,3,14,7,0,101,104,3,16,8,0,102,104,5,33,0,0,103,
        99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,105,
        1,0,0,0,105,106,5,11,0,0,106,107,5,5,0,0,107,11,1,0,0,0,108,109,
        5,35,0,0,109,110,5,4,0,0,110,111,5,12,0,0,111,112,5,10,0,0,112,113,
        5,11,0,0,113,114,5,5,0,0,114,13,1,0,0,0,115,116,6,7,-1,0,116,117,
        5,10,0,0,117,118,3,14,7,0,118,119,5,11,0,0,119,125,1,0,0,0,120,125,
        5,36,0,0,121,125,5,37,0,0,122,125,5,35,0,0,123,125,3,28,14,0,124,
        115,1,0,0,0,124,120,1,0,0,0,124,121,1,0,0,0,124,122,1,0,0,0,124,
        123,1,0,0,0,125,134,1,0,0,0,126,127,10,7,0,0,127,128,7,0,0,0,128,
        133,3,14,7,8,129,130,10,6,0,0,130,131,7,1,0,0,131,133,3,14,7,7,132,
        126,1,0,0,0,132,129,1,0,0,0,133,136,1,0,0,0,134,132,1,0,0,0,134,
        135,1,0,0,0,135,15,1,0,0,0,136,134,1,0,0,0,137,138,6,8,-1,0,138,
        139,5,20,0,0,139,149,3,16,8,6,140,141,5,10,0,0,141,142,3,16,8,0,
        142,143,5,11,0,0,143,149,1,0,0,0,144,149,5,34,0,0,145,149,5,35,0,
        0,146,149,3,18,9,0,147,149,3,28,14,0,148,137,1,0,0,0,148,140,1,0,
        0,0,148,144,1,0,0,0,148,145,1,0,0,0,148,146,1,0,0,0,148,147,1,0,
        0,0,149,155,1,0,0,0,150,151,10,7,0,0,151,152,7,2,0,0,152,154,3,16,
        8,8,153,150,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,
        0,0,156,17,1,0,0,0,157,155,1,0,0,0,158,159,3,14,7,0,159,160,7,3,
        0,0,160,161,3,14,7,0,161,19,1,0,0,0,162,163,5,27,0,0,163,164,3,16,
        8,0,164,165,3,26,13,0,165,21,1,0,0,0,166,167,5,28,0,0,167,168,3,
        34,17,0,168,169,5,35,0,0,169,171,5,10,0,0,170,172,3,24,12,0,171,
        170,1,0,0,0,171,172,1,0,0,0,172,173,1,0,0,0,173,174,5,11,0,0,174,
        175,3,26,13,0,175,23,1,0,0,0,176,177,3,34,17,0,177,184,5,35,0,0,
        178,179,5,29,0,0,179,180,3,34,17,0,180,181,5,35,0,0,181,183,1,0,
        0,0,182,178,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,
        0,0,185,25,1,0,0,0,186,184,1,0,0,0,187,189,5,30,0,0,188,190,3,2,
        1,0,189,188,1,0,0,0,190,191,1,0,0,0,191,189,1,0,0,0,191,192,1,0,
        0,0,192,193,1,0,0,0,193,194,5,31,0,0,194,27,1,0,0,0,195,196,5,35,
        0,0,196,198,5,10,0,0,197,199,3,30,15,0,198,197,1,0,0,0,198,199,1,
        0,0,0,199,200,1,0,0,0,200,201,5,11,0,0,201,29,1,0,0,0,202,205,3,
        14,7,0,203,205,3,16,8,0,204,202,1,0,0,0,204,203,1,0,0,0,205,213,
        1,0,0,0,206,209,5,29,0,0,207,210,3,14,7,0,208,210,3,16,8,0,209,207,
        1,0,0,0,209,208,1,0,0,0,210,212,1,0,0,0,211,206,1,0,0,0,212,215,
        1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,31,1,0,0,0,215,213,1,
        0,0,0,216,219,5,32,0,0,217,220,3,14,7,0,218,220,3,16,8,0,219,217,
        1,0,0,0,219,218,1,0,0,0,219,220,1,0,0,0,220,221,1,0,0,0,221,222,
        5,5,0,0,222,33,1,0,0,0,223,224,7,4,0,0,224,35,1,0,0,0,20,38,40,49,
        56,79,95,103,124,132,134,148,155,171,184,191,198,204,209,213,219
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'int'", "'='", "';'", 
                     "'float'", "'bool'", "'string'", "'print'", "'('", 
                     "')'", "'input'", "'*'", "'/'", "'+'", "'-'", "'AND'", 
                     "'OR'", "'XOR'", "'NEG'", "'>'", "'<'", "'=='", "'!='", 
                     "'<='", "'>='", "'while'", "'func'", "','", "'{'", 
                     "'}'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STRING", "BOOLEAN", "ID", "NUMBER", 
                      "FLOAT", "WS" ]

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
    T__31=32
    STRING=33
    BOOLEAN=34
    ID=35
    NUMBER=36
    FLOAT=37
    WS=38

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
                if token in [28]:
                    self.state = 36
                    self.function_definition()
                    pass
                elif token in [1, 3, 6, 7, 8, 9, 27, 32, 35]:
                    self.state = 37
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 39057359818) != 0)):
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


        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

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
            self.state = 79
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
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(SimpleLangParser.T__7)
                self.state = 75
                self.match(SimpleLangParser.ID)
                self.state = 76
                self.match(SimpleLangParser.T__3)
                self.state = 77
                self.match(SimpleLangParser.STRING)
                self.state = 78
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


        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.match(SimpleLangParser.ID)
                self.state = 82
                self.match(SimpleLangParser.T__3)
                self.state = 83
                self.expression(0)
                self.state = 84
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(SimpleLangParser.ID)
                self.state = 87
                self.match(SimpleLangParser.T__3)
                self.state = 88
                self.boolean_expression(0)
                self.state = 89
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.match(SimpleLangParser.ID)
                self.state = 92
                self.match(SimpleLangParser.T__3)
                self.state = 93
                self.match(SimpleLangParser.STRING)
                self.state = 94
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

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def boolean_expression(self):
            return self.getTypedRuleContext(SimpleLangParser.Boolean_expressionContext,0)


        def STRING(self):
            return self.getToken(SimpleLangParser.STRING, 0)

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
            self.state = 97
            self.match(SimpleLangParser.T__8)
            self.state = 98
            self.match(SimpleLangParser.T__9)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 99
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 100
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 101
                self.boolean_expression(0)
                pass

            elif la_ == 4:
                self.state = 102
                self.match(SimpleLangParser.STRING)
                pass


            self.state = 105
            self.match(SimpleLangParser.T__10)
            self.state = 106
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
            self.state = 108
            self.match(SimpleLangParser.ID)
            self.state = 109
            self.match(SimpleLangParser.T__3)
            self.state = 110
            self.match(SimpleLangParser.T__11)
            self.state = 111
            self.match(SimpleLangParser.T__9)
            self.state = 112
            self.match(SimpleLangParser.T__10)
            self.state = 113
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
            self.state = 124
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 116
                self.match(SimpleLangParser.T__9)
                self.state = 117
                self.expression(0)
                self.state = 118
                self.match(SimpleLangParser.T__10)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 120
                self.match(SimpleLangParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.FloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 121
                self.match(SimpleLangParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 122
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.FuncCallNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 123
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 132
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 126
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 127
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 128
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 129
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 130
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 131
                        self.expression(7)
                        pass

             
                self.state = 136
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
            self.state = 148
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.BoolNegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 138
                self.match(SimpleLangParser.T__19)
                self.state = 139
                self.boolean_expression(6)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.BoolParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(SimpleLangParser.T__9)
                self.state = 141
                self.boolean_expression(0)
                self.state = 142
                self.match(SimpleLangParser.T__10)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.BoolValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(SimpleLangParser.BOOLEAN)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.BoolVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.BoolCompareExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.comparizon_expression()
                pass

            elif la_ == 6:
                localctx = SimpleLangParser.FuncCallBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 147
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleLangParser.BoolBinaryOpContext(self, SimpleLangParser.Boolean_expressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expression)
                    self.state = 150
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 151
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 917504) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 152
                    self.boolean_expression(8) 
                self.state = 157
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
            self.state = 158
            self.expression(0)
            self.state = 159
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 160
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
            self.state = 162
            self.match(SimpleLangParser.T__26)
            self.state = 163
            self.boolean_expression(0)
            self.state = 164
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
            self.state = 166
            self.match(SimpleLangParser.T__27)
            self.state = 167
            self.type_()
            self.state = 168
            self.match(SimpleLangParser.ID)
            self.state = 169
            self.match(SimpleLangParser.T__9)
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 456) != 0):
                self.state = 170
                self.parametr_list()


            self.state = 173
            self.match(SimpleLangParser.T__10)
            self.state = 174
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
            self.state = 176
            self.type_()
            self.state = 177
            self.match(SimpleLangParser.ID)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 178
                self.match(SimpleLangParser.T__28)
                self.state = 179
                self.type_()
                self.state = 180
                self.match(SimpleLangParser.ID)
                self.state = 186
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
            self.state = 187
            self.match(SimpleLangParser.T__29)
            self.state = 189 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 188
                self.statement()
                self.state = 191 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 38788924362) != 0)):
                    break

            self.state = 193
            self.match(SimpleLangParser.T__30)
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
            self.state = 195
            self.match(SimpleLangParser.ID)
            self.state = 196
            self.match(SimpleLangParser.T__9)
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 257699087360) != 0):
                self.state = 197
                self.argument_list()


            self.state = 200
            self.match(SimpleLangParser.T__10)
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 202
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 203
                self.boolean_expression(0)
                pass


            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 206
                self.match(SimpleLangParser.T__28)
                self.state = 209
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 207
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 208
                    self.boolean_expression(0)
                    pass


                self.state = 215
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
            self.state = 216
            self.match(SimpleLangParser.T__31)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 217
                self.expression(0)

            elif la_ == 2:
                self.state = 218
                self.boolean_expression(0)


            self.state = 221
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
            self.state = 223
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 456) != 0)):
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
         




