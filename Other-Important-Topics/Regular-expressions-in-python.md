# Regular Expressions (RegEx) in Python

## 1. What are Regular Expressions?

A Regular Expression (RegEx) is a powerful sequence of characters used to define a **search pattern**.

It is used for:
- Searching text
- Extracting data
- Validating patterns
- Replacing substrings

---

## Python Support

Python provides RegEx support using the built-in module:

```python
import re
```

---

## When to Use RegEx?

### ✔ Use basic string methods when:
- Checking simple substrings

```python
"was" in text
```

---

### ✔ Use RegEx when:
- Patterns are complex
- Structure matters (not exact words)

Examples:
- Emails
- Phone numbers
- URLs
- Structured text extraction

---

## 2. Fundamental Functions in `re` Module

---

## A. `re.search()`

Searches the **first occurrence** of a pattern in a string.

### Example

```python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = "fox"

match = re.search(pattern, text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
```

---

## B. `re.finditer()`

Returns an iterator containing **all matches** in a string.

It also provides:
- Start index
- End index
- Match object details

---

### Example

```python
import re

text = "Cyclone, Dyclone, and Gyclone caused disruptions."

pattern = r"[A-Z]yclone"

matches = re.finditer(pattern, text)

for match in matches:
    print("Match object:", match)
    print("Span:", match.span())

    start, end = match.span()
    print("Extracted word:", text[start:end])
```

---

## 3. Metacharacters & Character Classes

Metacharacters are special symbols used to build patterns.

---

## Common RegEx Symbols

| Symbol | Meaning | Example |
|:------:|:--------|:--------|
| `[ ]` | Character class (any one character inside) | `[A-Z]` |
| `+` | One or more repetitions | `\w+` |
| `.` | Any character except newline | `a.b` |
| `\w` | Word character (a-z, A-Z, 0-9, _) | `\w+` |

---

## Example Patterns

### ✔ Uppercase Words

```python
[A-Z]yclone
```

Matches:
- Cyclone
- Dyclone
- Gyclone

---

### ✔ Word Pattern

```python
\w+
```

Matches:
- Any full word
- Numbers + letters + underscore

---

## 4. Raw Strings (`r""`)

In RegEx, backslashes are common.

So Python uses raw strings:

```python
r"\w+"
```

### Why?

Without raw string:

```
"\n" → newline
```

With raw string:

```
r"\n" → literal backslash + n
```

---

## 5. Useful RegEx Testing Tools

✔ regexr.com  
✔ regex101.com  

These tools help you:
- Visualize patterns
- Debug expressions
- Understand matching step-by-step

---

## 6. Official Documentation

📘 Python `re` module reference:
```
https://docs.python.org/3/library/re.html
```

---

## Final Idea

RegEx is a **pattern-matching engine** that allows Python to move from simple string operations to powerful text processing and data extraction.