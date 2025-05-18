"""
Java to C# converter using PLY (Python Lex-Yacc) lexer.

This lex program tokenizes Java code and outputs a converted C# version with basic keyword replacements and
some idiomatic changes like replacing System.out.println() with Console.WriteLine().

Usage:
    pip install ply
    python java2csharp.py &lt; input.java &gt; output.cs

Limitations:
- This is a lexer-only based simplistic converter; no full parsing or semantic conversion.
- It handles only a subset of Java features and keywords.
- Mainly demonstrates lexical scanning and token-based keyword replacement.

"""

import sys
import ply.lex as lex

# List of Java keywords we want to map/convert to C#
java_to_csharp_keywords = {
    'boolean': 'bool',
    'byte': 'byte',
    'char': 'char',
    'short': 'short',
    'int': 'int',
    'long': 'long',
    'float': 'float',
    'double': 'double',
    'void': 'void',
    'final': '',            # no direct equivalent; we'll remove 'final'
    'null': 'null',
    'true': 'true',
    'false': 'false',
    'new': 'new',
    'this': 'this',
    'super': 'base',        # super in java -> base in C#
    'class': 'class',
    'interface': 'interface',
    'extends': ':',         # inheritance symbol in C#
    'implements': ',',      # interface implementation separator in C#
    'package': '',          # no direct equivalent, usually namespaces in C#; remove line usually
    'import': 'using',
    'if': 'if',
    'else': 'else',
    'for': 'for',
    'while': 'while',
    'do': 'do',
    'switch': 'switch',
    'case': 'case',
    'default': 'default',
    'break': 'break',
    'continue': 'continue',
    'return': 'return',
}

# List of token names.
tokens = (
    'IDENTIFIER',
    'NUMBER',
    'STRING_LITERAL',
    'CHAR_LITERAL',
    'NEWLINE',

    # Operators and symbols
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'EQ', 'EQEQ', 'NEQ', 'LT', 'GT', 'LE', 'GE',
    'AND', 'OR', 'NOT',
    'INCREMENT', 'DECREMENT',
    'QUESTION', 'COLON',
    'DOT', 'COMMA', 'SEMICOLON',
    'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE',
    'LBRACKET', 'RBRACKET',
)

# Regular expressions for tokens
t_PLUS       = r'\+'
t_MINUS      = r'-'
t_TIMES      = r'\*'
t_DIVIDE     = r'/'
t_MOD        = r'%'

t_EQ         = r'='
t_EQEQ       = r'=='
t_NEQ        = r'!='
t_LT         = r'<'
t_GT         = r'>'
t_LE         = r'<='
t_GE         = r'>='

t_AND        = r'&&'
t_OR         = r'\|\|'
t_NOT        = r'!'

t_INCREMENT  = r'\+\+'
t_DECREMENT  = r'--'

t_QUESTION   = r'\?'
t_COLON      = r':'

t_DOT        = r'\.'
t_COMMA      = r','
t_SEMICOLON  = r';'

t_LPAREN     = r'\('
t_RPAREN     = r'\)'

t_LBRACE     = r'\{'
t_RBRACE     = r'\}'

t_LBRACKET   = r'\['
t_RBRACKET   = r'\]'

# Ignore whitespace (spaces and tabs) but keep newlines to preserve line endings
t_ignore  = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# String literal (double quotes), supports escaped quotes
def t_STRING_LITERAL(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# Char literal (single quotes), supports escaped chars
def t_CHAR_LITERAL(t):
    r'\'([^\\\n]|(\\.))*?\''
    return t

def t_NUMBER(t):
    r'(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    # Check if this identifier is a Java keyword to convert
    val = t.value
    if val == 'System':
        # Look ahead to see if next tokens are '.' 'out' '.' 'println'
        # If yes, then convert to Console.WriteLine
        # This is a simplified approach: check input starting at lexer position
        pos = t.lexpos
        remaining = t.lexer.lexdata[pos:]
        # Check for ".out.println"
        if remaining.startswith('.out.println'):
            # To consume '.out.println', advance lexer position
            # So next tokens will skip those characters
            # We'll print Console.WriteLine instead of "System.out.println"
            t.value = 'Console.WriteLine'
            # Mark to skip the characters '.out.println'
            t.lexer.lexpos += len('.out.println')
            return t
        else:
            # just System identifier
            t.value = val
            return t
    elif val in java_to_csharp_keywords:
        # Substitute keyword
        t.value = java_to_csharp_keywords[val]
        # If mapped keyword is empty string (like 'final', 'package'), skip token by returning None
        if t.value == '':
            # Ignore this token by returning None (removes it)
            return None
        return t
    else:
        return t

def t_COMMENT_SINGLELINE(t):
    r'//.*'
    # Echo comment as is
    return t

def t_COMMENT_MULTILINE(t):
    r'/\*(.|\n)*?\*/'
    # Echo comment as is
    return t

# Error handling rule
def t_error(t):
    # Output the illegal character and continue
    print(t.value[0], end='')
    t.lexer.skip(1)

def main():
    lexer = lex.lex()
    data = sys.stdin.read()
    lexer.input(data)

    # We'll reconstruct output by consuming tokens and printing mapped values or originals
    # Preserve formatting roughly by printing the value of tokens and newlines as they appear
    while True:
        tok = lexer.token()
        if not tok:
            break
        # Print token value or mapped value
        # Newline tokens just print newline
        if tok.type == 'NEWLINE':
            print('', end='\n')
            continue
        # Comments also print as is
        if tok.type == 'COMMENT_SINGLELINE' or tok.type == 'COMMENT_MULTILINE':
            print(tok.value, end='')
            continue

        # Normal tokens print their value
        print(tok.value, end='')

if __name__ == '__main__':
    main()
