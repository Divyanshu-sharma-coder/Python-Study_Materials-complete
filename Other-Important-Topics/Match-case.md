# Match Case Statements in Python

## 1. Introduction to `match-case`

The `match-case` statement was introduced in **Python 3.10**.

It provides **structural pattern matching**, similar to:
- `switch-case` in C / C++
- `if-elif-else` chains (but cleaner)

---

## Why it is useful?

✔ Reduces long `if-elif` chains  
✔ Improves readability  
✔ Makes code more structured  

---

## ⚠ Version Requirement

```
Python 3.10+
```

If you run it in older versions:

```
SyntaxError
```

---

## 2. Key Difference from C/C++

### In C/C++:
- Requires `break`
- Otherwise → fall-through occurs

---

### In Python:

✔ No fall-through  
✔ Only first matching case executes  
✔ Automatically exits after match  

---

## 3. Basic Syntax

---

## Example

```python
x = int(input("Enter value of x: "))

match x:
    case 0:
        print("x is zero")

    case 4:
        print("x is four")

    case _:
        print("x is something else")
```

---

## 4. Wildcard Case (`case _`)

The underscore `_` acts as a **default case**.

---

## Meaning

```
case _  → matches everything not matched above
```

---

## Example Behavior

If no case matches:

```
Fallback case runs
```

---

## 5. How Execution Works

Example:

```python
match x:
    case 0:
        ...
    case 4:
        ...
    case _:
        ...
```

---

## Flow

```
Check case 0 → no match
Check case 4 → no match
Run case _   → match found
Exit match block
```

---

## 6. Match Case with Conditions (Guards)

You can add conditions using `if`.

---

## Example

```python
x = int(input("Enter value: "))

match x:
    case 0:
        print("x is zero")

    case _ if x != 90:
        print("x is not 90")

    case _ if x != 80:
        print("x is not 80")

    case _:
        print("final fallback")
```

---

## 7. How Guards Work

Each case checks:

```
1. Pattern match
2. Condition (if present)
```

Only if BOTH are true → case executes.

---

## Example Input: 56

Execution:

```
case 0 → no match
case _ if x != 90 → True → executes
exit match
```

---

## 8. Key Features of `match-case`

✔ Cleaner alternative to `if-elif`  
✔ Supports patterns + conditions  
✔ No break required  
✔ First-match wins  

---

## 9. When to Use It

✔ Menu systems  
✔ Command parsing  
✔ State machines  
✔ Pattern-based logic  

---

## 10. When NOT to Use It

❌ Simple 1–2 condition checks  
❌ Overcomplicated nested patterns  
❌ When `if-else` is clearer  

---

## Final Idea

`match-case` in Python is a **modern control-flow system that simplifies decision-making by matching patterns instead of manually checking conditions one by one**.