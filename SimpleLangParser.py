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
        4,1,40,268,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        1,0,4,0,43,8,0,11,0,12,0,44,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        3,1,56,8,1,1,2,1,2,1,2,1,2,1,2,3,2,63,8,2,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,
        3,86,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,109,8,5,1,6,1,6,1,6,1,6,1,6,1,6,
        5,6,117,8,6,10,6,12,6,120,9,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,133,8,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,141,8,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,167,8,9,1,9,1,9,1,9,1,9,1,9,1,9,5,
        9,175,8,9,10,9,12,9,178,9,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,3,10,191,8,10,1,10,1,10,1,10,5,10,196,8,10,10,
        10,12,10,199,9,10,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,
        13,1,13,1,13,1,13,3,13,214,8,13,1,13,1,13,1,13,1,14,1,14,1,14,1,
        14,1,14,1,14,5,14,225,8,14,10,14,12,14,228,9,14,1,15,1,15,4,15,232,
        8,15,11,15,12,15,233,1,15,1,15,1,16,1,16,1,16,3,16,241,8,16,1,16,
        1,16,1,17,1,17,3,17,247,8,17,1,17,1,17,1,17,3,17,252,8,17,5,17,254,
        8,17,10,17,12,17,257,9,17,1,18,1,18,1,18,3,18,262,8,18,1,18,1,18,
        1,19,1,19,1,19,0,2,18,20,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,0,5,1,0,16,17,1,0,18,19,1,0,20,22,1,0,24,29,2,
        0,3,3,6,8,290,0,42,1,0,0,0,2,55,1,0,0,0,4,57,1,0,0,0,6,85,1,0,0,
        0,8,87,1,0,0,0,10,108,1,0,0,0,12,132,1,0,0,0,14,134,1,0,0,0,16,145,
        1,0,0,0,18,166,1,0,0,0,20,190,1,0,0,0,22,200,1,0,0,0,24,204,1,0,
        0,0,26,208,1,0,0,0,28,218,1,0,0,0,30,229,1,0,0,0,32,237,1,0,0,0,
        34,246,1,0,0,0,36,258,1,0,0,0,38,265,1,0,0,0,40,43,3,26,13,0,41,
        43,3,2,1,0,42,40,1,0,0,0,42,41,1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,
        0,44,45,1,0,0,0,45,1,1,0,0,0,46,56,3,6,3,0,47,56,3,10,5,0,48,56,
        3,14,7,0,49,56,3,16,8,0,50,56,3,4,2,0,51,56,3,24,12,0,52,56,3,36,
        18,0,53,56,3,8,4,0,54,56,3,12,6,0,55,46,1,0,0,0,55,47,1,0,0,0,55,
        48,1,0,0,0,55,49,1,0,0,0,55,50,1,0,0,0,55,51,1,0,0,0,55,52,1,0,0,
        0,55,53,1,0,0,0,55,54,1,0,0,0,56,3,1,0,0,0,57,58,5,1,0,0,58,59,3,
        20,10,0,59,62,3,30,15,0,60,61,5,2,0,0,61,63,3,30,15,0,62,60,1,0,
        0,0,62,63,1,0,0,0,63,5,1,0,0,0,64,65,5,3,0,0,65,66,5,37,0,0,66,67,
        5,4,0,0,67,68,5,38,0,0,68,86,5,5,0,0,69,70,5,6,0,0,70,71,5,37,0,
        0,71,72,5,4,0,0,72,73,5,39,0,0,73,86,5,5,0,0,74,75,5,7,0,0,75,76,
        5,37,0,0,76,77,5,4,0,0,77,78,3,20,10,0,78,79,5,5,0,0,79,86,1,0,0,
        0,80,81,5,8,0,0,81,82,5,37,0,0,82,83,5,4,0,0,83,84,5,35,0,0,84,86,
        5,5,0,0,85,64,1,0,0,0,85,69,1,0,0,0,85,74,1,0,0,0,85,80,1,0,0,0,
        86,7,1,0,0,0,87,88,3,38,19,0,88,89,5,9,0,0,89,90,5,38,0,0,90,91,
        5,10,0,0,91,92,5,37,0,0,92,93,5,5,0,0,93,9,1,0,0,0,94,95,5,37,0,
        0,95,96,5,4,0,0,96,97,3,18,9,0,97,98,5,5,0,0,98,109,1,0,0,0,99,100,
        5,37,0,0,100,101,5,4,0,0,101,102,3,20,10,0,102,103,5,5,0,0,103,109,
        1,0,0,0,104,105,5,37,0,0,105,106,5,4,0,0,106,107,5,35,0,0,107,109,
        5,5,0,0,108,94,1,0,0,0,108,99,1,0,0,0,108,104,1,0,0,0,109,11,1,0,
        0,0,110,111,5,37,0,0,111,112,5,4,0,0,112,113,5,9,0,0,113,118,3,18,
        9,0,114,115,5,11,0,0,115,117,3,18,9,0,116,114,1,0,0,0,117,120,1,
        0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,121,1,0,0,0,120,118,1,
        0,0,0,121,122,5,10,0,0,122,123,5,5,0,0,123,133,1,0,0,0,124,125,5,
        37,0,0,125,126,5,9,0,0,126,127,3,18,9,0,127,128,5,10,0,0,128,129,
        5,4,0,0,129,130,3,18,9,0,130,131,5,5,0,0,131,133,1,0,0,0,132,110,
        1,0,0,0,132,124,1,0,0,0,133,13,1,0,0,0,134,135,5,12,0,0,135,140,
        5,13,0,0,136,141,5,37,0,0,137,141,3,18,9,0,138,141,3,20,10,0,139,
        141,5,35,0,0,140,136,1,0,0,0,140,137,1,0,0,0,140,138,1,0,0,0,140,
        139,1,0,0,0,141,142,1,0,0,0,142,143,5,14,0,0,143,144,5,5,0,0,144,
        15,1,0,0,0,145,146,5,37,0,0,146,147,5,4,0,0,147,148,5,15,0,0,148,
        149,5,13,0,0,149,150,5,14,0,0,150,151,5,5,0,0,151,17,1,0,0,0,152,
        153,6,9,-1,0,153,154,5,13,0,0,154,155,3,18,9,0,155,156,5,14,0,0,
        156,167,1,0,0,0,157,167,5,38,0,0,158,167,5,39,0,0,159,167,5,37,0,
        0,160,167,3,32,16,0,161,162,5,37,0,0,162,163,5,9,0,0,163,164,3,18,
        9,0,164,165,5,10,0,0,165,167,1,0,0,0,166,152,1,0,0,0,166,157,1,0,
        0,0,166,158,1,0,0,0,166,159,1,0,0,0,166,160,1,0,0,0,166,161,1,0,
        0,0,167,176,1,0,0,0,168,169,10,8,0,0,169,170,7,0,0,0,170,175,3,18,
        9,9,171,172,10,7,0,0,172,173,7,1,0,0,173,175,3,18,9,8,174,168,1,
        0,0,0,174,171,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,
        0,0,0,177,19,1,0,0,0,178,176,1,0,0,0,179,180,6,10,-1,0,180,181,5,
        23,0,0,181,191,3,20,10,6,182,183,5,13,0,0,183,184,3,20,10,0,184,
        185,5,14,0,0,185,191,1,0,0,0,186,191,5,36,0,0,187,191,5,37,0,0,188,
        191,3,22,11,0,189,191,3,32,16,0,190,179,1,0,0,0,190,182,1,0,0,0,
        190,186,1,0,0,0,190,187,1,0,0,0,190,188,1,0,0,0,190,189,1,0,0,0,
        191,197,1,0,0,0,192,193,10,7,0,0,193,194,7,2,0,0,194,196,3,20,10,
        8,195,192,1,0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,
        0,198,21,1,0,0,0,199,197,1,0,0,0,200,201,3,18,9,0,201,202,7,3,0,
        0,202,203,3,18,9,0,203,23,1,0,0,0,204,205,5,30,0,0,205,206,3,20,
        10,0,206,207,3,30,15,0,207,25,1,0,0,0,208,209,5,31,0,0,209,210,3,
        38,19,0,210,211,5,37,0,0,211,213,5,13,0,0,212,214,3,28,14,0,213,
        212,1,0,0,0,213,214,1,0,0,0,214,215,1,0,0,0,215,216,5,14,0,0,216,
        217,3,30,15,0,217,27,1,0,0,0,218,219,3,38,19,0,219,226,5,37,0,0,
        220,221,5,11,0,0,221,222,3,38,19,0,222,223,5,37,0,0,223,225,1,0,
        0,0,224,220,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,
        0,0,227,29,1,0,0,0,228,226,1,0,0,0,229,231,5,32,0,0,230,232,3,2,
        1,0,231,230,1,0,0,0,232,233,1,0,0,0,233,231,1,0,0,0,233,234,1,0,
        0,0,234,235,1,0,0,0,235,236,5,33,0,0,236,31,1,0,0,0,237,238,5,37,
        0,0,238,240,5,13,0,0,239,241,3,34,17,0,240,239,1,0,0,0,240,241,1,
        0,0,0,241,242,1,0,0,0,242,243,5,14,0,0,243,33,1,0,0,0,244,247,3,
        18,9,0,245,247,3,20,10,0,246,244,1,0,0,0,246,245,1,0,0,0,247,255,
        1,0,0,0,248,251,5,11,0,0,249,252,3,18,9,0,250,252,3,20,10,0,251,
        249,1,0,0,0,251,250,1,0,0,0,252,254,1,0,0,0,253,248,1,0,0,0,254,
        257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,35,1,0,0,0,257,255,
        1,0,0,0,258,261,5,34,0,0,259,262,3,18,9,0,260,262,3,20,10,0,261,
        259,1,0,0,0,261,260,1,0,0,0,261,262,1,0,0,0,262,263,1,0,0,0,263,
        264,5,5,0,0,264,37,1,0,0,0,265,266,7,4,0,0,266,39,1,0,0,0,22,42,
        44,55,62,85,108,118,132,140,166,174,176,190,197,213,226,233,240,
        246,251,255,261
    ]

