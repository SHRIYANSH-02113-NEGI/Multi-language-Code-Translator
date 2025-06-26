%{
#include <stdio.h>
#include <stdlib.h>
%}

%%

var                     { printf("let "); }
let                     { printf("let "); }
const                   { printf("const "); }
function                { printf("function "); }
class                   { printf("class "); }
constructor             { printf("constructor "); }
this                    { printf("this "); }
super                   { printf("super "); }
extends                 { printf("extends "); }
console.log             { printf("console.info "); }
==                      { printf("=== "); }
!=                      { printf("!== "); }
=                       { printf("= "); }
;                       { printf("; "); }
=>                      { printf("=> "); }
import                  { printf("import "); }
export                  { printf("export "); }
from                    { printf("from "); }
default                 { printf("default "); }
interface               { printf("interface "); }
type                    { printf("type "); }
enum                    { printf("enum "); }
readonly                { printf("readonly "); }
number                  { printf("number "); }
string                  { printf("string "); }
boolean                 { printf("boolean "); }
any                     { printf("any "); }
\?\?                    { printf("?? "); }
\?\.\                   { printf("?. "); }
[(]                     { printf("( "); }
[)]                     { printf(") "); }
[{]                     { printf("{ "); }
[}]                     { printf("} "); }
[0-9]+\.[0-9]+          { printf("%s ", yytext); }
[0-9]+                  { printf("%s ", yytext); }
\"[^\"]*\"              { printf("%s ", yytext); }
\'[^\']*\'              { printf("%s ", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("%s ", yytext); }
[ \t]+                  ; 
\n                      { printf("\n"); } 
.                       { printf("%s ", yytext); }

%%
int main() {
    yyin = fopen("javascript.js", "r");  
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}