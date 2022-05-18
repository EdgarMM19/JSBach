grammar jsbach;

/* todo: llistes i musica */
/* todo: pensar sobre els salts de linea */
root : 
        functions
        EOF
        ;

functions : func+ ;

func : FNME fheader '|:' codeblock  ':|' ;

codeblock : (line)+;

line : 
           VAR  '<-'  expr                                                 # assign /* TODO: LLISTES */
        |  '<!>' (printable)+                                              # wrt /* TODO: llistes */
        |  '<?>' VAR                                                       # read
        |  '<:>' expr                                                      # repr /* TODO: llistes de notes */
        |  'if' cond '|:'  codeblock ':|' 'else' '|:' codeblock ':|'       # ifelse 
        |  'if'  cond  '|:'   codeblock  ':|'                              # if
        |  'while'  cond  '|:'   codeblock  ':|'                           # while
        /* | 'return' expr                                                 # ret TODO: afegir-ho */ 
        | FNME param                                                       # call
        ;

expr :
     '('  expr ')'           # par
    | expr  DIV  expr       # div
    | expr  MULT  expr       # mult
    | expr  REM  expr        # rem
    | expr  ADD  expr        # add
    | expr  SUBS  expr       # sub
    | NUM                    # num
    | VAR                    # var
    | NOTE                   # note
    ;

fheader :
    (VAR)* ;

param :
    (expr)*;

cond :  expr  COMP  expr  ;

printable : expr
            | STR;

STR : '"' (~[\n\r"])+ '"';
NOTE: [A-B]'0'
    | [A-G][1-7]
    | [A-G]
    | 'C8' ;

LN : '\n' | EOF;
VAR : [a-z][A-Za-z0-9]*;
FNME : [A-Z][A-Za-z0-9]*; 
NUM : [0-9]+ ; /* todo: add negative numbers? */


ADD : '+' ;
MULT : '*' ;
DIV : '/' ;
SUBS : '-' ;
REM : '%' ;
COMP : '=' | '<' | '>' | '/=' | '<=' | '>=' ;

WS : [ \n\t\r]+ -> skip ;

COMMENT : '~''~''~' (~[~])* '~''~''~' -> skip;