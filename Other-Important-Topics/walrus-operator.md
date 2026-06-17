# The Walrus Operator in Python

## 1. What is the Walrus Operator?

The **Walrus Operator** (`:=`) was introduced in **Python 3.8**.

It is officially called:
```
Assignment Expression
```

It allows you to:
- Assign a value
- AND use it in the same expression

---

## Why is it called "Walrus"?

Because `:=` looks like:
```
(:=) → walrus eyes and tusks
```

---

## Why use it?

✔ Reduces extra lines of code  
✔ Avoids repeated calculations  
✔ Makes loops and conditions cleaner  

---

## 2. Basic Syntax Comparison

---

### ❌ Without Walrus Operator

```python
a = False
print(a)
```

Or incorrect usage:

```python
# invalid syntax (cannot assign inside expression like this)
print(a = False)
```

---

### ✔ With Walrus Operator

```python
print(a := False)
```

---

## What happens here?

```
a = False  → assigned
print(a)   → printed
```

All in one line.

---

## 3. Practical Example: User Input Loop

---

### ❌ Traditional Way

```python
foods = []

while True:
    food = input("What food do you like? ")

    if food == "quit":
        break

    foods.append(food)
```

---

## ✔ Problem

- Requires extra variable handling
- Repeats logic
- Slightly longer code

---

## ✔ Walrus Operator Version

```python
foods = []

while (food := input("What food do you like? ")) != "quit":
    foods.append(food)
```

---

## How it works

```
1. Take input
2. Assign to 'food'
3. Check condition
4. Continue or break loop
```

---

## 4. Another Example: List Processing

---

### Example: Popping elements

```python
numbers = [1, 2, 3, 4, 5]

while (n := len(numbers)) > 0:
    print(numbers.pop())
```

---

## Output

```
5
4
3
2
1
```

---

## What’s happening?

Each loop:
- `n = len(numbers)`
- Condition checks `n > 0`
- Last element is removed

---

## 5. Where Walrus Operator is Useful

✔ While loops  
✔ Input handling  
✔ Regex matches  
✔ Filtering data  
✔ Reducing repeated function calls  

---

## 6. Where NOT to Use It

❌ Overcomplicating simple code  
❌ Reducing readability  
❌ Nested confusing expressions  

---

## 7. Key Takeaways

✔ `:=` assigns + evaluates in one step  
✔ Introduced in Python 3.8  
✔ Best for reducing repetition  
✔ Improves loop efficiency and readability (when used correctly)  

---

## Final Idea

The walrus operator helps you write **clean, compact, and efficient Python code by combining assignment and condition checking into a single expression**.