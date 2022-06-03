grammar jsbach;

root : 
        functions
        EOF
        ;

functions : func+ ;

func : FNME fheader '|:' codeblock  ':|' ;

codeblock : (line)*;

line : 
           VAR '<-' assignable                                             # assign
        |  VAR '[' expr ']' '<-' expr                                      # assignVectorPos
        |  '<!>' (printable)+                                              # wrt 
        |  '<?>' VAR                                                       # read
        |  '<:>' expr                                                      # repr
        |  '<:>' list                                                      # listrepr
        |  'if' expr '|:'  codeblock ':|' 'else' '|:' codeblock ':|'       # ifelse 
        |  'if'  expr  '|:'   codeblock  ':|'                              # if
        |  'while'  expr  '|:'   codeblock  ':|'                           # while
        |  VAR '<<' expr                                                   # append
        |  '8<' VAR '[' expr ']'                                           # delete
        |  'rück' expr                                                     # ret
        |  FNME param                                                      # call
        ;

expr :
     '('  expr ')'           # par
    | SUBS expr              # unarysub
    | '#' VAR                # listlength
    | VAR '[' expr ']'       # listaccess
    | expr  DIV  expr        # div
    | expr  MULT  expr       # mult
    | expr  REM  expr        # rem
    | expr  ADD  expr        # add
    | expr  SUBS  expr       # sub
    | expr COMP expr         # comparate 
    | NUM                    # num
    | VAR                    # var
    | NOTE                   # note
    | FNME param             # callInExpr
    ;

fheader :
    (VAR)* ;

param :
    (expr)*;

assignable : expr
            | list;

printable : expr
            | list
            | STR;

list : '{' (expr)* '}' ;


STR : '"' (~[\n\r"])+ '"';
NOTE: [A-B]'0'
    | [A-G][1-7]
    | [A-G]
    | 'C8' ;

VAR : [a-z][0-9a-zA-Z\u0080-\u00FF_]*;
FNME : [A-Z][0-9a-zA-Z\u0080-\u00FF_]*; 
NUM : [0-9]+| [0-9]+ ;

ADD : '+' ;
MULT : '*' ;
DIV : '/' ;
SUBS : '-' ;
REM : '%' ;
COMP : '=' | '<' | '>' | '/=' | '<=' | '>=' ;

WS : [ \n\t\r]+ -> skip ;

COMMENT : '~~~'(~[~])*'~~~' -> skip;