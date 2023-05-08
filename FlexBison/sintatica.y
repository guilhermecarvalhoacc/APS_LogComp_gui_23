%{
  #include<stdio.h>
  int yylex();
  void yyerror(const char *s) { printf("ERROR: %s\n", s); }
%}


%token IDENTIFIER
%token FLOAT
%token INT
%token TEQUAL
%token EQUALEQUAL
%token NadaVer
%token MENORQ
%token MENORQEQ
%token MAIORQ
%token MAIORQEQ
%token OP
%token CP
%token OC
%token CC
%token DOT
%token VIRGULA
%token DP
%token PLUS
%token MINUS
%token MULT
%token DIV
%token SE
%token CONTINUA
%token RETORNA
%token FUNC
%token MOSTRE
%token QUEBRALINHA
%start block

%%

block : statement
      | statement block;    

statement : assignment | return_statement QUEBRALINHA
          | print_statement
          | if_statement
          | while_statement
          QUEBRALINHA
          ;

print_statement : MOSTRE OP expression CP;

while_statement : CONTINUA 
                | COMP_EQEQ
                | COMP_MAIORQE
                | COMP_MQ
                | COMP_MENORQE
                | COMP_MENORQ
                DP block
             ;


COMP_STATE : COMP_EQEQ
                      | COMP_MAIORQE
                      | COMP_MQ
                      | COMP_MENORQE
                      | COMP_MENORQ
                      ;

if_statement : SE COMP_STATE DP block;

assignment : identifier TEQUAL expression
           | identifier TEQUAL expression OP CP 

return_statement : RETORNA expression;

expression : term
           | term MINUS term
           | term PLUS term
           ;

term : factor
     | factor DIV factor
     | factor MULT factor
     ;

factor : MINUS factor
       | PLUS factor
       | number
       | OP expression CP
       | identifier
       ;

identifier : IDENTIFIER;
number : INT;


COMP_EQEQ: expression EQUALEQUAL expression;
COMP_MAIORQE: expression MAIORQEQ expression;
COMP_MQ: expression MAIORQ expression; 
COMP_MENORQE: expression MENORQEQ expression; 
COMP_MENORQ: expression MENORQ expression; 

%%

int main(){
  yyparse();
  return 0;
}