%{
#include <stdio.h>
#include <stdlib.h>

extern FILE *yyin;
%}

%%

// Sample conversions from Java to C#
"System.out.println"     { printf("Console.WriteLine"); }
"public"                 { printf("public "); }
"private"                { printf("private "); }
"protected"              { printf("protected "); }
"static"                 { printf("static "); }
"void"                   { printf("void "); }
"int"                    { printf("int "); }
"float"                  { printf("float "); }
"double"                 { printf("double "); }
"String"                 { printf("string "); }
";"                      { printf(";"); }
"{"                      { printf("{"); }
"}"                      { printf("}"); }
"("                      { printf("("); }
")"                      { printf(")"); }
"="                      { printf("="); }
"+"                      { printf("+"); }
"-"                      { printf("-"); }
"*"                      { printf("*"); }
"/"                      { printf("/"); }

[a-zA-Z_][a-zA-Z0-9_]*    { printf("%s ", yytext); }
[ \t]+                   { }         // Skip whitespace
\n                       { printf("\n"); }
.                        { printf("%s", yytext); }

%%

int main() {
    yyin = fopen("input.java", "r");
    if (!yyin) {
        fprintf(stderr, "Cannot open input.java\n");
        return 1;
    }
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}
