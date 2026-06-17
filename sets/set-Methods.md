# Set Methods in Python

Python provides numerous built-in methods to perform operations on sets. Many of these methods mirror standard algebraic Set Theory (like unions and intersections), while others are built to handle structural content updates.

---

## 1. Set Operations (Mathematical)

### `union()` and `update()`

#### `union()`

Combines all unique elements from both sets and returns a **new set**.

```python
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

result = s1.union(s2)

print(result)

# Output:
# {1, 2, 3, 5, 6, 7}

print(s1)

# Output:
# {1, 2, 5, 6}
```

#### `update()`

Adds elements from another set directly into the original set.

```python
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

s1.update(s2)

print(s1)

# Output:
# {1, 2, 3, 5, 6, 7}
```

---

### `intersection()` and `intersection_update()`

#### `intersection()`

Returns a new set containing only common elements.

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities3 = cities.intersection(cities2)

print(cities3)

# Output:
# {'Tokyo', 'Madrid'}
```

#### `intersection_update()`

Keeps only common elements in the original set.

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.intersection_update(cities2)

print(cities)

# Output:
# {'Tokyo', 'Madrid'}
```

---

### `symmetric_difference()` and `symmetric_difference_update()`

Returns elements that exist in either set but not in both.

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.symmetric_difference(cities2))

# Output:
# {'Berlin', 'Delhi', 'Seoul', 'Kabul'}
```

#### `symmetric_difference_update()`

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.symmetric_difference_update(cities2)

print(cities)

# Output:
# {'Berlin', 'Delhi', 'Seoul', 'Kabul'}
```

---

### `difference()` and `difference_update()`

Returns elements present in the first set but missing from the second.

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

print(cities.difference(cities2))

# Output:
# {'Berlin', 'Delhi'}
```

#### `difference_update()`

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

cities.difference_update(cities2)

print(cities)

# Output:
# {'Berlin', 'Delhi'}
```

---

## 2. Set Conditional Inquiries

### `isdisjoint()`

Checks whether two sets have no common elements.

```python
s1 = {1, 2, 3}
s2 = {4, 5, 6}

print(s1.isdisjoint(s2))

# Output:
# True
```

---

### `issuperset()`

Returns `True` if the set contains all elements of another set.

```python
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities3 = {"Tokyo", "Madrid"}

print(cities.issuperset(cities3))

# Output:
# True
```

---

### `issubset()`

Returns `True` if every element exists in another set.

```python
cities = {"Tokyo", "Madrid"}
cities2 = {"Tokyo", "Madrid", "Berlin", "Delhi"}

print(cities.issubset(cities2))

# Output:
# True
```

---

## 3. Managing Items

### `add()`

Adds a single element.

```python
cities = {"Tokyo", "Berlin"}

cities.add("Helsinki")

print(cities)

# Output:
# {'Tokyo', 'Berlin', 'Helsinki'}
```

---

### `remove()`

Removes an element.

Raises `KeyError` if the element does not exist.

```python
cities = {"Tokyo", "Berlin"}

cities.remove("Berlin")

print(cities)

# Output:
# {'Tokyo'}
```

---

### `discard()`

Removes an element safely.

No error occurs if the item does not exist.

```python
cities = {"Tokyo", "Berlin"}

cities.discard("London")

print(cities)

# Output:
# {'Tokyo', 'Berlin'}
```

---

### `pop()`

Removes and returns a random element.

```python
cities = {"Tokyo", "Madrid", "Berlin"}

item = cities.pop()

print(item)
print(cities)
```

**Note:** Since sets are unordered, the removed item can vary.

---

### `clear()`

Removes all elements.

```python
cities = {"Tokyo", "Berlin"}

cities.clear()

print(cities)

# Output:
# set()
```

---

### `del`

`del` is a Python keyword, not a set method.

It completely removes the variable from memory.

```python
cities = {"Tokyo", "Berlin"}

del cities

# print(cities)

# NameError:
# name 'cities' is not defined
```

---

## 4. Membership Testing

### Using `in`

```python
info = {"Carla", 19, False}

if "Carla" in info:
    print("Carla is present!")

# Output:
# Carla is present!
```

### Using `not in`

```python
info = {"Carla", 19, False}

if "Harry" not in info:
    print("Harry is not present!")

# Output:
# Harry is not present!
```

---

## Summary Cheat Sheet

| Method | Purpose | Modifies Original Set? | Handles Missing Elements Gracefully? |
|----------|----------|----------|----------|
| `union()` | Combine sets | ❌ No | ✅ Yes |
| `update()` | Merge into original | ✅ Yes | ✅ Yes |
| `intersection()` | Common elements | ❌ No | ✅ Yes |
| `intersection_update()` | Keep common elements | ✅ Yes | ✅ Yes |
| `symmetric_difference()` | Non-common elements | ❌ No | ✅ Yes |
| `symmetric_difference_update()` | Update with non-common elements | ✅ Yes | ✅ Yes |
| `difference()` | Elements unique to first set | ❌ No | ✅ Yes |
| `difference_update()` | Remove common elements | ✅ Yes | ✅ Yes |
| `add()` | Add one item | ✅ Yes | ✅ Yes |
| `remove()` | Remove one item | ✅ Yes | ❌ No |
| `discard()` | Remove one item safely | ✅ Yes | ✅ Yes |
| `pop()` | Remove random item | ✅ Yes | ❌ No (if empty) |
| `clear()` | Remove all items | ✅ Yes | ✅ Yes |
| `isdisjoint()` | Check for common items | ❌ No | ✅ Yes |
| `issubset()` | Check subset relationship | ❌ No | ✅ Yes |
| `issuperset()` | Check superset relationship | ❌ No | ✅ Yes |

---

## Key Takeaway

Python sets are powerful data structures designed for working with unique values. Their built-in methods allow you to perform mathematical set operations, manage elements efficiently, and perform fast membership testing. Understanding these methods is essential for solving many real-world programming problems involving collections of unique data.