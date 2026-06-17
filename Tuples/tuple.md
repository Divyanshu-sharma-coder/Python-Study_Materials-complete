# Python Tuples

Tuples are an ordered collection of data items in Python. They allow you to store multiple items in a single variable. While they are highly similar to lists, the core difference is that **tuples are immutable**—once created, their elements and length cannot be changed.

---

## 1. Creating a Tuple

Tuples are created by placing elements inside round brackets `()` separated by commas.

```python
# Creating a tuple with multiple elements
tup = (1, 5, 6)

print(type(tup))  # Output: <class 'tuple'>
print(tup)        # Output: (1, 5, 6)
```

### The Single-Element Tuple Pitfall

If you want to create a tuple with only one element, you must include a trailing comma. Otherwise, Python will confuse it with a regular data type enclosed in parentheses.

```python
# Wrong Way: Confused as an integer
wrong_tup = (1)
print(type(wrong_tup))  # Output: <class 'int'>

# Correct Way: Explicitly a tuple
correct_tup = (1,)
print(type(correct_tup))  # Output: <class 'tuple'>
```

---

## 2. Immutability (Lists vs. Tuples)

Unlike lists, tuples do not support item assignment. Attempting to change an element will result in a `TypeError`.

### List Example (Mutable)

```python
my_list = [1, 2, 3]

my_list[0] = 90

print(my_list)  # Output: [90, 2, 3]
```

### Tuple Example (Immutable)

```python
my_tuple = (1, 2, 3)

# my_tuple[0] = 90
# TypeError: 'tuple' object does not support item assignment
```

### Why Use Tuples Over Lists?

Use tuples when you want a "constant list" whose contents must never be changed accidentally later in a program.

---

## 3. Tuple Indexing

Tuple items can be accessed using index numbers, just like lists.

### Positive Indexing

```python
tup = (2, 76, 342, 32, "Green", True)

print(tup[0])  # Output: 2
print(tup[2])  # Output: 342

# print(tup[34])
# IndexError: tuple index out of range
```

### Negative Indexing

Negative indexing counts backward from the end of the tuple.

Python calculates:

```python
actual_index = len(tuple) + negative_index
```

Example:

```python
tup = (2, 76, 342, 32, "Green", True)

print(tup[-1])  # Output: True
```

---

## 4. Checking for Elements (`in` Keyword)

You can check if a specific element exists within a tuple using the `in` keyword.

```python
tup = (2, 76, 342, 32, "Green", True)

if 342 in tup:
    print("342 is present in this tuple")
else:
    print("Not present")
```

---

## 5. Tuple Slicing

Slicing allows you to extract a portion of a tuple.

**Syntax:**

```python
tuple[start:end]
```

> The end index is excluded.

Example:

```python
tup = (2, 76, 342, 32, "Green", True)

new_tup = tup[1:4]

print(new_tup)  # Output: (76, 342, 32)
```

### Slicing Shortcuts

```python
tup = (2, 76, 342, 32)

print(tup[:3])   # Output: (2, 76, 342)
print(tup[2:])   # Output: (342, 32)
print(tup[:])    # Output: (2, 76, 342, 32)
```

### Rules

- Missing start index defaults to `0`
- Missing end index defaults to `len(tuple)`
- Slicing returns a brand-new tuple

---

## Summary

| Feature | Description |
|----------|-------------|
| Syntax | Defined using round brackets `()` or commas |
| Immutability | Cannot alter elements after creation |
| Single Element | Requires a trailing comma like `(1,)` |
| Indexing | Supports positive and negative indexing |
| Slicing | Extracts subset ranges into a new tuple |
| Membership (`in`) | Checks whether an element exists |

---

## Key Takeaway

Python tuples are ordered, immutable sequences. Use them when working with data that should remain constant throughout program execution and must be protected from accidental modification.