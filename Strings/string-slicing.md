# String Slicing and Operations in Python

---

## 1. Finding the Length of a String (`len()`)

To determine the total number of character elements contained inside a text string, Python uses the built-in global **`len()`** function.

```python
fruit = "Mango"

# len() counts characters starting from 1
length_of_fruit = len(fruit)

print(f"Mango is a {length_of_fruit} letter word.")  
# Output: Mango is a 5 letter word.
```

---

## 2. Introduction to String Slicing

Slicing allows you to extract a specific segment (substring) from an existing string.

You perform slicing using square brackets `[]` with a start and end index separated by a colon `:`.

### Core Syntax:
```python
string_name[start_index : end_index]
```

📌 **Crucial Rule:**  
Slicing is **inclusive of start_index** but **exclusive of end_index**.

It extracts characters from `start_index` up to `end_index - 1`.

---

### Example ("Mango"):
```
Mango
0 1 2 3 4
```

```python
fruit = "Mango"

# Extract indices 0, 1, 2, 3 (excludes index 4)
print(fruit[0:4])  # Output: Mang

# Extract indices 1, 2, 3
print(fruit[1:4])  # Output: ang
```

---

## 3. Omitting Slice Index Arguments (Shorthand Syntax)

If you omit start or end index, Python automatically assumes default values.

---

### A. Missing Start Index (`[:end]`)

If start is missing, slicing starts from index `0`.

```python
fruit = "Mango"

print(fruit[:4])  # Output: Mang
```

---

### B. Missing End Index (`[start:]`)

If end is missing, slicing goes till the end of the string.

```python
fruit = "Mango"

print(fruit[0:])  # Output: Mango
print(fruit[:])   # Output: Mango
```

---

## 4. Negative Slicing Operations

Negative indexing counts from the end:

- `-1` → last character  
- `-2` → second last character  

Python internally converts negative indices using:
```
len(string) + negative_index
```

---

### Example 1:
```python
fruit = "Mango"  # length = 5

print(fruit[0:-3])
```

**Evaluation:**
- -3 → 5 + (-3) = 2  
- So expression becomes `fruit[0:2]`

**Output:**
```
Ma
```

---

### Example 2:
```python
print(fruit[-3:-1])
```

**Evaluation:**
- -3 → 2
- -1 → 4  
- So expression becomes `fruit[2:4]`

**Output:**
```
ng
```

---

## 5. Day #12 Brain Teaser Quiz

Test your string slicing understanding:

```python
nm = "Harry"

print(nm[-4:-2])
```

---

### Solution Breakdown:

- `len(nm) = 5`

Convert negative indices:
- Start: `5 + (-4) = 1`
- End: `5 + (-2) = 3`

So expression becomes:
```python
nm[1:3]
```

Extracts index `1` and `2`.

---

### Final Output:
```
ar
```