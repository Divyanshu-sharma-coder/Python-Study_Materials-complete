# Raising Custom Errors in Python

In software development, there are two major aspects of exception management:

1. **Handling Exceptions** → Managing unexpected runtime failures using `try-except`.
2. **Raising Exceptions** → Intentionally stopping program execution when invalid conditions are detected.

Python allows developers to manually generate exceptions using the `raise` keyword.

---

## 1. What is `raise`?

The `raise` keyword is used to deliberately trigger an exception.

Instead of waiting for Python to discover a problem, you explicitly tell Python:

> "This condition is invalid. Stop execution immediately."

### Syntax

```python
raise ExceptionType("Error Message")
```

---

## 2. Why Intentionally Raise Errors?

At first glance, intentionally crashing a program sounds strange.

However, in real-world software, allowing invalid data to continue through a system can cause:

- Corrupted databases
- Incorrect financial calculations
- Security vulnerabilities
- Broken business logic

Professional applications validate inputs early and stop execution when requirements are violated.

---

## Example: Input Validation

```python
a = int(input("Enter any value between 5 and 9: "))

if a < 5 or a > 9:
    raise ValueError("Value must be between 5 and 9!")

print(f"Success! Proceeding with value: {a}")
```

---

### Valid Input

Input:

```text
7
```

Output:

```text
Success! Proceeding with value: 7
```

---

### Invalid Input

Input:

```text
3
```

Output:

```text
ValueError:
Value must be between 5 and 9!
```

Execution immediately stops.

---

## 3. Raising Built-in Exceptions

Python provides many built-in exception classes that can be raised manually.

---

### ValueError

Used when the value is invalid but the data type is correct.

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

### ZeroDivisionError

```python
number = 0

if number == 0:
    raise ZeroDivisionError("Division by zero is prohibited.")
```

---

### IndexError

```python
index = 10

if index >= 5:
    raise IndexError("Index exceeds list size.")
```

---

### TypeError

```python
name = 123

if not isinstance(name, str):
    raise TypeError("Name must be a string.")
```

---

## Common Built-in Exceptions

| Exception | Purpose |
|------------|------------|
| ValueError | Invalid value |
| TypeError | Wrong data type |
| IndexError | Invalid sequence index |
| KeyError | Missing dictionary key |
| ZeroDivisionError | Division by zero |
| FileNotFoundError | File missing |
| MemoryError | Memory exhausted |
| ImportError | Failed import |

---

## 4. Raising Exceptions Inside Functions

Validation logic is often placed inside functions.

```python
def divide(a, b):

    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    return a / b

print(divide(10, 2))
```

Output:

```text
5.0
```

---

### Invalid Call

```python
print(divide(10, 0))
```

Output:

```text
ZeroDivisionError:
Cannot divide by zero.
```

---

## 5. Using `raise` with `try-except`

Raised exceptions can be caught just like system-generated exceptions.

```python
try:

    age = int(input("Enter age: "))

    if age < 18:
        raise ValueError("User must be at least 18 years old.")

except ValueError as e:
    print(f"Validation Failed: {e}")
```

---

### Input

```text
15
```

Output:

```text
Validation Failed:
User must be at least 18 years old.
```

---

## 6. Creating Custom Exceptions

For large applications, generic exceptions such as:

```python
ValueError
TypeError
IndexError
```

may not provide enough context.

Python allows you to create your own exception types.

---

## Creating a Custom Exception Class

Every custom exception inherits from Python's base `Exception` class.

```python
class ServerOffError(Exception):
    pass
```

Now Python recognizes:

```python
ServerOffError
```

as a legitimate exception type.

---

## Example: Server Status Validation

```python
class ServerOffError(Exception):
    pass

server_power = False

if not server_power:
    raise ServerOffError(
        "Critical: Primary server is offline!"
    )
```

Output:

```text
ServerOffError:
Critical: Primary server is offline!
```

---

## Adding Documentation to Custom Exceptions

```python
class ServerOffError(Exception):
    """
    Raised when the server loses power.
    """
    pass
```

This improves maintainability and readability.

---

## 7. Catching Custom Exceptions

Custom exceptions work exactly like built-in exceptions.

```python
class ServerOffError(Exception):
    pass

try:

    server_power = False

    if not server_power:
        raise ServerOffError("Server is offline.")

except ServerOffError as e:
    print(e)
```

Output:

```text
Server is offline.
```

---

## 8. Real-World Example: Bank Withdrawal System

```python
class InsufficientFundsError(Exception):
    pass

balance = 500

withdraw_amount = 1000

if withdraw_amount > balance:
    raise InsufficientFundsError(
        "Insufficient account balance."
    )
```

Output:

```text
InsufficientFundsError:
Insufficient account balance.
```

---

## 9. Real-World Example: Age Verification

```python
class UnderAgeError(Exception):
    pass

age = 16

if age < 18:
    raise UnderAgeError(
        "You must be at least 18 years old."
    )
```

---

## Exception Hierarchy

```text
BaseException
    │
    ├── Exception
    │       │
    │       ├── ValueError
    │       ├── TypeError
    │       ├── IndexError
    │       ├── KeyError
    │       └── YourCustomError
```

Custom exceptions usually inherit from:

```python
Exception
```

---

## Difference Between Handling and Raising

| Operation | Keyword | Purpose |
|------------|------------|------------|
| Handle Error | `try-except` | Prevent program crashes |
| Raise Error | `raise` | Stop execution when conditions are invalid |
| Custom Error | `class MyError(Exception)` | Create application-specific exceptions |

---

## Summary Cheat Sheet

| Syntax | Purpose |
|----------|----------|
| `raise ValueError("msg")` | Raise built-in exception |
| `raise TypeError("msg")` | Raise type-related error |
| `raise Exception("msg")` | Raise generic exception |
| `class MyError(Exception)` | Create custom exception |
| `raise MyError("msg")` | Raise custom exception |
| `except MyError as e` | Catch custom exception |

---

## Key Takeaway

The `raise` keyword allows developers to intentionally stop program execution when invalid conditions are detected. This prevents bad data from spreading through a system and makes software safer and easier to debug. For large-scale applications, custom exception classes provide precise, domain-specific error handling that improves code quality and maintainability.