# f-Strings in Python

Introduced in Python 3.6, **f-strings** (formatted string literals) offer a highly efficient, elegant, and readable way to insert variables and expressions dynamically inside string components.

---

## 1. Evolution of String Formatting

### The Old `.format()` Method

Before f-strings, developers commonly used the `.format()` method to inject variable values into placeholders `{}`.

```python
name = "Harry"
country = "India"

txt = "Hey, my name is {} and I am from {}"

print(txt.format(name, country))

# Output:
# Hey, my name is Harry and I am from India
```

### Index-Based Placeholders

If variables were passed in a different order, you could specify index values.

```python
name = "Harry"
country = "India"

txt = "Hey, my name is {1} and I am from {0}"

print(txt.format(country, name))

# Output:
# Hey, my name is Harry and I am from India
```

### Drawback of `.format()`

As the number of variables increases, tracking placeholder indexes becomes difficult and reduces readability.

---

## 2. The f-String Approach

By placing an `f` before the opening quotation mark, Python automatically evaluates expressions enclosed in curly braces `{}`.

```python
name = "Harry"
country = "India"

print(f"Hey, my name is {name} and I am from {country}")

# Output:
# Hey, my name is Harry and I am from India
```

### Why f-Strings?

- Cleaner syntax
- Better readability
- Faster to write
- Easier debugging
- Modern Python standard

---

## 3. Formatting Values (Decimal Precision)

You can control how values are displayed using format specifiers.

### Limiting Floats to 2 Decimal Places

```python
price = 49.099999

txt = f"For only {price:.2f} dollars!"

print(txt)

# Output:
# For only 49.10 dollars!
```

### Format Syntax

```python
{variable:.2f}
```

Where:

- `:` begins the formatting section
- `.2f` means display exactly 2 digits after the decimal point

---

## 4. Retaining Literal Curly Braces `{}`

Curly braces normally indicate expressions in f-strings.

To display actual braces, escape them by doubling them.

### Printing Literal Braces

```python
print(f"We use f-strings like this: My name is {{name}}")

# Output:
# We use f-strings like this: My name is {name}
```

### Rule

| Input | Output |
|---------|---------|
| `{{` | `{` |
| `}}` | `}` |

---

## Summary

| Feature / Method | Syntax Example | Key Advantage |
|------------------|---------------|---------------|
| Old Formatting | `"{} {}".format(a, b)` | Functional but harder to manage |
| Indexed Formatting | `"{1} {0}".format(a, b)` | Allows custom ordering |
| Basic f-string | `f"Hello {name}"` | Clean and highly readable |
| Decimal Control | `f"{price:.2f}"` | Controls float precision |
| Escaping Braces | `f"{{text}}"` | Prints literal curly braces |

---

## Key Takeaway

f-strings are the modern and preferred way to format strings in Python. They make code cleaner, more readable, and easier to maintain. Whenever you need to combine variables with text, f-strings should generally be your first choice.