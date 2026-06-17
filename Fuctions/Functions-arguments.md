# Function Arguments in Python

## 1. Introduction to Function Arguments

Function arguments are values passed into a function when it is called.

They allow functions to work with **dynamic input instead of fixed data**.

---

## 2. Types of Function Arguments

Python provides **4 main types** of function arguments:

```
1. Default Arguments
2. Keyword Arguments
3. Required Arguments
4. Variable-Length Arguments
```

---

# A. Default Arguments

Default arguments provide fallback values if no input is given.

---

## Example

```python
def calculate_average(a=9, b=1):
    print("Average:", (a + b) / 2)


calculate_average()        # uses default values
calculate_average(1, 5)    # overrides both
calculate_average(5)       # overrides only a
```

---

## How it works

```
If value not passed → use default
```

---

# B. Keyword Arguments

Keyword arguments allow you to specify parameter names explicitly.

---

## Example

```python
def calculate_average(a, b):
    print("Average:", (a + b) / 2)


calculate_average(b=9, a=21)
```

---

## Key Feature

✔ Order does NOT matter  
✔ Clear readability  

---

# C. Required Arguments

Required arguments must always be provided.

---

## Example

```python
def calculate_average(a, b=1):
    print("Average:", (a + b) / 2)
```

---

## Incorrect usage

```python
# calculate_average()  ❌ Error (missing required argument)
```

---

## Correct usage

```python
calculate_average(5)
```

---

# D. Variable-Length Arguments

Used when number of inputs is unknown.

---

# I. *args (Positional Arguments)

All extra values are stored in a tuple.

---

## Example

```python
def calculate_bulk_average(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


print(calculate_bulk_average(5, 6, 7, 1))
```

---

## Output

```
4.75
```

---

## How it works

```
(5, 6, 7, 1) → stored as tuple
```

---

# II. **kwargs (Keyword Arguments)

Stores arguments as a dictionary.

---

## Example

```python
def print_user_profile(**data):
    print(type(data))
    print("Hello", data.get("first_name"), data.get("last_name"))


print_user_profile(
    first_name="Amy",
    middle_name="Agarwal",
    last_name="Jain"
)
```

---

## Output type

```
<class 'dict'>
```

---

## How it works

```
key=value pairs → dictionary
```

---

## 3. The `return` Statement

The `return` statement:

✔ Sends value back to caller  
✔ Stops function execution immediately  

---

## Example

```python
def compute_average(*numbers):
    total = 0

    for num in numbers:
        total += num

    return total / len(numbers)


c = compute_average(5, 6, 7, 1)
print(c)
```

---

## Key Behavior

```
return → exit function immediately
```

---

## If no return?

Function returns:

```
None
```

---

## 4. Summary Table

| Type | Symbol | Behavior |
|------|--------|----------|
| Default | `a=10` | Uses fallback value |
| Keyword | `a=5` | Order not required |
| Required | `a` | Must be provided |
| *args | `*args` | Tuple input |
| **kwargs | `**kwargs` | Dictionary input |

---

## Final Idea

Function arguments in Python make functions **highly flexible, reusable, and powerful by allowing different ways of passing data dynamically**.