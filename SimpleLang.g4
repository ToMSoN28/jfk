grammar SimpleLang;

program: (function_definition | statement| struct_definition)+;

struct_definition: 'struct' ID '{' field_declaration+ '}' ';' ;
field_declaration: type ID ';';

statement: variable_declaration
         | assignment
         | print_statement
         | input_statement
         | if_statement
         | loop_while
         | loop_for_iterator
         | return_statement
         | table_declaration
         | table_assignment
         | matrix_declaration
         | matrix_assignment
         | matrix_element_assignment
         ;

if_statement: 'if' boolean_expression code_block ('else' code_block)? ;

variable_declaration: 'int' var_name=ID ('=' NUMBER)? ';'
                    | 'float' var_name=ID ('=' FLOAT)? ';'
                    | 'bool' var_name=ID ('=' boolean_expression)? ';'
                    | 'string' var_name=ID ('=' STRING)? ';'
                    | type_name=ID var_name=ID ';'
                    ;

table_declaration: type '[' NUMBER ']' ID ';' ;

assignment: struct_var=ID '.' field_name=ID '=' expression ';'
          |var_name=ID '=' expression ';'
          | var_name=ID '=' boolean_expression ';'
          | var_name=ID '=' STRING ';'
          ;

table_assignment: ID '=' '[' expression (',' expression)* ']' ';'                  
                | ID '[' expression ']' '=' expression ';'                         
                ;

matrix_declaration: type ID '[' NUMBER ']' '[' NUMBER ']' ('=' matrix_initializer)? ';' ;
matrix_initializer: '[' row_initializer (',' row_initializer)* ']' ;
row_initializer: '[' expression (',' expression)* ']' ;

matrix_assignment: ID '=' matrix_initializer ';' ;
matrix_element_assignment: ID '[' expression ']' '[' expression ']' '=' expression ';' ;


print_statement: 'print' '(' (ID | expression | boolean_expression | STRING ) ')' ';' ;

input_statement: ID '=' 'input' '(' ')' ';' ;

expression: expression op=('*'|'/') expression # MulDiv
          | expression op=('+'|'-') expression # AddSub
          | '(' expression ')'                             # ParensExpr  // Changed label
          | NUMBER                                         # NumberExpr  // Changed label
          | FLOAT                                          # FloatExpr   // Changed label
          | STRING                                         # StringExpr  // Changed label
          | ID                                             # VariableExpr// Changed label
          | func_call                                      # FuncCallExpr// Changed label
          | ID '[' expression ']'                          # TableElemExpr// Changed label
          | ID '[' expression ']' '[' expression ']'       # MatrixElemExpr// Changed label
          | expression '.' ID                              # StructMemberAccessExpr // Changed label
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

loop_for_iterator: 'for' ID ',' ID 'in' 'iterator' '(' ID ')' code_block ;

function_definition: 'func' type ID '(' parametr_list? ')' code_block ;

parametr_list: type ID (',' type ID)* ;

code_block: '{' statement+ '}' ;

func_call: ID '(' argument_list? ')' ;

argument_list: (expression | boolean_expression) (',' (expression | boolean_expression))* ;

return_statement: 'return' (expression | boolean_expression)? ';' ;

type: 'int' | 'float' | 'bool' | 'string' | ID;
STRING: '"' (~["\\] | '\\' .)* '"';
BOOLEAN: 'true' | 'false';
ID: [a-zA-Z][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;
SINGLE_LINE_COMMENT: '//' ~[\r\n]* -> skip;
MULTI_LINE_COMMENT: '/*' .*? '*/' -> skip;