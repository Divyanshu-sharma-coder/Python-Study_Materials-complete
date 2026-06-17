# Docstrings and PEP 8 in Python

Both **Docstrings** and **PEP 8** are fundamental concepts in Python. They are frequently asked about in technical interviews because they assess your knowledge of writing maintainable, clean, and professional Python code.

---

## 1. Python Docstrings (Documentation Strings)

Python docstrings are string literals that appear **immediately after** the definition of a function, method, class, or module. They are specifically designed to document what the component does.

---

## Core Syntax and Positioning

A docstring must be placed on the very first line below the component's declaration.

```python
def square(n):
    """Takes in a number n and returns its square."""
    print(n ** 2)

square(5)

# Output:
# 25
```

---

## Docstrings vs Comments

Although docstrings and comments may look similar, Python treats them differently.

### Comments (`#`)

- Used for notes and explanations.
- Ignored by the Python interpreter.
- Not stored anywhere in memory.

```python
# This is a comment
print("Hello World")
```

### Docstrings (`""" """`)

- Used for documentation.
- Stored by Python at runtime.
- Accessible through the `.__doc__` attribute.

```python
def square(n):
    """Takes in a number n and returns its square."""
    print(n ** 2)

print(square.__doc__)

# Output:
# Takes in a number n and returns its square.
```

---

## Accessing Docstrings Dynamically

Python automatically stores valid docstrings inside the `__doc__` attribute.

```python
def greet(name):
    """Greets the user by name."""
    return f"Hello, {name}"

print(greet.__doc__)

# Output:
# Greets the user by name.
```

---
# Important *
## Invalid Docstring Positioning

A docstring must appear immediately after the function definition.

Incorrect example:

```python
def square(n):
    print(n)
    """Takes in a number n and returns its square."""
    print(n ** 2)

print(square.__doc__)

# Output:
# None
```

### Why Does This Happen?

Because Python only treats the **first statement** after the function declaration as a docstring.

Since `print(n)` comes first, the string is treated as a normal string literal and ignored.

---

## 2. PEP 8 (Python Enhancement Proposal)

PEP 8 is Python's official style guide.

It was written by:

- Guido van Rossum
- Barry Warsaw
- Nick Coghlan

---

## What Does PEP Stand For?

**PEP = Python Enhancement Proposal**

PEP 8 specifically defines conventions and best practices for writing Python code.

---

## Goals of PEP 8

- Improve readability
- Maintain consistency
- Make collaboration easier
- Create a common coding standard

---

## Common PEP 8 Guidelines

### Use 4 Spaces for Indentation

```python
def greet():
    print("Hello")
```

### Use Meaningful Variable Names

```python
student_name = "Harry"
student_age = 20
```

### Add Spaces Around Operators

```python
x = 10 + 20
```

Instead of:

```python
x=10+20
```

### Limit Line Length

Recommended:

```python
maximum_line_length = 79
```

---

## 3. The Zen of Python

Python contains a famous Easter egg called **The Zen of Python**.

It was written by **Tim Peters** and contains guiding principles for writing good software.

You can display it using:

```python
import this
```

---

## Output

```text
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

---

## Why The Zen of Python Matters

These principles influence:

- PEP 8
- Python libraries
- Software design decisions
- Clean coding practices

One of the most famous lines is:

> Readability counts.

This idea is at the heart of Python's philosophy.

---

## Summary

| Term | Purpose | Technical Behavior |
|--------|---------|-------------------|
| Docstring | Documents functions, classes, methods, and modules | Stored in `.__doc__` and available at runtime |
| Comment | Developer notes and explanations | Ignored by Python |
| PEP 8 | Official Python style guide | Defines coding standards and conventions |
| `import this` | Displays The Zen of Python | Built-in Easter egg showing Python philosophy |

---

## Key Takeaway

Docstrings help document your code and are accessible at runtime through the `__doc__` attribute. Comments are ignored by Python and serve only as notes for developers. PEP 8 provides a standard set of style guidelines that make Python code more readable, maintainable, and professional. The Zen of Python captures the philosophy behind these conventions and serves as a guide for writing elegant software.