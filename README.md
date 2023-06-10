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

Trabalho soma(x::Int, y::Int)::Int
  Devolva x + y
FIM

x_1::Int
x_1 = 2
x_1 = soma(1, x_1)

x_1 = Leia()
SoSe ((x_1 > 1) && !(x_1 < 1)) 
  x_1 = 3
SeNumFor 
  
  x_1 = (-20+30)*4*3/40 # teste de comentario
  
FIM
Amostre(x_1)
x_1 = Leia()
SoSe ((x_1 > 1) && !(x_1 < 1))
  x_1 = 3
SeNumFor
  x_1 = (-20+30)*12/40
FIM
Amostre(x_1)
ArrochaEnquanto ((x_1 > 1) || (x_1 == 1)) 
  x_1 = x_1 - 1
  Amostre(x_1)
FIM
