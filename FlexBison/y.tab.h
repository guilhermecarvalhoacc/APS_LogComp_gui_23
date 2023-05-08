/* A Bison parser, made by GNU Bison 3.5.1.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2020 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* Undocumented macros, especially those whose name start with YY_,
   are private implementation details.  Do not rely on them.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    IDENTIFIER = 258,
    FLOAT = 259,
    INT = 260,
    TEQUAL = 261,
    EQUALEQUAL = 262,
    NadaVer = 263,
    MENORQ = 264,
    MENORQEQ = 265,
    MAIORQ = 266,
    MAIORQEQ = 267,
    OP = 268,
    CP = 269,
    OC = 270,
    CC = 271,
    DOT = 272,
    VIRGULA = 273,
    DP = 274,
    PLUS = 275,
    MINUS = 276,
    MULT = 277,
    DIV = 278,
    SE = 279,
    CONTINUA = 280,
    RETORNA = 281,
    FUNC = 282,
    MOSTRE = 283,
    QUEBRALINHA = 284
  };
#endif
/* Tokens.  */
#define IDENTIFIER 258
#define FLOAT 259
#define INT 260
#define TEQUAL 261
#define EQUALEQUAL 262
#define NadaVer 263
#define MENORQ 264
#define MENORQEQ 265
#define MAIORQ 266
#define MAIORQEQ 267
#define OP 268
#define CP 269
#define OC 270
#define CC 271
#define DOT 272
#define VIRGULA 273
#define DP 274
#define PLUS 275
#define MINUS 276
#define MULT 277
#define DIV 278
#define SE 279
#define CONTINUA 280
#define RETORNA 281
#define FUNC 282
#define MOSTRE 283
#define QUEBRALINHA 284

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
