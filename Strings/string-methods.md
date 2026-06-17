# String Methods in Python

---

## 1. The Core Concept of Immutability

In Python, strings are **immutable**.  
This means once a string is created, it **cannot be changed in place**.

Whenever you apply a string method (like `.upper()` or `.lower()`), Python:

- Does NOT modify the original string
- Creates a **new string object**
- Returns the new value

```python
a = "Harry"

# Returns a new string but DOES NOT change original
print(a.upper())  # Output: HARRY
print(a)          # Output: Harry
```

---

## 2. Standard Case Modification Methods

### A. `.upper()`
Converts all characters to uppercase.

```python
a = "Harry"
print(a.upper())  # Output: HARRY
```

---

### B. `.lower()`
Converts all characters to lowercase.

```python
a = "Harry"
print(a.lower())  # Output: harry
```

---

### C. `.capitalize()`
Capitalizes the first character and makes the rest lowercase.

```python
heading = "iNtRoDuCtIoN tO jS"
print(heading.capitalize())  # Output: Introduction to js
```

---

### D. `.title()`
Capitalizes the first letter of each word.

```python
text = "his name is dan"
print(text.title())  # Output: His Name Is Dan
```

---

### E. `.swapcase()`
Swaps uppercase to lowercase and vice versa.

```python
text = "Python Programming"
print(text.swapcase())  # Output: pYTHON pROGRAMMING
```

---

## 3. Whitespace & Character Trimming Methods

### `.rstrip()`
Removes trailing characters (end of string only).

```python
text = "Harry!!!"
print(text.rstrip("!"))  # Output: Harry
```

---

## 4. Search, Replacement & Layout Methods

### A. `.replace()`
Replaces all occurrences of a substring.

```python
text = "Harry Harry"
print(text.replace("Harry", "John"))  # Output: John John
```

---

### B. `.split()`
Splits a string into a list.

```python
text = "Harry Rohan Lovish"
print(text.split(" "))
# Output: ['Harry', 'Rohan', 'Lovish']
```

---

### C. `.center()`
Centers a string with padding.

```python
msg = "Welcome"
print(msg.center(20))
# Output: "      Welcome       "
```

---

### D. `.count()`
Counts occurrences of a substring.

```python
text = "Harry Harry"
print(text.count("Harry"))  # Output: 2
```

---

## 5. Boolean Inspection Methods (True/False)

### A. `.startswith()` and `.endswith()`

```python
text = "Welcome to Python"

print(text.startswith("Welcome"))  # True
print(text.endswith("Python"))     # True

# Range-based check
print(text.endswith("to", 4, 10))  # True
```

---

### B. `.find()` vs `.index()`

```python
text = "He is an honest man"

print(text.find("is"))   # 3
print(text.find("xyz"))  # -1

print(text.index("is"))  # 3
# print(text.index("xyz"))  # ValueError
```

---

### C. Character Type Validators

- `.isalnum()` → only letters & numbers  
- `.isalpha()` → only letters  
- `.islower()` → all lowercase  
- `.isupper()` → all uppercase  
- `.isspace()` → only whitespace  
- `.istitle()` → title case format  
- `.isprintable()` → printable characters only  

```python
str1 = "Welcome00"
print(str1.isalnum())  # True

str2 = "Welcome\n"
print(str2.isprintable())  # False
```