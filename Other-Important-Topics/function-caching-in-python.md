# Function Caching in Python

## 1. What is Function Caching?

Function caching is an optimization technique used to **store results of expensive function calls** so that future calls with the same inputs can be served instantly.

This avoids:
- Re-computation
- Unnecessary CPU usage
- Repeated delays

---

## Core Idea (Memoization)

Function caching is based on:

```
Memoization = Store + Reuse previous results
```

---

## Real-World Analogy

Imagine an e-commerce homepage:

- ❌ Without cache → rebuild layout every time (slow)
- ✔ With cache → serve pre-built layout instantly

---

## 2. Using `lru_cache` in Python

Python provides built-in caching using:

```python
functools.lru_cache
```

---

## Import Required

```python
import functools
import time
```

---

## Example: Baseline Caching Behavior

```python
import functools
import time

@functools.lru_cache(maxsize=None)
def expensive_calculation(n):
    print(f"Computing calculation for {n}...")
    time.sleep(5)  # Simulating heavy computation
    return n * 2


# First run (no cache)
print(expensive_calculation(20))
print(expensive_calculation(2))
print(expensive_calculation(6))

print("-" * 20)

# Second run (cached values)
print(expensive_calculation(20))
print(expensive_calculation(2))
print(expensive_calculation(6))

print("-" * 20)

# New value (not cached)
print(expensive_calculation(61))
```

---

## Output Behavior

```
Computing calculation for 20...
40
Computing calculation for 2...
4
Computing calculation for 6...
12
--------------------
40
4
12
--------------------
Computing calculation for 61...
122
```

---

## 3. How Caching Works

### First Call
- Function runs normally
- Result stored in cache

### Repeated Call
- Function is NOT executed
- Result is fetched directly from memory

---

## 4. Cache Lifetime

✔ Cache exists only during program execution

```
Start Program → Cache Exists → Program Ends → Cache Deleted
```

It is NOT stored in:
- ❌ Files
- ❌ Databases
- ❌ Persistent storage

---

## 5. When to Use Function Caching

✔ Good use cases:
- Heavy computations
- Repeated function calls
- API responses
- Database query optimization

---

## 6. When NOT to Use It

❌ Avoid caching when:
- Inputs are always unique
- Memory usage is a concern
- Data changes frequently

---

## 7. Memory Warning

If `maxsize` is too large or unlimited:

```python
@lru_cache(maxsize=None)
```

Then:
- Cache can grow infinitely
- RAM usage increases
- May cause performance issues in large systems

---

## 8. Key Takeaways

✔ Caching stores function results  
✔ `lru_cache` automates memoization  
✔ Saves time for repeated computations  
✔ Tradeoff: speed vs memory usage  

---

## Final Idea

Function caching improves performance by **avoiding repeated execution of expensive functions and serving results directly from memory when possible**.