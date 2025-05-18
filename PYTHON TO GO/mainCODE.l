%{
#include <stdio.h>
#include <stdlib.h>

extern FILE *yyin;
%}

%%

self                                               { printf("self "); }
pass                                               { printf("# pass\n"); }
True                                               { printf("true "); }
False                                              { printf("false "); }
None                                               { printf("nil "); }
def[ \t]+[a-zA-Z_][a-zA-Z0-9_]*\(.*\):             { printf("def %s\n", yytext); }
class[ \t]+[a-zA-Z_][a-zA-Z0-9_]*:                 { printf("class %s\n", yytext); }
print[ \t]*[(]                                     { printf("puts "); }
input[(][)]                                        { printf("gets.chomp "); }
len[(]                                             { /* skip len( */ }
[)]                                                { printf(".length "); }
if[ \t]+.*:                                        { printf("if "); }
elif[ \t]+.*:                                      { printf("elsif "); }
else:                                              { printf("else "); }
for[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]+in[ \t]+.*:    { printf("for %s in ", yytext); }
while[ \t]+.*:                                     { printf("while "); }
and                                                { printf("&& "); }
or                                                 { printf("|| "); }
not                                                { printf("! "); }
is                                                 { printf("== "); }
[ \t]+in[ \t]+                                     { printf(".include? "); }
\+=                                                { printf("+= "); }
-=                                                 { printf("-= "); }
\*=                                                { printf("*= "); }
\/=                                                { printf("/= "); }
\*\*=                                              { printf("**= "); }
\"[^\"]*\"                                         { printf("%s ", yytext); }
\'[^\']*\'                                         { printf("%s ", yytext); }
[0-9]+(\.[0-9]+)?                                  { printf("%s ", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*                             { printf("%s ", yytext); }
[ \t]+                                             ;
\n                                                 { printf("\n"); }
.                                                  { printf("%s ", yytext); }

%%

int main() {
    yyin = fopen("python.py", "r");
   

    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}
