# Sets in Python

In Python, a **Set** is an unordered collection of data items. Borrowing principles from mathematical Set Theory, a set is used to store multiple items in a single variable while strictly ensuring that **no duplicate entries** exist.

---

## 1. Why Use Sets? (The Core Problem Solved)

Imagine gathering unique data (like names or employee IDs) from various sources. If you collect this data in a list, it can quickly become cluttered with duplicates if people submit the same entry multiple times.

A set automatically removes duplicate values.

```python
# Initial set contains repeated values
s = {2, 4, 2, 6}

print(s)

# Output:
# {2, 4, 6}
```

Notice that the duplicate `2` is automatically removed.

---

## 2. Structural Features of Sets

### Unordered Collection

Elements inside a set do not have a fixed order.

```python
s = {10, 20, 30, 40}

print(s)
```

The display order may differ from the order in which items were inserted.

---

### Unindexed Access

Sets do not support indexing.

```python
s = {10, 20, 30}

# print(s[0])

# TypeError:
# 'set' object is not subscriptable
```

---

### Immutable Elements

Individual items inside a set cannot be modified directly.

However, you can:

- Add new elements
- Remove existing elements

```python
s = {1, 2, 3}

s.add(4)

print(s)
```

---

### Heterogeneous Data

Sets can store multiple data types together.

```python
info = {"Carla", 19, False, 5.9}

print(info)

# Example Output:
# {False, 'Carla', 19, 5.9}
```

---

## 3. The Empty Set Trap ⚠️

A common mistake is using `{}` to create an empty set.

### Wrong Way

```python
wrong_set = {}

print(type(wrong_set))

# Output:
# <class 'dict'>
```

Python interprets `{}` as an empty dictionary.

---

### Correct Way

Use the `set()` constructor.

```python
correct_set = set()

print(type(correct_set))

# Output:
# <class 'set'>
```

---

## 4. Accessing Set Items

Since sets are unordered and unindexed, elements must be accessed using iteration.

### Using a `for` Loop

```python
info = {"Carla", 19, False, 5.9}

for value in info:
    print(value)
```

Possible Output:

```text
False
Carla
19
5.9
```

The order may vary each time the program runs.

---

## Set Membership Testing

One major advantage of sets is fast membership checking.

```python
numbers = {10, 20, 30, 40}

print(20 in numbers)

# Output:
# True
```

```python
print(99 in numbers)

# Output:
# False
```

---

## Removing Duplicates from a List

A common use case for sets is duplicate removal.

```python
numbers = [1, 2, 2, 3, 3, 4, 5, 5]

unique_numbers = set(numbers)

print(unique_numbers)

# Output:
# {1, 2, 3, 4, 5}
```

---

## Summary

| Feature | Lists / Tuples | Sets |
|----------|---------------|------|
| Duplicates | Allowed | Automatically removed |
| Indexing | Supported | Not supported |
| Ordering | Maintains order | Unordered |
| Empty Declaration | `[]` or `()` | `set()` |
| Membership Checking | Slower | Faster |
| Unique Values | Not guaranteed | Guaranteed |

---

## Key Takeaway

Python sets are unordered collections that automatically remove duplicates and provide efficient membership testing. They are ideal when you care about **uniqueness of data** rather than the order in which the data appears.