import streamlit as st
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
    'final': '',  # no direct equivalent; we'll remove 'final'
    'null': 'null',
    'true': 'true',
    'false': 'false',
    'new': 'new',
    'this': 'this',
    'super': 'base',  # super in java -> base in C#
    'class': 'class',
    'interface': 'interface',
    'extends': ':',  # inheritance symbol in C#
    'implements': ',',  # interface implementation separator in C#
    'package': '',  # no direct equivalent, usually namespaces in C#; remove line usually
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
    'IDENTIFIER', 'NUMBER', 'STRING_LITERAL', 'CHAR_LITERAL', 'NEWLINE',
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
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'

t_EQ = r'='
t_EQEQ = r'=='
t_NEQ = r'!='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='

t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'

t_QUESTION = r'\?'
t_COLON = r':'

t_DOT = r'\.'
t_COMMA = r','
t_SEMICOLON = r';'

t_LPAREN = r'\('
t_RPAREN = r'\)'

t_LBRACE = r'\{'
t_RBRACE = r'\}'

t_LBRACKET = r'\['
t_RBRACKET = r'\]'

t_ignore = ' \t'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_STRING_LITERAL(t):
    r'\"([^\\n]|(\\.))*?\"'
    return t

def t_CHAR_LITERAL(t):
    r'\'([^\\n]|(\\.))*?\''
    return t

def t_NUMBER(t):
    r'(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    return t

def t_IDENTIFIER(t):
    r'[A-Za-z_][A-Za-z0-9_]*'
    val = t.value
    if val == 'System':  
        pos = t.lexpos
        remaining = t.lexer.lexdata[pos:]
        if remaining.startswith('.out.println'):
            t.value = 'Console.WriteLine'
            t.lexer.lexpos += len('.out.println')  
            return t
    if val in java_to_csharp_keywords:
        t.value = java_to_csharp_keywords[val]
        if t.value == '': 
            return None
    return t

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

def convert_java_to_csharp(java_code):
    lexer = lex.lex()
    lexer.input(java_code)

    result = []
    indentation = 0
    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == 'NEWLINE':
            result.append('\n' + '    ' * indentation) 
            continue

        if tok.type == 'LBRACE':  
            result.append(tok.value)
            indentation += 1
        elif tok.type == 'RBRACE': 
            indentation -= 1
            result.append('\n' + '    ' * indentation + tok.value)
        else:
            result.append(tok.value)

    return ''.join(result)

def main():
    st.title("Java to C# Converter")
    st.write("Enter your Java code below and get the converted C# code.")

    java_code = st.text_area("Java Code", height=300)
    
    if st.button("Convert"):
        if java_code.strip() == "":
            st.warning("Please enter some Java code to convert.")
        else:
            csharp_code = convert_java_to_csharp(java_code)
            st.text_area("Converted C# Code", value=csharp_code, height=300)

if __name__ == '__main__':
    main()