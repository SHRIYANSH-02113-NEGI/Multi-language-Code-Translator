import streamlit as st
import re

# Mapping of keywords/operators to replacements
replacements = {
    "var": "let",
    "let": "let",
    "const": "const",
    "function": "function",
    "class": "class",
    "constructor": "constructor",
    "this": "this",
    "super": "super",
    "extends": "extends",
    "console.log": "console.info",
    "==": "===",
    "!=": "!==",
    "=": "=",
    ";": ";",
    "=>": "=>",
    "import": "import",
    "export": "export",
    "from": "from",
    "default": "default",
    "interface": "interface",
    "type": "type",
    "enum": "enum",
    "readonly": "readonly",
    "number": "number",
    "string": "string",
    "boolean": "boolean",
    "any": "any",
    "??": "??",
    "?.": "?.",
    "(": "(",
    ")": ")",
    "{": "{",
    "}": "}"
}

# Build regex pattern that matches any of the keywords/operators or identifiers or numbers or strings
pattern = re.compile(
    r'''
    console\.log|==|!=|=>|\?\?|\?\.|   # multi-char operators/keywords first
    [a-zA-Z_][a-zA-Z0-9_]*|                # identifiers
    "[^"]*"|                             # double quoted strings
    '[^']*'|                               # single quoted strings
    [0-9]+\.[0-9]+|                       # float numbers
    [0-9]+|                                # integers
    [{}();=]                               # single-char punctuation/operators
    ''' ,
    re.VERBOSE,
)

def replace_token(token):
    # If token exactly matches a replacement key, replace it
    return replacements.get(token, token)

def process_line(line):
    result = []
    pos = 0
    for match in pattern.finditer(line):
        start, end = match.span()
        if start > pos:
            result.append(line[pos:start])
        token = match.group(0)
        result.append(replace_token(token))
        pos = end
    if pos < len(line):
        result.append(line[pos:])
    return ''.join(result)

# Streamlit UI wrapped in main

def main():
    st.title("JS to TypeScript Converter")
    js_code = st.text_area("Paste your JavaScript code here:", height=300)

    if st.button("Convert to TypeScript"):
        ts_lines = [process_line(line) for line in js_code.splitlines(keepends=True)]
        ts_code = ''.join(ts_lines)
        st.code(ts_code, language='typescript')

if __name__ == '__main__':
    main()
