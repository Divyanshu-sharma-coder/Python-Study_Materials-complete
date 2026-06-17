# Python List Methods

In Python, lists are mutable data types, meaning their elements can be changed after they are created. Python provides several built-in methods to manipulate, sort, and gather information about lists.

---

## 1. Modifying and Adding Elements

### `append()`

Adds an element to the end of the list.

```python
l = [11, 2, 4, 6]
l.append(7)
print(l)  # Output: [11, 2, 4, 6, 7]
```

### `insert()`

Inserts an item at a specific index.

```python
l = [11, 2, 4, 6]
l.insert(1, 899)
print(l)  # Output: [11, 899, 2, 4, 6]
```

---

## 2. Ordering and Sorting Elements

### `sort()`

Sorts the list in ascending order.

```python
l = [11, 2, 4, 6]
l.sort()
print(l)  # Output: [2, 4, 6, 11]
```

### Sort in Descending Order

```python
l = [11, 2, 4, 6]
l.sort(reverse=True)
print(l)  # Output: [11, 6, 4, 2]
```

### `reverse()`

Reverses the order of elements.

```python
l = [11, 2, 4, 6]
l.reverse()
print(l)  # Output: [6, 4, 2, 11]
```

---

## 3. Information and Searching

### `index()`

Returns the index of the first occurrence of an element.

```python
l = [11, 2, 1, 4, 6, 1]
print(l.index(1))  # Output: 2
```

### `count()`

Counts how many times an element appears.

```python
l = [11, 2, 1, 4, 6, 1, 1]
print(l.count(1))  # Output: 3
```

---

## 4. Copying and Memory Management

### Reference Assignment

Both variables point to the same list.

```python
l = [11, 2, 4, 6]

m = l
m[0] = 0

print(l)  # Output: [0, 2, 4, 6]
print(m)  # Output: [0, 2, 4, 6]
```

### `copy()`

Creates an independent copy.

```python
l = [11, 2, 4, 6]

m = l.copy()
m[0] = 0

print(l)  # Output: [11, 2, 4, 6]
print(m)  # Output: [0, 2, 4, 6]
```

---

## 5. Joining and Merging Lists

### `extend()`

Adds elements from another iterable.

```python
l = [11, 2, 4, 6]
m = [900, 1000, 1100]

l.extend(m)

print(l)
# Output: [11, 2, 4, 6, 900, 1000, 1100]
```

### Concatenation Using `+`

Creates a new list.

```python
l = [11, 2, 4, 6]
m = [900, 1000, 1100]

k = l + m

print(k)
# Output: [11, 2, 4, 6, 900, 1000, 1100]

print(l)
# Output: [11, 2, 4, 6]

print(m)
# Output: [900, 1000, 1100]
```

---

## Summary

| Method | Description |
|----------|-------------|
| `append(x)` | Add an element to the end |
| `insert(i, x)` | Insert at a specific index |
| `sort()` | Sort ascending |
| `sort(reverse=True)` | Sort descending |
| `reverse()` | Reverse list order |
| `index(x)` | Return first index of element |
| `count(x)` | Count occurrences |
| `copy()` | Create shallow copy |
| `extend(iterable)` | Add elements from another iterable |
| `+` | Concatenate two lists |

---

### Key Takeaway

Python lists are mutable and provide powerful methods for adding, removing, sorting, searching, copying, and combining elements efficiently.