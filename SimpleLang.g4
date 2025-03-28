grammar SimpleLang;

program: statement+;

statement: variable_declaration
         | assignment
         | print_statement
         | input_statement
         ;

variable_declaration: 'int' ID '=' NUMBER ';' 
                    | 'float' ID '=' FLOAT ';' ;

assignment: ID '=' expression ';' ;

print_statement: 'print' '(' expression ')' ';' ;

input_statement: ID '=' 'input' '(' ')' ';' ;

expression: expression op=('*'|'/') expression # MulDiv
          | expression op=('+'|'-') expression # AddSub
          | '(' expression ')'                  # Parens
          | NUMBER                               # Number
          | FLOAT                                # FloatNumber
          | ID                                   # Variable
          ;

ID: [a-zA-Z][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
WS: [ \t\r\n]+ -> skip;