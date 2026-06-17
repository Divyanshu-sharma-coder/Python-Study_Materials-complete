# Lambda Functions in Python

A **Lambda Function** in Python is a small, throwaway, **anonymous function** (a function defined without a name).

Unlike regular functions defined using the standard `def` keyword, lambda functions are structured as a single inline expression.

They are highly compact and ideal for situations requiring clean, micro-sized operational logic.

---

## 1. Syntax Comparison

A standard function requires a name, intentional structural indentation, and an explicit `return` statement.

A lambda function collapses all of these requirements into a single line.

### Lambda Syntax

```python
lambda arguments: expression
```

### Components

| Component | Description |
|------------|------------|
| `lambda` | Keyword used to create an anonymous function |
| `arguments` | Input parameters passed into the function |
| `expression` | Single operation that is evaluated and automatically returned |

---

### Standard Function vs Lambda Function

#### Using `def`

```python
def square(x):
    return x * x

print(square(5))
```

#### Using `lambda`

```python
square = lambda x: x * x

print(square(5))
```

#### Output

```text
25
```

---

## 2. Code Implementation Demonstrations

### A. Single Parameter Transformation (Doubling a Number)

#### Standard Function

```python
def double_standard(x):
    return x * 2
```

#### Lambda Function

```python
double_lambda = lambda x: x * 2
```

#### Execution

```python
print(double_standard(5))
print(double_lambda(5))
```

#### Output

```text
10
10
```

---

### B. Cubing a Number

```python
cube = lambda x: x * x * x

print(cube(5))
```

#### Output

```text
125
```

---

### C. Multi-Parameter Operations (Calculating an Average)

Lambda functions can accept multiple arguments but can only contain a single expression.

#### Example

```python
average = lambda x, y, z: (x + y + z) / 3

print(average(3, 5, 10))
```

#### Output

```text
6.0
```

---

## 3. The True Use Case: Passing Functions as Arguments

Assigning a lambda function to a variable is useful for learning, but the real power of lambda functions appears when they are passed directly into another function.

This pattern is known as **Higher-Order Programming**.

A **Higher-Order Function** is a function that:

- Accepts another function as an argument.
- Returns another function.
- Or both.

---

### Example: Higher-Order Function

```python
def apply_operation(func, value):
    return 6 + func(value)
```

The parameter `func` expects another function.

---

### Case 1: Passing a Named Lambda Variable

```python
cube_operation = lambda x: x * x * x

print(apply_operation(cube_operation, 2))
```

#### Calculation

```text
6 + (2³)
6 + 8
```

#### Output

```text
14
```

---

### Case 2: Passing a Completely Anonymous Lambda

```python
print(
    apply_operation(
        lambda x: x * x,
        2
    )
)
```

#### Calculation

```text
6 + (2²)
6 + 4
```

#### Output

```text
10
```

---

## 4. Why Lambda Functions Exist

Without lambda:

```python
def square(x):
    return x * x

result = apply_operation(square, 2)
```

With lambda:

```python
result = apply_operation(
    lambda x: x * x,
    2
)
```

The lambda version avoids creating a separate function that may only be used once.

This keeps code concise and readable.

---

## 5. Lambda with Functional Programming Tools

Lambda functions are commonly used alongside Python's functional programming utilities.

### A. Using `map()`

Transform every element in a collection.

```python
numbers = [1, 2, 3, 4, 5]

squared = list(
    map(
        lambda x: x * x,
        numbers
    )
)

print(squared)
```

#### Output

```text
[1, 4, 9, 16, 25]
```

---

### B. Using `filter()`

Select only values that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

evens = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(evens)
```

#### Output

```text
[2, 4, 6]
```

---

### C. Using `sorted()`

Customize sorting behavior.

```python
students = [
    ("Alice", 80),
    ("Bob", 95),
    ("Charlie", 70)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)
```

#### Output

```text
[
    ('Charlie', 70),
    ('Alice', 80),
    ('Bob', 95)
]
```

---

## 6. Limitations of Lambda Functions

Lambda functions are intentionally restricted.

### Allowed

```python
lambda x: x * 2
```

```python
lambda x, y: x + y
```

```python
lambda name: name.upper()
```

### Not Allowed

Multiple statements:

```python
lambda x:
    a = x + 1
    return a
```

Loops:

```python
lambda x:
    for i in range(x):
        print(i)
```

Docstrings:

```python
lambda x:
    """Documentation"""
```

Complex business logic should use regular functions instead.

---

## Standard Function vs Lambda Function

| Feature | Standard Function (`def`) | Lambda Function |
|----------|-------------------------|----------------|
| Has Name | ✅ Yes | ❌ No (anonymous) |
| Multiple Statements | ✅ Yes | ❌ No |
| Explicit Return | ✅ Required | ❌ Automatic |
| Supports Docstrings | ✅ Yes | ❌ No |
| Readability for Complex Logic | ✅ Better | ❌ Poor |
| Best For | Large reusable logic | Small one-line operations |

---

## Summary Key Takeaways

### Lambda Functions Are:

- Anonymous functions.
- Defined using the `lambda` keyword.
- Limited to a single expression.
- Automatically return their result.
- Frequently used with `map()`, `filter()`, and `sorted()`.

### Best Use Cases

✅ Quick calculations

✅ One-time operations

✅ Higher-order functions

✅ Functional programming

### Avoid Lambda When

❌ Logic becomes complex

❌ Multiple statements are required

❌ Documentation is needed

❌ Readability suffers

---

## Recommended Professional Rule

Use:

```python
lambda x: x * 2
```

for short, obvious operations.

Use:

```python
def process_customer_data():
    ...
```

for anything involving multiple steps, conditions, loops, validation, or business logic.

A good rule of thumb is:

> If the lambda cannot fit comfortably on one line, it should probably be a regular function.