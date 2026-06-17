# Dictionaries in Python

A **Dictionary** in Python is an ordered collection of data items that stores elements as **key-value pairs**. Dictionaries are highly optimized for fast lookups and are similar to real-world dictionaries, where a word (key) maps to its meaning (value).

---

## 1. Core Structural Features

### Key-Value Pairs

Each entry consists of a key and its corresponding value.

```python
employee_ids = {
    344: "Harry",
    56: "Shubham",
    678: "Zakir",
    567: "Neha"
}

print(employee_ids[567])

# Output:
# Neha
```

---

### Dictionary Characteristics

- Stores data as `key: value` pairs
- Created using curly braces `{ }`
- Keys must be unique
- Values may be duplicated
- Ordered since Python 3.7+
- Extremely fast lookups using hash tables

---

## 2. Accessing Elements and Handling Missing Keys

There are two common ways to retrieve values.

### Bracket Notation

```python
info = {
    "name": "Karan",
    "age": 19
}

print(info["name"])

# Output:
# Karan
```

### Missing Key with Bracket Notation

```python
info = {
    "name": "Karan",
    "age": 19
}

# print(info["address"])

# KeyError:
# 'address'
```

If the key does not exist, Python raises a `KeyError`.

---

### The `.get()` Method

A safer alternative.

```python
info = {
    "name": "Karan",
    "age": 19
}

print(info.get("name"))

# Output:
# Karan
```

### Missing Key with `.get()`

```python
info = {
    "name": "Karan",
    "age": 19
}

print(info.get("address"))

# Output:
# None
```

Instead of crashing, Python returns `None`.

---

## 3. Extracting Keys, Values, and Items

### `.keys()`

Returns all keys.

```python
info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

print(info.keys())

# Output:
# dict_keys(['name', 'age', 'eligible'])
```

---

### `.values()`

Returns all values.

```python
info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

print(info.values())

# Output:
# dict_values(['Karan', 19, True])
```

---

### `.items()`

Returns key-value pairs as tuples.

```python
info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

print(info.items())

# Output:
# dict_items([
#     ('name', 'Karan'),
#     ('age', 19),
#     ('eligible', True)
# ])
```

---

## 4. Looping Through Dictionaries

### Using `.keys()`

```python
info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

for key in info.keys():
    print(f"The value corresponding to {key} is {info[key]}")
```

Possible Output:

```text
The value corresponding to name is Karan
The value corresponding to age is 19
The value corresponding to eligible is True
```

---

### Using `.items()` (Recommended)

The most Pythonic approach.

```python
info = {
    "name": "Karan",
    "age": 19,
    "eligible": True
}

for key, value in info.items():
    print(f"Key: {key} -> Value: {value}")
```

Output:

```text
Key: name -> Value: Karan
Key: age -> Value: 19
Key: eligible -> Value: True
```

---

## 5. Real-World Use Cases

### Student Grade Book

```python
grades = {
    "Harry": 92,
    "Karan": 88,
    "Neha": 95
}

print(grades["Neha"])

# Output:
# 95
```

---

### Product Catalog

```python
products = {
    "Laptop": 65000,
    "Phone": 25000,
    "Tablet": 18000
}

print(products["Phone"])

# Output:
# 25000
```

---

### Employee Records

```python
employee = {
    "id": 101,
    "name": "Harry",
    "department": "Data Science"
}

print(employee["department"])

# Output:
# Data Science
```

---

## Dictionary vs List

| Feature | List | Dictionary |
|----------|----------|----------|
| Access Method | Index | Key |
| Syntax | `[]` | `{}` |
| Lookup Speed | Slower | Faster |
| Data Structure | Single values | Key-value pairs |
| Example | `students[0]` | `students["Harry"]` |

---

## Summary Cheat Sheet

| Method / Operator | Purpose | Missing Key Behavior |
|------------------|----------|----------|
| `dict[key]` | Retrieve value using key | ❌ Raises `KeyError` |
| `dict.get(key)` | Safely retrieve value | ✅ Returns `None` |
| `keys()` | Returns all keys | N/A |
| `values()` | Returns all values | N/A |
| `items()` | Returns key-value tuples | N/A |
| `for key in dict` | Iterate over keys | N/A |
| `for key, value in dict.items()` | Iterate over keys and values | N/A |

---

## Key Takeaway

Dictionaries are one of Python's most powerful data structures. They store information as **key-value pairs**, provide extremely fast lookups, and are ideal for representing structured real-world data such as user profiles, product catalogs, configuration settings, and database-like records. Whenever you need to map one piece of information to another, a dictionary is often the best choice.