class SimpleLangParser ( Parser ):

    grammarFileName = "SimpleLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'int'", "'='", "';'", 
                     "'float'", "'bool'", "'string'", "'['", "']'", "','", 
                     "'print'", "'('", "')'", "'input'", "'*'", "'/'", "'+'", 
                     "'-'", "'AND'", "'OR'", "'XOR'", "'NEG'", "'>'", "'<'", 
                     "'=='", "'!='", "'<='", "'>='", "'while'", "'func'", 
                     "'{'", "'}'", "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "STRING", "BOOLEAN", 
                      "ID", "NUMBER", "FLOAT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_if_statement = 2
    RULE_variable_declaration = 3
    RULE_table_declaration = 4
    RULE_assignment = 5
    RULE_table_assignment = 6
    RULE_print_statement = 7
    RULE_input_statement = 8
    RULE_expression = 9
    RULE_boolean_expression = 10
    RULE_comparizon_expression = 11
    RULE_loop_while = 12
    RULE_function_definition = 13
    RULE_parametr_list = 14
    RULE_code_block = 15
    RULE_func_call = 16
    RULE_argument_list = 17
    RULE_return_statement = 18
    RULE_type = 19

    ruleNames =  [ "program", "statement", "if_statement", "variable_declaration", 
                   "table_declaration", "assignment", "table_assignment", 
                   "print_statement", "input_statement", "expression", "boolean_expression", 
                   "comparizon_expression", "loop_while", "function_definition", 
                   "parametr_list", "code_block", "func_call", "argument_list", 
                   "return_statement", "type" ]

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
    T__32=33
    T__33=34
    STRING=35
    BOOLEAN=36
    ID=37
    NUMBER=38
    FLOAT=39
    WS=40

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
            self.state = 42 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 42
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [31]:
                    self.state = 40
                    self.function_definition()
                    pass
                elif token in [1, 3, 6, 7, 8, 12, 30, 34, 37]:
                    self.state = 41
                    self.statement()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 157840052682) != 0)):
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


        def table_declaration(self):
            return self.getTypedRuleContext(SimpleLangParser.Table_declarationContext,0)


        def table_assignment(self):
            return self.getTypedRuleContext(SimpleLangParser.Table_assignmentContext,0)


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
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.print_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 49
                self.input_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 51
                self.loop_while()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 52
                self.return_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 53
                self.table_declaration()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 54
                self.table_assignment()
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
            self.state = 57
            self.match(SimpleLangParser.T__0)
            self.state = 58
            self.boolean_expression(0)
            self.state = 59
            self.code_block()
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 60
                self.match(SimpleLangParser.T__1)
                self.state = 61
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
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.match(SimpleLangParser.T__2)
                self.state = 65
                self.match(SimpleLangParser.ID)
                self.state = 66
                self.match(SimpleLangParser.T__3)
                self.state = 67
                self.match(SimpleLangParser.NUMBER)
                self.state = 68
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(SimpleLangParser.T__5)
                self.state = 70
                self.match(SimpleLangParser.ID)
                self.state = 71
                self.match(SimpleLangParser.T__3)
                self.state = 72
                self.match(SimpleLangParser.FLOAT)
                self.state = 73
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.match(SimpleLangParser.T__6)
                self.state = 75
                self.match(SimpleLangParser.ID)
                self.state = 76
                self.match(SimpleLangParser.T__3)
                self.state = 77
                self.boolean_expression(0)
                self.state = 78
                self.match(SimpleLangParser.T__4)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 4)
                self.state = 80
                self.match(SimpleLangParser.T__7)
                self.state = 81
                self.match(SimpleLangParser.ID)
                self.state = 82
                self.match(SimpleLangParser.T__3)
                self.state = 83
                self.match(SimpleLangParser.STRING)
                self.state = 84
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


    class Table_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(SimpleLangParser.TypeContext,0)


        def NUMBER(self):
            return self.getToken(SimpleLangParser.NUMBER, 0)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def getRuleIndex(self):
            return SimpleLangParser.RULE_table_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_declaration" ):
                listener.enterTable_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_declaration" ):
                listener.exitTable_declaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_declaration" ):
                return visitor.visitTable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def table_declaration(self):

        localctx = SimpleLangParser.Table_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_table_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.type_()
            self.state = 88
            self.match(SimpleLangParser.T__8)
            self.state = 89
            self.match(SimpleLangParser.NUMBER)
            self.state = 90
            self.match(SimpleLangParser.T__9)
            self.state = 91
            self.match(SimpleLangParser.ID)
            self.state = 92
            self.match(SimpleLangParser.T__4)
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
        self.enterRule(localctx, 10, self.RULE_assignment)
        try:
            self.state = 108
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(SimpleLangParser.ID)
                self.state = 95
                self.match(SimpleLangParser.T__3)
                self.state = 96
                self.expression(0)
                self.state = 97
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.match(SimpleLangParser.ID)
                self.state = 100
                self.match(SimpleLangParser.T__3)
                self.state = 101
                self.boolean_expression(0)
                self.state = 102
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 104
                self.match(SimpleLangParser.ID)
                self.state = 105
                self.match(SimpleLangParser.T__3)
                self.state = 106
                self.match(SimpleLangParser.STRING)
                self.state = 107
                self.match(SimpleLangParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleLangParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,i)


        def getRuleIndex(self):
            return SimpleLangParser.RULE_table_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_assignment" ):
                listener.enterTable_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_assignment" ):
                listener.exitTable_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTable_assignment" ):
                return visitor.visitTable_assignment(self)
            else:
                return visitor.visitChildren(self)




    def table_assignment(self):

        localctx = SimpleLangParser.Table_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_table_assignment)
        self._la = 0 # Token type
        try:
            self.state = 132
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(SimpleLangParser.ID)
                self.state = 111
                self.match(SimpleLangParser.T__3)
                self.state = 112
                self.match(SimpleLangParser.T__8)
                self.state = 113
                self.expression(0)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 114
                    self.match(SimpleLangParser.T__10)
                    self.state = 115
                    self.expression(0)
                    self.state = 120
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 121
                self.match(SimpleLangParser.T__9)
                self.state = 122
                self.match(SimpleLangParser.T__4)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(SimpleLangParser.ID)
                self.state = 125
                self.match(SimpleLangParser.T__8)
                self.state = 126
                self.expression(0)
                self.state = 127
                self.match(SimpleLangParser.T__9)
                self.state = 128
                self.match(SimpleLangParser.T__3)
                self.state = 129
                self.expression(0)
                self.state = 130
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
        self.enterRule(localctx, 14, self.RULE_print_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(SimpleLangParser.T__11)
            self.state = 135
            self.match(SimpleLangParser.T__12)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 136
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 2:
                self.state = 137
                self.expression(0)
                pass

            elif la_ == 3:
                self.state = 138
                self.boolean_expression(0)
                pass

            elif la_ == 4:
                self.state = 139
                self.match(SimpleLangParser.STRING)
                pass


            self.state = 142
            self.match(SimpleLangParser.T__13)
            self.state = 143
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
        self.enterRule(localctx, 16, self.RULE_input_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(SimpleLangParser.ID)
            self.state = 146
            self.match(SimpleLangParser.T__3)
            self.state = 147
            self.match(SimpleLangParser.T__14)
            self.state = 148
            self.match(SimpleLangParser.T__12)
            self.state = 149
            self.match(SimpleLangParser.T__13)
            self.state = 150
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


    class TableElemContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SimpleLangParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SimpleLangParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(SimpleLangParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableElem" ):
                listener.enterTableElem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableElem" ):
                listener.exitTableElem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableElem" ):
                return visitor.visitTableElem(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SimpleLangParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 153
                self.match(SimpleLangParser.T__12)
                self.state = 154
                self.expression(0)
                self.state = 155
                self.match(SimpleLangParser.T__13)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(SimpleLangParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.FloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(SimpleLangParser.FLOAT)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.FuncCallNumContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 160
                self.func_call()
                pass

            elif la_ == 6:
                localctx = SimpleLangParser.TableElemContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(SimpleLangParser.ID)
                self.state = 162
                self.match(SimpleLangParser.T__8)
                self.state = 163
                self.expression(0)
                self.state = 164
                self.match(SimpleLangParser.T__9)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = SimpleLangParser.MulDivContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 169
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 170
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = SimpleLangParser.AddSubContext(self, SimpleLangParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 172
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        self.expression(8)
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_boolean_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = SimpleLangParser.BoolNegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 180
                self.match(SimpleLangParser.T__22)
                self.state = 181
                self.boolean_expression(6)
                pass

            elif la_ == 2:
                localctx = SimpleLangParser.BoolParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 182
                self.match(SimpleLangParser.T__12)
                self.state = 183
                self.boolean_expression(0)
                self.state = 184
                self.match(SimpleLangParser.T__13)
                pass

            elif la_ == 3:
                localctx = SimpleLangParser.BoolValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 186
                self.match(SimpleLangParser.BOOLEAN)
                pass

            elif la_ == 4:
                localctx = SimpleLangParser.BoolVariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.match(SimpleLangParser.ID)
                pass

            elif la_ == 5:
                localctx = SimpleLangParser.BoolCompareExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 188
                self.comparizon_expression()
                pass

            elif la_ == 6:
                localctx = SimpleLangParser.FuncCallBoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 189
                self.func_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 197
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = SimpleLangParser.BoolBinaryOpContext(self, SimpleLangParser.Boolean_expressionContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolean_expression)
                    self.state = 192
                    if not self.precpred(self._ctx, 7):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                    self.state = 193
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7340032) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 194
                    self.boolean_expression(8) 
                self.state = 199
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 22, self.RULE_comparizon_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.expression(0)
            self.state = 201
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 202
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
        self.enterRule(localctx, 24, self.RULE_loop_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(SimpleLangParser.T__29)
            self.state = 205
            self.boolean_expression(0)
            self.state = 206
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
        self.enterRule(localctx, 26, self.RULE_function_definition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(SimpleLangParser.T__30)
            self.state = 209
            self.type_()
            self.state = 210
            self.match(SimpleLangParser.ID)
            self.state = 211
            self.match(SimpleLangParser.T__12)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 456) != 0):
                self.state = 212
                self.parametr_list()


            self.state = 215
            self.match(SimpleLangParser.T__13)
            self.state = 216
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
        self.enterRule(localctx, 28, self.RULE_parametr_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.type_()
            self.state = 219
            self.match(SimpleLangParser.ID)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 220
                self.match(SimpleLangParser.T__10)
                self.state = 221
                self.type_()
                self.state = 222
                self.match(SimpleLangParser.ID)
                self.state = 228
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
        self.enterRule(localctx, 30, self.RULE_code_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(SimpleLangParser.T__31)
            self.state = 231 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 230
                self.statement()
                self.state = 233 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 155692569034) != 0)):
                    break

            self.state = 235
            self.match(SimpleLangParser.T__32)
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
        self.enterRule(localctx, 32, self.RULE_func_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(SimpleLangParser.ID)
            self.state = 238
            self.match(SimpleLangParser.T__12)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1030800547840) != 0):
                self.state = 239
                self.argument_list()


            self.state = 242
            self.match(SimpleLangParser.T__13)
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
        self.enterRule(localctx, 34, self.RULE_argument_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 244
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 245
                self.boolean_expression(0)
                pass


            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 248
                self.match(SimpleLangParser.T__10)
                self.state = 251
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 249
                    self.expression(0)
                    pass

                elif la_ == 2:
                    self.state = 250
                    self.boolean_expression(0)
                    pass


                self.state = 257
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
        self.enterRule(localctx, 36, self.RULE_return_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 258
            self.match(SimpleLangParser.T__33)
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 259
                self.expression(0)

            elif la_ == 2:
                self.state = 260
                self.boolean_expression(0)


            self.state = 263
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
        self.enterRule(localctx, 38, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
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
        self._predicates[9] = self.expression_sempred
        self._predicates[10] = self.boolean_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

    def boolean_expression_sempred(self, localctx:Boolean_expressionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         




