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
        |  '<!>' (printable)+                                                # wrt /* TODO: escriure moltes coses, lletra, llistes */
        |  '<?>'  VAR                                                      # read
        |  '<:>'  NOTE                                                     # repr /* TODO: llistes de notes */
        |  'if' cond '|:'  codeblock ':|' 'else' '|:' codeblock ':|'       # ifelse 
        |  'if'  cond  '|:'   codeblock  ':|'                              # if
        |  'while'  cond  '|:'   codeblock  ':|'                           # while
        /* | 'return' expr                                                 # ret TODO: afegir-ho */ 
        | FNME param                                                       # call
        ;

expr :
     '('  expr ')'           # par
    |  expr  DIV  expr       # div
    | expr  MULT  expr       # mult
    | expr  REM  expr        # rem
    | expr  ADD  expr        # add
    | expr  SUBS  expr       # sub
    | NUM                    # num
    | VAR                    # var
    ;

fheader :
    (VAR)* ;

param :
    (expr)*;

cond :  expr  COMP  expr  ;

printable : expr
            | STR;

STR : '"' (~[ \n\r])+ '"';

LN : '\n' | EOF;
VAR : [a-z][A-Za-z0-9]*;
FNME : [A-Z][A-Za-z0-9]*; /* TODO: distingir variables i funcions si o no */
NOTE: [A-C][0-8]; /* TODO: ferho be */
NUM : [0-9]+ ;


ADD : '+' ;
MULT : '*' ;
DIV : '/' ;
SUBS : '-' ;
REM : '%' ;
COMP : '=' | '<' | '>' | '/=' | '<=' | '>=' ;

WS : [ \n\t\r]+ -> skip ;

/* COMMENT : '~''~''~'~'~''~''~' -> skip; TODO */