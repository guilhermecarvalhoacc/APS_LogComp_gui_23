# Nordesthon

## *EBNF*

"Print" = Amostre 
"While" = ArrochaEnquanto
"IF" = SoSe
"Else" = SeNumFor
"Read" = DigaAi

BLOCK = { STATEMENT };

STATEMENT = ( λ | ASSIGNMENT | PRINT), "\n" ;

ASSIGNMENT = (IDENTIFIER, "=", RELEXPRESION) | (DP , TYPE) | "(" , ")" | "(", {"(", RELEXPRESSION, "VIRGULA"} , ")! ;

RETURN = ( "return", RELEXPRESSION, "\n" );

PRINT = "Amostre", "(", RELEXPRESSION, ")" ;

IF  = ("SoSe", RELEXPRESSION, "\n" , {STATEMENT}, ELSE) | ("IF", RELEXPRESSION, "\n" , {STATEMENT}, "end");

ELSE = ("SeNumFor" , "\n", {STATEMENT}, "end");

WHILE = ("ArrochaEnquanto", RELEXPRESSION, "\n", {STATEMENT}, "end");

FUNCTION = ("function", IDENTIFIER, "(", ")") | ("function", IDENTIFIER, "(", IDENTIFIER, "DP", TYPE, ("VIRGULA | ")")) , "DP", TYPE, "\n", {STATEMENT}, "end");

RELEXPRESSION = ( EXPRESSION, COMPARACAO );

RELEXPRESSION = EXPRESSION, { ( "==" | ">" | "<" ), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-" | "||" , "."), TERM } ;

TERM = FACTOR, { ("*" | "/", "&&"), FACTOR } ;

FACTOR = ("INT" | "STRING"  | (IDENTIFIER | IDENTIFIER, "(", {RELEXPRESSION, "VIRGULA"}, ")" ) | ( "+", FACTOR) | ( "-", FACTOR) | "!", FACTOR) | ( "DigaAi", "(", ")");

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

TYPE = ("Int" | "String") ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
