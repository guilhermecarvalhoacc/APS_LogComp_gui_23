# Nordesthon

## *EBNF*

"Print" = Amostre 
"While" = ArrochaEnquanto
"IF" = SoSe
"Else" = SeNumFor
"Read" = DigaAi

BLOCK = { STATEMENT };

STATEMENT = ( λ | ASSIGNMENT | PRINT), "\n" ;

ASSIGNMENT = (IDENTIFIER, "=", RELEXPRESION) | (DP , TYPE) | "(" , ")" | "(", {"(", RELEXPRESSION, "VIRGULA"} , ")" ;

RETURN = ( "Devolve", RELEXPRESSION, "\n" );

PRINT = "Amostre", "(", RELEXPRESSION, ")" ;

IF  = ("SoSe", RELEXPRESSION, "\n" , {STATEMENT}, ELSE) | ("IF", RELEXPRESSION, "\n" , {STATEMENT}, "FIM");

ELSE = ("SeNumFor" , "\n", {STATEMENT}, "FIM");

WHILE = ("ArrochaEnquanto", RELEXPRESSION, "\n", {STATEMENT}, "FIM");

FUNCTION = ("Trabalho", IDENTIFIER, "(", ")") | ("function", IDENTIFIER, "(", IDENTIFIER, "DP", TYPE, ("VIRGULA | ")")) , "DP", TYPE, "\n", {STATEMENT}, "FIM");

RELEXPRESSION = ( EXPRESSION, COMPARACAO );

RELEXPRESSION = EXPRESSION, { ( "==" | ">" | "<" ), EXPRESSION } ;

EXPRESSION = TERM, { ("+" | "-" | "||" , "."), TERM } ;

TERM = FACTOR, { ("*" | "/", "&&"), FACTOR } ;

FACTOR = ("INT" | "STRING"  | (IDENTIFIER | IDENTIFIER, "(", {RELEXPRESSION, "VIRGULA"}, ")" ) | ( "+", FACTOR) | ( "-", FACTOR) | "!", FACTOR) | ( "DigaAi", "(", ")");

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

TYPE = ("Int" | "Texto") ;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;





# Exemplo de codigo 

![image](https://github.com/guilhermecarvalhoacc/APS_LogComp_gui_23/assets/55805333/0ff4c7b6-b78c-46a2-b0d2-d9a65cb5d9d5)


