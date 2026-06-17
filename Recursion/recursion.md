# Recursion in Python

**Recursion** is a programming technique where a function calls itself directly or indirectly during execution. It allows complex problems to be solved by breaking them into smaller versions of the same problem.

---

## 1. What is Recursion?

In Python, a function can call another function. Similarly, a function can also call itself.

Without a stopping condition, recursive calls would continue forever, eventually causing a `RecursionError`.

To prevent this, every recursive function must contain a **Base Case**.

### Components of Recursion

1. **Base Case**
   - Stops the recursion.
   - Returns a concrete value.

2. **Recursive Case**
   - Calls the same function with a modified argument.
   - Moves closer to the base case.

---

## 2. Classic Example: Factorial

The factorial of a number `n` is the product of all positive integers less than or equal to `n`.

### Example

```text
5! = 5 × 4 × 3 × 2 × 1 = 120
```

---

## Recursive Formula

```text
Factorial(n) = n × Factorial(n - 1)
```

### Base Cases

```text
Factorial(0) = 1
Factorial(1) = 1
```

---

## Python Implementation

```python
def factorial(n):

    # Base Case
    if n == 0 or n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)

print(factorial(3))  # Output: 6
print(factorial(4))  # Output: 24
print(factorial(5))  # Output: 120
```

---

## How the Call Stack Executes `factorial(5)`

```text
factorial(5)
= 5 * factorial(4)

factorial(4)
= 4 * factorial(3)

factorial(3)
= 3 * factorial(2)

factorial(2)
= 2 * factorial(1)

factorial(1)
= 1   ← Base Case Reached
```

### Resolution Phase

```text
2 × 1  = 2
3 × 2  = 6
4 × 6  = 24
5 × 24 = 120
```

Final Result:

```text
120
```

---

## 3. Classic Example: Fibonacci Sequence

The Fibonacci Sequence is a series where each number equals the sum of the previous two numbers.

### Mathematical Rules

```text
F(0) = 0
F(1) = 1

F(n) = F(n - 1) + F(n - 2)
```

---

## Fibonacci Sequence

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
```

---

## 4. Recursive Fibonacci Function

### Python Implementation

```python
def fibonacci(n):

    # Base Cases
    if n == 0:
        return 0

    elif n == 1:
        return 1

    # Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
print(fibonacci(6))  # Output: 8
```

---

## How Fibonacci Recursion Works

Example:

```python
fibonacci(5)
```

Expands into:

```text
fibonacci(5)
=
fibonacci(4) + fibonacci(3)

=
(fibonacci(3) + fibonacci(2))
+
(fibonacci(2) + fibonacci(1))
```

The process continues until all branches reach:

```text
fibonacci(0)
fibonacci(1)
```

which are the base cases.

---

## Common Errors

### Missing Base Case

```python
def bad_function(n):
    return bad_function(n - 1)
```

Result:

```text
RecursionError:
maximum recursion depth exceeded
```

Reason:

The function never stops calling itself.

---

### Not Moving Toward the Base Case

```python
def bad_function(n):
    if n == 0:
        return 0

    return bad_function(n + 1)
```

Result:

```text
Infinite recursion
```

Reason:

The value moves away from the base case instead of toward it.

---

## Advantages of Recursion

- Elegant and concise code
- Natural solution for tree structures
- Useful for divide-and-conquer algorithms
- Closely matches mathematical definitions

---

## Disadvantages of Recursion

- Higher memory usage due to call stack
- Slower than iterative solutions in some cases
- Risk of `RecursionError`
- Can be harder to debug

---

## Summary

| Component | Purpose | Risk if Missing |
|------------|---------|----------------|
| Base Case | Terminates recursion | Causes `RecursionError` |
| Recursive Case | Calls the function again | Function behaves like a normal one-time function |
| Call Stack | Stores pending function calls | Consumes memory |
| Argument Progression | Moves toward base case | Infinite recursion |

---

## Key Takeaway

Recursion solves problems by reducing them into smaller versions of themselves. Every recursive function must have a **Base Case** and a **Recursive Case**. With each recursive call, the input should move closer to the base case; otherwise, the program will continue indefinitely and eventually crash with a `RecursionError`.