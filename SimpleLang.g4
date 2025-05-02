grammar SimpleLang;

program: (function_definition | statement)+;

statement: variable_declaration
         | assignment
         | print_statement
         | input_statement
         | if_statement
         | loop_while
         | return_statement
         | table_declaration
         | table_assignment
         ;

if_statement: 'if' boolean_expression code_block ('else' code_block)? ;

variable_declaration: 'int' ID '=' NUMBER ';' 
                    | 'float' ID '=' FLOAT ';' 
                    | 'bool' ID '=' boolean_expression ';' 
                    | 'string' ID '=' STRING ';'
                    ;

table_declaration: type '[' NUMBER ']' ID ';' ;

assignment: ID '=' expression ';' 
          | ID '=' boolean_expression ';' 
          | ID '=' STRING ';'
          ;

table_assignment: ID '=' '[' expression (',' expression)* ']' ';'                  
                | ID '[' expression ']' '=' expression ';'                         
                ;

print_statement: 'print' '(' (ID | expression | boolean_expression | STRING ) ')' ';' ;

input_statement: ID '=' 'input' '(' ')' ';' ;

expression: expression op=('*'|'/') expression # MulDiv
          | expression op=('+'|'-') expression # AddSub
          | '(' expression ')'                  # Parens
          | NUMBER                               # Number
          | FLOAT                                # FloatNumber
          | ID                                   # Variable
          | func_call                            # FuncCallNum
          | ID '[' expression ']'                # TableElem
          ;

boolean_expression: boolean_expression op=('AND' | 'OR' | 'XOR') boolean_expression # BoolBinaryOp
                  | 'NEG' boolean_expression                                        # BoolNegation
                  | '(' boolean_expression ')'                                     # BoolParens
                  | BOOLEAN                                                        # BoolValue
                  | ID                                                             # BoolVariable
                  | comparizon_expression                                          # BoolCompareExpr
                  | func_call                                                      # FuncCallBool
                  ;

comparizon_expression: expression op=('>'|'<'|'=='|'!='|'<='|'>=') expression ;   

loop_while: 'while' boolean_expression code_block ;

function_definition: 'func' type ID '(' parametr_list? ')' code_block ;

parametr_list: type ID (',' type ID)* ;

code_block: '{' statement+ '}' ;

func_call: ID '(' argument_list? ')' ;

argument_list: (expression | boolean_expression) (',' (expression | boolean_expression))* ;

return_statement: 'return' (expression | boolean_expression)? ';' ;

type: 'int' | 'float' | 'bool' | 'string';
STRING: '"' (~["\\] | '\\' .)* '"';
BOOLEAN: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;