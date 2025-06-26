import streamlit as st
from app import convert_java_to_csharp
from pytoruby import translate_python_code
from jstots import process_line

# Conversion function wrappers
def convert_python_to_ruby(code: str) -> str:
    return translate_python_code(code)

def convert_java_to_csharp_wrapper(code: str) -> str:
    return convert_java_to_csharp(code)

def convert_js_to_ts(code: str) -> str:
    ts_lines = [process_line(line) for line in code.splitlines(keepends=True)]
    return ''.join(ts_lines)

# Main UI
def main():
    st.title("Multi-Language Code Converter")

    input_mode = st.radio("Input method:", ["Paste code", "Upload file"])

    user_code = ""
    if input_mode == "Paste code":
        user_code = st.text_area("Your code:", height=300)
    else:
        uploaded_file = st.file_uploader("Upload code file", type=["py", "java", "js", "txt"])
        if uploaded_file:
            user_code = uploaded_file.read().decode("utf-8")

    conversion_type = st.selectbox("Choose conversion:", ["Java → C#", "Python → Ruby", "JavaScript → TypeScript"])

    if st.button("Convert"):
        if not user_code.strip():
            st.warning("Please provide some code for conversion.")
        else:
            if conversion_type == "Java → C#":
                result = convert_java_to_csharp_wrapper(user_code)
                filename = "converted.cs"
                language = "csharp"

            elif conversion_type == "Python → Ruby":
                result = convert_python_to_ruby(user_code)
                filename = "translated.rb"
                language = "ruby"

            elif conversion_type == "JavaScript → TypeScript":
                result = convert_js_to_ts(user_code)
                filename = "converted.ts"
                language = "typescript"

            st.code(result, language=language)

            word_count = len(result.split())
            st.info(f"Words in converted code: {word_count}")

            st.download_button(
                label="Download converted code",
                data=result,
                file_name=filename,
                mime="text/plain"
            )

if __name__ == '__main__':
    main()
