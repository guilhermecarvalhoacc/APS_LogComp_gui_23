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
    INT = 258,
    PLUS = 259,
    MINUS = 260,
    MULT = 261,
    DIV = 262,
    OP = 263,
    CP = 264,
    OC = 265,
    CC = 266,
    EQUAL = 267,
    IDENTIFIER = 268,
    QUEBRALINHA = 269,
    EQUALEQUAL = 270,
    MAIORQ = 271,
    MENORQ = 272,
    AND = 273,
    OR = 274,
    NOT = 275,
    DOT = 276,
    STRING = 277,
    VIRGULA = 278,
    DOISPONTOS = 279,
    VARTYPE = 280,
    READ = 281,
    PRINT = 282,
    IF = 283,
    ELSE = 284,
    PV = 285,
    WHILE = 286,
    RETURN = 287
  };
#endif
/* Tokens.  */
#define INT 258
#define PLUS 259
#define MINUS 260
#define MULT 261
#define DIV 262
#define OP 263
#define CP 264
#define OC 265
#define CC 266
#define EQUAL 267
#define IDENTIFIER 268
#define QUEBRALINHA 269
#define EQUALEQUAL 270
#define MAIORQ 271
#define MENORQ 272
#define AND 273
#define OR 274
#define NOT 275
#define DOT 276
#define STRING 277
#define VIRGULA 278
#define DOISPONTOS 279
#define VARTYPE 280
#define READ 281
#define PRINT 282
#define IF 283
#define ELSE 284
#define PV 285
#define WHILE 286
#define RETURN 287

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
