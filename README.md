# Nordesthon

## *EBNF*

"Print" = Amostre 

"While" = ArrochaEnquanto

"IF" = SoSe

"Else" = SeNumFor

"Read" = DigaAi

DECLARATION = ( "fn" , IDENTIFIER , "(" , ( IDENTIFIER, ( "," | ":") "TYPE", ",") | ")" , "->", TYPE, BLOCK);

BLOCK = {STATEMENT};

STATEMENT =  (IDENTIFIER | ("Amostre", "(", RELEXPRESSION, ")") | BLOCK | CONDITIONS | "retorne" , RELEXPRESSION);

CONDITIONS = ("SoSe", "(", RELEXPRESSION ,")", STATEMENT, (("SeNumFor", STATEMENT) | λ )) | ("ArrochaEnquanto", "(", RELEXPRESSION ,")", STATEMENT));

RELEXPRESSION = EXPRESSION , {("<" | ">" | "==") , EXPRESSION } ;

FACTOR = INT | STRING | IDENTIFIER_FACTOR | (( "+" | "-" | "!" ) , FACTOR) | "(" , RELEXPRESSION, ")" | READ, "(" , ")" ;

IDENTIFIER_FACTOR = ( λ | "(" , ( ")" | { RELEXPRESSION, "," }, ")" );

IDENTIFIER_STATEMENT = ( DECLARATION | ASSIGNMENT);

DECLARATION = ( "::", TYPE , ("=", RELEXPRESSION,"\n") | \n;

TYPE = "Int" | "String";

TERM = FACTOR, { ("*" | "/" | "&&"), FACTOR };

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM } ;

ASSIGNMENT = (IDENTIFIER, "=", RELEXPRESSION) | ( "(", { RELEXPRESSION, { "," | RELEXPRESSION } }, ")" );

READ = "DigaAi", "(" , ")" ;

VAR = ("Numero" | "Texto") , IDENTIFIER , (λ | {"," , IDENTIFIER });

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;

STRING = """, (LETTER | DIGIT), """;
