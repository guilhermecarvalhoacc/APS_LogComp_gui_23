%{
    #include <stdio.h>
    #include <string.h>
    #include "y.tab.h"
%}

%%

[ \t]                 ;

"="                     return TEQUAL;
"=="                    return EQUALEQUAL;
"<"                     return MENORQ;
"<="                    return MENORQEQ;
">"                     return MAIORQ;
">="                    return MAIORQEQ;
"("                     return OP;
")"                     return CP; 
"{"                     return OC;
"}"                     return CC;
"."                     return DOT;
","                     return VIRGULA;
"::"                    return DP;
"+"                     return PLUS;
"-"                     return MINUS;
"*"                     return MULT;
"/"                     return DIV;
"if"                    return SE;
"while"                 return CONTINUA;
"def"                   return RETORNA;
"return"                return FUNC;
"print"                 return MOSTRE;
[a-zA-Z_][a-zA-Z0-9_]*  return IDENTIFIER;
[0-9]+.[0-9]*           return FLOAT;
[0-9]+                  return INT;
"\n"                    return QUEBRALINHA;
.                       printf("Unknown token!n"); yyterminate();
%%
int yywrap(void) {
    return 1;
}