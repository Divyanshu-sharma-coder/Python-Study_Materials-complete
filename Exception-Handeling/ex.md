# Exception Handling in Python

In programming, unexpected runtime errors can occur due to invalid user input, incorrect operations, missing files, network failures, or programmer mistakes.

Without exception handling, these errors cause the program to terminate immediately.

**Exception Handling** allows a program to detect, manage, and recover from errors gracefully instead of crashing.

---

## 1. The Core `try-except` Construct

Python provides two primary blocks for handling exceptions:

- `try` → Contains code that may generate an error.
- `except` → Contains code that runs if an error occurs.

---

## The Crash Problem (Without Exception Handling)

```python
a = input("Enter the number: ")

print(f"Multiplication table of {a}")

num = int(a)

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")

print("Some critical lines of code...")
print("End of program")
```

### Problem

If the user enters:

```text
Harry
```

Python produces:

```text
ValueError:
invalid literal for int() with base 10: 'Harry'
```

The entire program stops immediately.

The last two print statements never execute.

---

## The Graceful Solution (Using `try-except`)

```python
a = input("Enter the number: ")

try:
    num = int(a)

    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

except:
    print("Invalid Input! Please enter a valid integer.")

print("Some critical lines of code...")
print("End of program")
```

### Output (if user enters "Harry")

```text
Invalid Input! Please enter a valid integer.

Some critical lines of code...
End of program
```

The program continues running.

---

## 2. Catching Specific Exception Types

Instead of catching every possible error, Python allows handling specific exceptions individually.

---

### Example

```python
try:
    num = int(input("Enter an index number: "))

    a = [6, 3]

    print(a[num])

except ValueError:
    print("Number entered is not a valid integer.")

except IndexError:
    print("Index Error! That position does not exist.")
```

---

### Scenario 1

Input:

```text
abc
```

Output:

```text
Number entered is not a valid integer.
```

---

### Scenario 2

Input:

```text
5
```

Output:

```text
Index Error! That position does not exist.
```

---

### Scenario 3

Input:

```text
0
```

Output:

```text
6
```

No exception occurs.

---

## Common Built-in Exceptions

| Exception | Cause |
|------------|------------|
| ValueError | Invalid value |
| IndexError | Invalid list index |
| KeyError | Missing dictionary key |
| TypeError | Wrong data type |
| ZeroDivisionError | Division by zero |
| FileNotFoundError | Missing file |
| ImportError | Failed module import |
| NameError | Undefined variable |

---

## Example: ZeroDivisionError

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Output:

```text
Cannot divide by zero.
```

---

## Example: KeyError

```python
student = {
    "name": "Harry"
}

try:
    print(student["age"])

except KeyError:
    print("Key not found.")
```

Output:

```text
Key not found.
```

---

## 3. Capturing the Exception Object

Python allows you to inspect the actual error message.

Use the `as` keyword.

---

### Syntax

```python
except ExceptionType as e:
```

---

### Example

```python
try:
    num = int(input("Enter a number: "))

except ValueError as e:
    print(f"System Error Trace: {e}")
```

Input:

```text
Harry
```

Output:

```text
System Error Trace:
invalid literal for int() with base 10: 'Harry'
```

The variable `e` stores Python's original exception message.

---

## 4. Catching Multiple Exceptions Together

```python
try:
    value = int(input("Enter a number: "))

    result = 10 / value

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

---

### Input

```text
0
```

Output:

```text
Division by zero is not allowed.
```

---

## 5. Generic Exception Handling

You can catch all exceptions using:

```python
try:
    x = int(input("Enter a number: "))

except Exception as e:
    print(f"Error occurred: {e}")
```

### Warning ⚠️

Avoid overusing generic exceptions because they can hide bugs.

Prefer specific exceptions whenever possible.

---

## 6. The `else` Block

The `else` block executes only if no exception occurs.

```python
try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Conversion successful.")
```

---

### Input

```text
25
```

Output:

```text
Conversion successful.
```

---

## 7. The `finally` Block

The `finally` block always executes.

It runs whether an exception occurs or not.

```python
try:
    print("Opening file...")

except:
    print("Something went wrong.")

finally:
    print("Closing file...")
```

Output:

```text
Opening file...
Closing file...
```

---

## Execution Flow

```text
try
 │
 ├── No Error
 │     │
 │     └── else
 │
 ├── Error
 │     │
 │     └── except
 │
 └── finally
```

The `finally` block always executes last.

---

## Why Exception Handling Matters

### System Continuity

Programs remain operational despite errors.

---

### Better User Experience

Instead of crashing:

```text
ValueError:
invalid literal for int()
```

You can show:

```text
Please enter a valid number.
```

---

### Easier Debugging

Specific exception handling reveals exactly what failed.

---

### Safer Programs

Unexpected situations are managed gracefully.

---

## Summary Cheat Sheet

| Keyword | Purpose |
|----------|----------|
| `try` | Code that may fail |
| `except` | Handles exceptions |
| `except ErrorType` | Handles a specific exception |
| `except ErrorType as e` | Captures error details |
| `else` | Runs if no exception occurs |
| `finally` | Always executes |
| `raise` | Manually generate an exception |

---

## Key Takeaway

Exception Handling allows Python programs to survive runtime errors without crashing. The `try-except` mechanism catches failures and redirects execution into safe recovery paths. Professional applications rely heavily on exception handling to improve reliability, debugging, and user experience.