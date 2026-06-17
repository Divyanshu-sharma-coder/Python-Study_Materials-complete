# Dictionary Methods in Python

Python provides multiple built-in methods to manipulate, structure, and modify dictionaries. These methods are essential when working with key-value mappings and are widely used in applications, APIs, databases, and data processing.

---

## 1. Merging and Clearing Data

### `update()`

The `update()` method merges another dictionary into the current dictionary.

- Existing keys are updated.
- New keys are added.

```python
# Initial employee performance metrics
ep1 = {
    122: 45,
    123: 89,
    567: 69,
    670: 69
}

ep2 = {
    222: 67,
    56: 90
}

ep1.update(ep2)

print(ep1)

# Output:
# {
#   122: 45,
#   123: 89,
#   567: 69,
#   670: 69,
#   222: 67,
#   56: 90
# }
```

---

### Updating Existing Keys

```python
student = {
    "name": "Harry",
    "age": 20
}

student.update({"age": 21})

print(student)

# Output:
# {'name': 'Harry', 'age': 21}
```

---

### `clear()`

Removes all key-value pairs from the dictionary.

```python
ep1 = {
    122: 45,
    123: 89
}

ep1.clear()

print(ep1)

# Output:
# {}
```

---

## 2. Removing Elements Dynamically

### `pop()`

Removes a specified key and returns its corresponding value.

```python
ep1 = {
    122: 45,
    123: 89,
    567: 69
}

removed_value = ep1.pop(123)

print(removed_value)

# Output:
# 89

print(ep1)

# Output:
# {122: 45, 567: 69}
```

---

### Missing Key with `pop()`

```python
ep1 = {
    122: 45
}

# ep1.pop(999)

# KeyError:
# 999
```

---

### `popitem()`

Removes and returns the last inserted key-value pair.

```python
ep1 = {
    122: 45,
    123: 89,
    567: 69
}

removed_pair = ep1.popitem()

print(removed_pair)

# Output:
# (567, 69)

print(ep1)

# Output:
# {122: 45, 123: 89}
```

---

### Empty Dictionary Warning

```python
empty_dict = {}

# empty_dict.popitem()

# KeyError:
# 'popitem(): dictionary is empty'
```

---

## 3. The `del` Keyword

`del` is a Python keyword, not a dictionary method.

It is used to delete specific entries or entire variables.

---

### Removing a Specific Key

```python
ep1 = {
    122: 45,
    123: 89
}

del ep1[122]

print(ep1)

# Output:
# {123: 89}
```

---

### Deleting the Entire Dictionary

```python
ep1 = {
    122: 45,
    123: 89
}

del ep1

# print(ep1)

# NameError:
# name 'ep1' is not defined
```

---

## 4. Strict Type Matching Warning ⚠️

Dictionary keys are type-sensitive.

```python
ep1 = {
    122: 45
}

# del ep1["122"]

# KeyError:
# '122'
```

Reason:

```python
122      # Integer
"122"    # String
```

These are completely different keys.

Correct usage:

```python
del ep1[122]
```

---

## 5. Additional Useful Dictionary Methods

### `copy()`

Creates a shallow copy of a dictionary.

```python
student = {
    "name": "Harry",
    "age": 20
}

student_copy = student.copy()

print(student_copy)

# Output:
# {'name': 'Harry', 'age': 20}
```

---

### `setdefault()`

Returns the value of a key.

If the key does not exist, it creates it with a default value.

```python
student = {
    "name": "Harry"
}

student.setdefault("age", 20)

print(student)

# Output:
# {'name': 'Harry', 'age': 20}
```

---

### `fromkeys()`

Creates a dictionary from a sequence of keys.

```python
keys = ["name", "age", "city"]

new_dict = dict.fromkeys(keys, "Not Provided")

print(new_dict)

# Output:
# {
#   'name': 'Not Provided',
#   'age': 'Not Provided',
#   'city': 'Not Provided'
# }
```

---

## Summary Reference Table

| Method / Operator | Purpose | Parameters Required? | Missing Key Behavior |
|------------------|----------|----------|----------|
| `update(dict2)` | Merge another dictionary | ✅ Yes | Adds new entries |
| `clear()` | Remove all items | ❌ No | Clears silently |
| `pop(key)` | Remove key and return value | ✅ Yes | ❌ Raises `KeyError` |
| `popitem()` | Remove last inserted pair | ❌ No | ❌ Raises `KeyError` if empty |
| `del dict[key]` | Delete specific key | ✅ Yes | ❌ Raises `KeyError` |
| `del dict` | Delete entire dictionary | ❌ No | Removes variable |
| `copy()` | Create shallow copy | ❌ No | Safe |
| `setdefault()` | Get or create key | ✅ Yes | Creates key if missing |
| `fromkeys()` | Create dictionary from keys | ✅ Yes | Safe |

---

## Key Takeaway

Dictionary methods allow you to efficiently add, update, remove, copy, and manage key-value data. Methods like `update()`, `pop()`, `popitem()`, and `clear()` are used frequently in real-world applications, while keywords like `del` provide direct control over dictionary memory management. Understanding these operations is essential for working with structured data in Python.