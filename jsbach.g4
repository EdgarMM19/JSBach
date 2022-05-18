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
        |  '<!>' (printable)+                                              # wrt 
        |  '<?>' VAR                                                       # read
        |  '<:>' expr                                                      # repr
        |  '<:>' list                                                      # listrepr
        |  'if' cond '|:'  codeblock ':|' 'else' '|:' codeblock ':|'       # ifelse 
        |  'if'  cond  '|:'   codeblock  ':|'                              # if
        |  'while'  cond  '|:'   codeblock  ':|'                           # while
        |  VAR '<<' expr                                                   # append
        |  '8<' VAR '[' expr ']'                                           # delete
        /* | 'return' expr                                                 # ret TODO: afegir-ho */ 
        | FNME param                                                       # call
        ;

expr :
     '('  expr ')'           # par
    | '#' VAR                # listlength
    | VAR '[' expr ']'       # listaccess
    | expr  DIV  expr        # div
    | expr  MULT  expr       # mult
    | expr  REM  expr        # rem
    | expr  ADD  expr        # add
    | expr  SUBS  expr       # sub
    | SUBS expr              # unarysub
    | NUM                    # num
    | VAR                    # var
    | NOTE                   # note
    ;

fheader :
    (VAR)* ;

param :
    (expr)*;

cond :  expr  COMP  expr  ;

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

LN : '\n' | EOF;
VAR : [a-z][A-Za-z0-9_]*;
FNME : [A-Z][A-Za-z0-9_]*; 
NUM : '-'[0-9]+| [0-9]+ ;


ADD : '+' ;
MULT : '*' ;
DIV : '/' ;
SUBS : '-' ;
REM : '%' ;
COMP : '=' | '<' | '>' | '/=' | '<=' | '>=' ;

WS : [ \n\t\r]+ -> skip ;

COMMENT : '~''~''~' (~[~])* '~''~''~' -> skip;