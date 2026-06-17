# Local vs Global Variables in Python

Understanding variable scope determines where your data is accessible, where it is protected, and how long it survives in memory while your program executes.

---

## 1. Defining Scope: Local vs Global

### Local Variables

A **local variable** is a variable defined inside a function.

**Characteristics:**
- Exists only within the function where it is created.
- Cannot be accessed outside the function.
- Created when the function is called.
- Destroyed when the function finishes execution.

### Example

```python
def my_function():
    y = 5
    print(y)

my_function()
```

---

### Global Variables

A **global variable** is defined outside all functions.

**Characteristics:**
- Accessible throughout the program.
- Can be read inside functions.
- Remains in memory until the program terminates.

### Example

```python
x = 10

def display():
    print(x)

display()
print(x)
```

---

## 2. Variable Isolation Rules

When you assign a variable inside a function, Python automatically treats it as a local variable, even if a global variable with the same name already exists.

### Example

```python
x = 10  # Global Variable

def my_function():
    y = 5
    x = 4  # Local Variable

    print(f"Inside function: y = {y}")
    print(f"Inside function: x = {x}")

my_function()

print(f"Outside function: x = {x}")
```

### Output

```text
Inside function: y = 5
Inside function: x = 4
Outside function: x = 10
```

### Why?

Python creates a new local variable named `x` inside the function instead of modifying the global variable.

---

## 3. The `global` Keyword

To modify a global variable inside a function, use the `global` keyword.

### Example

```python
x = 10

def modify_global():
    global x
    x = 5

    print(f"Inside function: x = {x}")

print(f"Before function call: x = {x}")

modify_global()

print(f"After function call: x = {x}")
```

### Output

```text
Before function call: x = 10
Inside function: x = 5
After function call: x = 5
```

### How It Works

```python
global x
```

This statement tells Python:

> "Do not create a local variable named `x`. Use the global variable instead."

---

## 4. Local Variable Destruction

Local variables disappear after the function finishes execution.

### Example

```python
def my_function():
    y = 100
    print(y)

my_function()

# print(y)
```

### Result

```text
NameError: name 'y' is not defined
```

The variable `y` existed only inside the function.

---

## 5. Why Excessive Global Variables Are Discouraged

Although Python allows global variables, professional developers avoid modifying them frequently.

### Problems

#### 1. Side Effects

Multiple functions changing the same variable can produce unexpected behavior.

```python
score = 0

def add_bonus():
    global score
    score += 50
```

Tracking changes becomes difficult in large applications.

---

#### 2. Harder Debugging

A bug may originate from any function that modifies the global variable.

---

#### 3. Reduced Readability

Functions become dependent on outside variables instead of working independently.

---

## 6. Professional Alternative: Return Values

Instead of modifying globals, pass data into functions and return results.

### Recommended Approach

```python
def calculate_new_value(current_value):
    return current_value + 5

x = 10

x = calculate_new_value(x)

print(x)
```

### Output

```text
15
```

This approach:
- Makes functions predictable.
- Improves testing.
- Reduces hidden side effects.
- Improves code readability.

---

## Summary Table

| Property | Local Variable | Global Variable |
|-----------|---------------|----------------|
| Declaration Location | Inside a function | Outside all functions |
| Visibility | Only inside the function | Entire program |
| Lifetime | Temporary | Entire program execution |
| Memory | Destroyed after function returns | Remains until program ends |
| Accessible Outside Function | ❌ No | ✅ Yes |
| Modification Inside Function | Directly | Requires `global` keyword |

---

## Key Takeaway

Python uses **scope** to control where variables can be accessed.

- **Local variables** are temporary and exist only inside functions.
- **Global variables** are accessible throughout the program.
- Functions should generally avoid modifying global variables.
- The preferred professional approach is to pass values as arguments and return new values instead of relying on global state.