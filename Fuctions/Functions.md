# Functions in Python

## 1. What is a Function?

A **function** is a reusable block of code that performs a specific task.

Instead of repeating the same logic again and again, you define it once and call it whenever needed.

---

## Core Idea (DRY Principle)

```
DRY = Don't Repeat Yourself
```

---

## Why Functions are Important?

✔ Code reusability  
✔ Easy debugging  
✔ Better structure  
✔ Modular programming  

---

## Real-world analogy

A function is like a **machine**:

```
Input → Processing → Output
```

You don’t rebuild the machine every time — you just reuse it.

---

## 2. Types of Functions in Python

---

## A. Built-in Functions

These are already provided by Python.

### Examples:

```python
print()
len()
max()
min()
sum()
type()
```

---

## B. User-defined Functions

These are created by programmers using `def`.

---

## 3. Creating a Function

---

## Syntax

```python
def function_name(parameters):
    # function body
    pass
```

---

## Important Rules

✔ Use `def` keyword  
✔ Function name must be meaningful  
✔ Indentation is mandatory  
✔ Colon `:` is required  

---

## 4. The `pass` Statement

If you want to create an empty function:

```python
def my_function():
    pass
```

---

## Why use `pass`?

✔ Avoids indentation errors  
✔ Acts as a placeholder  
✔ Useful during planning phase  

---

## 5. Example 1: Geometric Mean

```python
def calculate_gmean(a, b):
    mean = (a * b) / (a + b)
    print("Geometric Mean:", mean)


calculate_gmean(9, 8)
calculate_gmean(8, 7)
```

---

## Output Idea

```
Geometric Mean: 4.21
Geometric Mean: 3.73
```

---

## 6. Example 2: Number Comparison

```python
def is_greater(a, b):
    if a > b:
        print("First number is greater")
    elif a < b:
        print("Second number is greater")
    else:
        print("Both are equal")


is_greater(9, 8)
is_greater(5, 22)
is_greater(10, 10)
```

---

## Output

```
First number is greater
Second number is greater
Both are equal
```

---

## 7. How Function Execution Works

```
Function defined → Function called → Code executes → Output returned/printed
```

---

## 8. Benefits of Functions

✔ Breaks code into modules  
✔ Improves readability  
✔ Makes debugging easier  
✔ Supports teamwork in large projects  

---

## 9. Key Takeaways

✔ Functions are reusable blocks of code  
✔ Defined using `def`  
✔ Can take inputs (parameters)  
✔ Can return or print outputs  
✔ Help follow DRY principle  

---

## Final Idea

Functions allow Python programs to become **organized, reusable, and scalable by breaking complex logic into small manageable blocks of code**.