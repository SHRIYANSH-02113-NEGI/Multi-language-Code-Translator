%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern FILE *yyin;
%}

%option noyywrap

// Patterns for recognizing Java constructs

// Recognize class declarations
"public"[ \t]+"class"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"{" {
    char class_name[100];
    sscanf(yytext, "public class %s", class_name);
    char *brace_pos = strchr(class_name, '{');
    if (brace_pos) *brace_pos = '\0';
    printf("public class %s\n{\n", class_name);
}

"private"[ \t]+"class"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"{" {
    char class_name[100];
    sscanf(yytext, "private class %s", class_name);
    char *brace_pos = strchr(class_name, '{');
    if (brace_pos) *brace_pos = '\0';
    printf("private class %s\n{\n", class_name);
}

"protected"[ \t]+"class"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"{" {
    char class_name[100];
    sscanf(yytext, "protected class %s", class_name);
    char *brace_pos = strchr(class_name, '{');
    if (brace_pos) *brace_pos = '\0';
    printf("protected class %s\n{\n", class_name);
}

// Recognize method signatures
"public"[ \t]+"void"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"(" {
    char method_name[100];
    sscanf(yytext, "public void %s", method_name);
    char *paren_pos = strchr(method_name, '(');
    if (paren_pos) *paren_pos = '\0';
    printf("public void %s()\n{\n", method_name);
}

"private"[ \t]+"void"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"(" {
    char method_name[100];
    sscanf(yytext, "private void %s", method_name);
    char *paren_pos = strchr(method_name, '(');
    if (paren_pos) *paren_pos = '\0';
    printf("private void %s()\n{\n", method_name);
}

"protected"[ \t]+"void"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"(" {
    char method_name[100];
    sscanf(yytext, "protected void %s", method_name);
    char *paren_pos = strchr(method_name, '(');
    if (paren_pos) *paren_pos = '\0';
    printf("protected void %s()\n{\n", method_name);
}

"public"[ \t]+"static"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"(" {
    char return_type[50], method_name[100];
    sscanf(yytext, "public static %s %s", return_type, method_name);
    char *paren_pos = strchr(method_name, '(');
    if (paren_pos) *paren_pos = '\0';
    printf("public static %s %s()\n{\n", return_type, method_name);
}

// Recognize variable declarations
"private"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*";" {
    char type[50], var_name[50];
    sscanf(yytext, "private %s %s", type, var_name);
    if (strcmp(type, "String") == 0)
        printf("private string %s;\n", var_name);
    else
        printf("private %s %s;\n", type, var_name);
}

"public"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*";" {
    char type[50], var_name[50];
    sscanf(yytext, "public %s %s", type, var_name);
    if (strcmp(type, "String") == 0)
        printf("public string %s;\n", var_name);
    else
        printf("public %s %s;\n", type, var_name);
}

"protected"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*";" {
    char type[50], var_name[50];
    sscanf(yytext, "protected %s %s", type, var_name);
    if (strcmp(type, "String") == 0)
        printf("protected string %s;\n", var_name);
    else
        printf("protected %s %s;\n", type, var_name);
}

// Method call (very basic)
"printInfo()" {
    printf("    printInfo();\n");
}

// Recognize System.out.println
"System"[ \t]*"."[ \t]*"out"[ \t]*"."[ \t]*"println"[ \t]*"(" {
    printf("    Console.WriteLine(");
}

// Constructor
"public"[ \t]+[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"(" {
    char class_name[100];
    sscanf(yytext, "public %s", class_name);
    char *paren_pos = strchr(class_name, '(');
    if (paren_pos) *paren_pos = '\0';
    printf("public %s()\n{\n", class_name);
}

// Return, boolean, null, numbers
"return"        { printf("return "); }
"true"          { printf("true"); }
"false"         { printf("false"); }
"null"          { printf("null"); }
[0-9]+(\.[0-9]+)? { printf("%s", yytext); }

// Identifiers
[a-zA-Z_][a-zA-Z0-9_]* { printf("%s ", yytext); }

// String literal
\"([^\"\n]*)\" {
    char *str = strdup(yytext);
    for (int i = 0; str[i]; i++) {
        if (str[i] != ' ' || str[i] == '"')
            putchar(str[i]);
    }
    free(str);
}

// Assignment with 'this.'
"this"[ \t]*"."[ \t]*[a-zA-Z_][a-zA-Z0-9_]*[ \t]*"=" {
    printf("this.%s = ", yytext + 5);
}

// Braces, semicolons, newlines
"{"     { printf("{\n"); }
"}"     { printf("}\n"); }
";"     { printf(";\n"); }
\n      { printf("\n"); }

// Catch-all for other characters
.       { printf("%s", yytext); }

%%

int main() {
    yyin = fopen("javafile.java", "r");
    if (!yyin) {
        perror("Failed to open file");
        return 1;
    }
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}
