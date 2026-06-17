# The `finally` Keyword in Python

The `finally` block is a special component of Python's exception-handling system. It is used to execute code that **must run regardless of whether an exception occurs or not**.

The primary purpose of `finally` is resource cleanup, such as:

- Closing files
- Closing database connections
- Releasing network resources
- Cleaning temporary data
- Restoring application states

---

## 1. What is the `finally` Block?

The code inside a `finally` block is guaranteed to execute after the `try` and `except` blocks complete.

```python
try:
    l = [1, 5, 6, 7]

    i = int(input("Enter the index: "))

    print(l[i])

except IndexError:
    print("Some index error occurred.")

finally:
    print("I am always executed!")
```

---

## Scenario A: Valid Input

Input:

```text
0
```

Output:

```text
1
I am always executed!
```

No exception occurs, but the `finally` block still runs.

---

## Scenario B: Invalid Input

Input:

```text
5
```

Output:

```text
Some index error occurred.
I am always executed!
```

An exception occurs, yet the `finally` block still executes.

---

## Execution Flow

```text
try
 │
 ├── Success
 │      │
 │      └── finally
 │
 └── Error
        │
        ├── except
        │
        └── finally
```

The `finally` block always executes last.

---

## 2. Why Not Simply Write Code Below `try-except`?

Many beginners ask:

```python
try:
    # risky code

except:
    # error handling

print("I also run.")
```

Why not use this instead of `finally`?

---

## Normal Script Example

```python
try:
    print("Inside try")

except:
    print("Inside except")

print("Outside block")
```

Output:

```text
Inside try
Outside block
```

This seems similar to `finally`.

However, the difference appears when functions use `return`.

---

## 3. The Real Power of `finally`

### Example Without `finally`

```python
def func1():

    try:
        l = [1, 5, 6, 7]

        i = int(input("Enter index: "))

        print(l[i])

        return 1

    except:
        print("Some error occurred.")

        return 0

    print("I will never execute!")

    return -1
```

---

### Input

```text
0
```

Output:

```text
1
```

The function immediately exits after:

```python
return 1
```

Everything below it is skipped.

---

## Example With `finally`

```python
def func1():

    try:
        l = [1, 5, 6, 7]

        i = int(input("Enter index: "))

        print(l[i])

        return 1

    except:
        print("Some error occurred.")

        return 0

    finally:
        print("I am inside finally and I always run!")

x = func1()

print(x)
```

---

### Input

```text
0
```

Output:

```text
1
I am inside finally and I always run!
1
```

---

## What Happened?

Even though:

```python
return 1
```

was executed, Python temporarily pauses the function exit, executes the `finally` block, and only then returns control to the caller.

This is why `finally` is so powerful.

---

## Demonstration with Both Return Paths

```python
def test(value):

    try:

        if value > 0:
            return "Positive"

        return "Zero or Negative"

    finally:
        print("Cleanup executed")
```

---

### Example 1

```python
print(test(5))
```

Output:

```text
Cleanup executed
Positive
```

---

### Example 2

```python
print(test(-1))
```

Output:

```text
Cleanup executed
Zero or Negative
```

The `finally` block executes regardless of which return path is taken.

---

## 4. `finally` with Exceptions

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Execution completed.")
```

Output:

```text
Cannot divide by zero.
Execution completed.
```

---

## 5. `finally` Without an `except`

A `finally` block can exist alongside only a `try` block.

```python
try:
    print("Working...")

finally:
    print("Cleanup complete.")
```

Output:

```text
Working...
Cleanup complete.
```

---

## 6. Real-World File Handling Example

Without `finally`, a file might remain open if an error occurs.

```python
file = open("data.txt")

try:
    content = file.read()

finally:
    file.close()
```

Regardless of success or failure:

```python
file.close()
```

always executes.

---

## 7. Database Example

```python
connection = create_connection()

try:
    run_query()

finally:
    connection.close()
```

Even if the query crashes, the database connection is properly released.

---

## 8. Network Request Example

```python
socket = connect_to_server()

try:
    send_data()

finally:
    socket.close()
```

This prevents resource leaks.

---

## Common Use Cases

| Task | Why Use `finally`? |
|--------|--------|
| File Handling | Always close files |
| Database Operations | Always close connections |
| Network Programming | Always release sockets |
| Temporary Files | Always remove them |
| UI Applications | Restore interface state |
| Resource Management | Prevent memory/resource leaks |

---

## Summary Cheat Sheet

| Situation | Normal Code After `try-except` | `finally` |
|------------|------------|------------|
| No Error | ✅ Runs | ✅ Runs |
| Exception Handled | ✅ Runs | ✅ Runs |
| Function Returns Early | ❌ Skipped | ✅ Runs |
| Cleanup Required | ❌ Not Guaranteed | ✅ Guaranteed |
| Resource Management | ❌ Risky | ✅ Safe |

---

## Difference Between `except`, `else`, and `finally`

| Block | Executes When? |
|---------|---------|
| `except` | Only when an exception occurs |
| `else` | Only when no exception occurs |
| `finally` | Always executes |

---

## Key Takeaway

The `finally` block exists to guarantee execution of critical cleanup code. Unlike normal statements written after a `try-except` structure, `finally` executes even when a function encounters a `return` statement or an exception. This makes it essential for safely managing files, databases, network connections, and other resources that must be released under all circumstances.