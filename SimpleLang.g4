grammar SimpleLang;

program: statement+;

statement: variable_declaration
         | assignment
         | print_statement
         | input_statement
         | if_statement
         ;

if_statement: 'if' boolean_expression code_block ('else' code_block)? ;

variable_declaration: 'int' ID '=' NUMBER ';' 
                    | 'float' ID '=' FLOAT ';' 
                    | 'bool' ID '=' boolean_expression ';' ;

assignment: ID '=' expression ';' 
          | ID '=' boolean_expression ';' ;

print_statement: 'print' '(' (expression | boolean_expression) ')' ';' ;

input_statement: ID '=' 'input' '(' ')' ';' ;

expression: expression op=('*'|'/') expression # MulDiv
          | expression op=('+'|'-') expression # AddSub
          | '(' expression ')'                  # Parens
          | NUMBER                               # Number
          | FLOAT                                # FloatNumber
          | ID                                   # Variable
          ;

boolean_expression: boolean_expression op=('AND' | 'OR' | 'XOR') boolean_expression # BoolBinaryOp
                  | 'NEG' boolean_expression                                        # BoolNegation
                  | '(' boolean_expression ')'                                     # BoolParens
                  | BOOLEAN                                                        # BoolValue
                  | ID                                                             # BoolVariable
                  | comparizon_expression                                          # BoolCompareExpr
                  ;

comparizon_expression: expression op=('>'|'<'|'=='|'!='|'<='|'>=') expression ;         

code_block: '{' statement+ '}' ;

BOOLEAN: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;