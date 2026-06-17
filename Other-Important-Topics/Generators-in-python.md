# Generators in Python

## 1. What are Generators?

Generators are a special type of function in Python that **produce values one at a time instead of storing everything in memory**.

They behave like iterators but are much more memory efficient.

---

## Core Idea

Instead of building a full dataset:

```
[0, 1, 2, 3, 4]
```

A generator produces:

```
0 → 1 → 2 → 3 → 4 (one by one)
```

---

## Real-Life Analogy

- ❌ List = full basket of mangoes (stored all at once)
- ✔ Generator = mango tree (produces mangoes when needed)

---

## 2. Lists vs Generators

### ✔ Lists / Tuples / Sets
- Store everything in memory
- High RAM usage
- Fast access, but heavy for large data

### ✔ Generators
- Do NOT store full data
- Generate values on demand
- Extremely memory efficient

---

## 3. The `yield` Keyword

Generators use `yield` instead of `return`.

---

## Difference

### ✔ `return`
- Ends function completely
- Sends final output

### ✔ `yield`
- Pauses function
- Saves state
- Resumes later

---

## Lazy Evaluation

Generators use:

```
Lazy Evaluation = compute only when needed
```

---

## 4. Practical Implementation

---

## A. Manual Iteration Using `next()`

```python
def my_generator():
    for i in range(5):
        yield i


gen = my_generator()

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 2
```

---

## How It Works

Each `next()`:
- Resumes function
- Runs until next `yield`
- Pauses again

---

## B. Loop-Based Traversal

```python
def large_scale_generator():
    for i in range(50000000):
        yield i


for value in large_scale_generator():
    print(value)

    if value == 5:
        break
```

---

## Why This Is Powerful

Even with 50 million values:

✔ No memory crash  
✔ No full storage  
✔ Values generated on the fly  

---

## 5. Memory Advantage

### Without Generator
```
list(range(50000000)) → huge RAM usage
```

### With Generator
```
one value at a time → constant memory usage
```

---

## 6. Key Benefits of Generators

### ✔ Memory Efficiency
- No large storage in RAM
- Ideal for big data streams

### ✔ Fast Startup
- No waiting for full dataset creation

### ✔ Pipeline Friendly
- Perfect for:
  - Data Science
  - ML pipelines
  - Log processing
  - Streaming data

---

## 7. When to Use Generators

✔ Use when:
- Data is large
- You only need values once
- Streaming / continuous processing

---

## 8. When NOT to Use Generators

❌ Avoid when:
- You need random access
- You need to reuse data multiple times
- You need sorting or indexing

---

## Final Idea

Generators allow Python to work with **infinite or massive data efficiently by producing values only when required instead of storing everything in memory**.