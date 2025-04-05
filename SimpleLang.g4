grammar SimpleLang;

program: statement+;

statement: variable_declaration
         | assignment
         | print_statement
         | input_statement
         ;

variable_declaration: 'int' ID '=' int_expression ';' 
                    | 'float' ID '=' float_expression ';' 
                    | 'bool' ID '=' boolean_expression ';' ;

assignment: ID '=' float_expression ';' 
          | ID '=' int_expression ';' 
          | ID '=' boolean_expression ';' ;

print_statement: 'print' '(' (float_expression | int_expression | boolean_expression) ')' ';' ;

input_statement: ID '=' 'input' '(' ')' ';' ;

int_expression: int_expression op=('*'|'/') int_expression # MulDivInt
          | int_expression op=('+'|'-') int_expression # AddSubInt
          | '(' int_expression ')'                  # ParensInt
          | NUMBER                               # Number
          | ID                                   # VariableInt
          ;

float_expression: float_expression op=('*'|'/') float_expression # MulDivFloat
          | float_expression op=('+'|'-') float_expression # AddSubFloat
          | '(' float_expression ')'                  # ParensFloat
          | FLOAT                                # FloatNumber
          | ID                                   # VariableFloat
          ;

boolean_expression: boolean_expression op=('AND' | 'OR' | 'XOR') boolean_expression # BoolBinaryOp
                  | 'NEG' boolean_expression                                        # BoolNegation
                  | '(' boolean_expression ')'                                     # BoolParens
                  | BOOLEAN                                                        # BoolValue
                  | ID                                                             # BoolVariable
                  ;

BOOLEAN: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;