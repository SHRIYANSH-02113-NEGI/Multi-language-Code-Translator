# 🔁 Multilanguage Code Translator Using Lex and Python

## 👋 Introduction

As programming ecosystems evolve, developers often need to **migrate code between languages** — whether to meet platform requirements, optimize performance, or modernize legacy systems.  
This project provides a **Multilanguage Code Translator** that bridges this gap by enabling **automatic source code conversion** between popular languages.

Leveraging the power of **Lex (Lexical Analyzer Generator)** and **Python**, the tool supports translation between:

- 🐍 **Python → Ruby**
- ☕ **Java → C#**
- 🌐 **JavaScript → TypeScript**

This cross-language translator aims to preserve **semantic accuracy** and **coding conventions**, making it useful for students, developers, and teams adopting new technologies.

---

## 🧠 Project Motivation

Language syntax may differ, but many programming languages share **common structures** like conditionals, loops, functions, and object-oriented principles.

Manual translation of code is time-consuming and error-prone. This tool **automates the translation**, ensuring syntactic correctness and efficient adaptation across languages.

---

## 🔍 Target Languages

### 1. 🐍 Python → 💎 Ruby

| Feature          | Python              | Ruby               |
|------------------|---------------------|--------------------|
| Function Syntax  | `def func():`       | `def func`         |
| Blocks           | Indentation-based   | `do...end`         |
| Print Statement  | `print()`           | `puts`             |

---

### 2. ☕ Java → 💠 C#

| Feature           | Java                          | C#                            |
|------------------|-------------------------------|-------------------------------|
| Entry Point       | `public static void main()`   | `static void Main()`          |
| Classes           | `class`                       | `class`                       |
| Keywords          | `boolean`, `final`, etc.      | `bool`, `readonly`, etc.      |

---

### 3. 🌐 JavaScript → 📘 TypeScript

| Feature           | JavaScript                | TypeScript                    |
|------------------|---------------------------|-------------------------------|
| Typing           | Dynamic                   | Static                        |
| Variable Decl.   | `var`, `let`, `const`     | `let`, `const: type`          |
| Functions        | Anonymous & Named         | Typed Functions               |

---

## 🛠️ Architecture

### 🔹 Lex (Lexical Analyzer)

Lex is used to **tokenize** input code, identifying keywords, symbols, identifiers, and patterns.  
Each source language has its own `.l` file (e.g., `java_to_csharp.l`).

### 🔹 Python Backend

Python handles:

- Parsing tokens
- Applying transformation rules
- Generating output code
- Optional GUI via **Streamlit**

---

## 📁 File Structure


---

## 🔧 Technologies Used

- 💻 **Lex (Flex)** – For lexical analysis and token generation
- 🐍 **Python 3.x** – For rule-based transformation and output handling
- 🧪 **PLY** – Python Lex-Yacc (optional, for advanced parsing)
- 🖼️ **Streamlit** – For GUI interface (optional)
- 📝 **Regex** – To pattern-match language syntax

---

## 📌 Assumptions

- ✅ Input code is **syntactically correct**
- ✅ Focused on **core language constructs** (not full libraries)
- ✅ One language conversion per execution
- ✅ Output is **readable and maintainable**
- ✅ Python 3.x environment is set up correctly

---

## 🎯 Sample Use Cases

- 🔄 Migrate Java code to C# for .NET backend
- 🔄 Convert Python scripts to Ruby for Rails integration
- 🔄 Transform JavaScript into TypeScript for typed frontend frameworks

---

## 💡 Key Features

- ⚡ Real-time Code Translation
- 📂 Supports Multiple Language Pairs
- 🧠 Preserves Logic and Comments
- 🔁 Easy to Add New Language Pairs
- 🎨 Optional Streamlit GUI

---

## ✅ Project Impact

This project showcases practical applications of **compiler design** principles such as **lexical analysis**, **token parsing**, and **language syntax mapping**.  
It serves as a robust tool for cross-platform development and demonstrates the power of **automated source code transformation**.

---

## 🚀 How to Run

### CLI Mode

```bash
make
python parser.py --input examples/sample_java.java --mode java_to_csharp
