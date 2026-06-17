# Strings in Python

## 1. What is a String?

In Python, a **String** is a data type used to represent textual data.  
It is fundamentally a sequential collection (or sequence) of Unicode characters.

Any data wrapped inside quotation marks—whether it is a single character, a word, or an entire paragraph—is treated natively as a string by Python.

---

## 2. Declaring Strings

You can define strings in Python using either single quotation marks (`'`) or double quotation marks (`"`). Both syntaxes behave identically.

```python
name = "Harry"
friend = 'Rohan'
another_friend = "Lovish"

print("Hello, " + name)
```

---

## Handling Internal Quotation Marks

If you need to include quote marks as literal text inside a string, you can mismatch your wrappers, or use an escape sequence (`\"`):

```python
# Option 1: Wrap double quotes inside single quotes
apple = 'He said, "I want to eat an apple."'
print(apple)

# Option 2: Use escape sequence characters
apple_escape = "He said, \"I want to eat an apple.\""
print(apple_escape)
```

---

## 3. Multiline Strings

If you try to write a string across multiple lines using a regular single or double quote, Python throws a syntax error:

`SyntaxError: EOL while scanning string literal`

To define a block of text spanning multiple lines, wrap it inside triple single quotes (`'''`) or triple double quotes (`"""`). This preserves all internal line breaks and formatting exactly as typed.

```python
conversation = """Hi Harry,
How are you?
I am doing good.
"""

print(conversation)
```

---

## 4. String Indexing & Accessing Characters

Because a string is an ordered sequence of characters, you can access specific characters individually using square brackets `[]` and their index number.

Python indexing starts at **0**.  
For a string of length N, valid indices range from `0` to `N-1`.

```python
name = "Harry"

print(name[0])  # H
print(name[1])  # a
print(name[2])  # r
```

---

## Index Out of Range Error

If you try to access an index that does not exist, Python raises an error:

```python
name = "Harry"

# print(name[5])  
# IndexError: string index out of range
```

---

## 5. Iterating Through Strings Using a For Loop

Instead of accessing characters one by one using indices, you can iterate through the string directly using a loop.

```python
name = "Harry"

print("Iterating through character elements:")

for character in name:
    print(character)
```

### Output
```
Iterating through character elements:
H
a
r
r
y
```