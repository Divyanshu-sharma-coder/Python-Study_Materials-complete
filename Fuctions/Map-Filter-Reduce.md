# Map, Filter, and Reduce in Python

In Python, **`map()`**, **`filter()`**, and **`reduce()`** are powerful functional programming utilities designed to perform bulk operations on iterable data structures such as lists, tuples, and sets.

These functions eliminate the need for explicit loops in many situations, resulting in cleaner, more readable, and often more efficient code.

Because all three functions accept another function as an argument, they are classified as **Higher-Order Functions**.

---

## 1. The `map()` Function

The **`map()`** function applies a transformation function to **every element** in an iterable and returns a map object containing the transformed values.

### Syntax

```python
map(function, iterable)
```

### Parameters

| Parameter | Description |
|------------|------------|
| `function` | Function applied to each element |
| `iterable` | Sequence being processed |

### Return Value

```text
Map Object (Iterator)
```

Usually converted into a list:

```python
list(map(...))
```

---

## Example: Cubing Every Number

Suppose we want to calculate:

```text
x³
```

for every value in a list.

### Traditional Approach

```python
numbers = [1, 2, 4, 6, 3]

cubed_loop = []

for x in numbers:
    cubed_loop.append(x * x * x)

print(cubed_loop)
```

### Output

```text
[1, 8, 64, 216, 27]
```

---

### Using `map()`

```python
numbers = [1, 2, 4, 6, 3]

cubed_map = list(
    map(
        lambda x: x * x * x,
        numbers
    )
)

print(cubed_map)
```

### Output

```text
[1, 8, 64, 216, 27]
```

---

### Visual Flow

```text
Input List

[1, 2, 4, 6, 3]

        │
        ▼

lambda x: x³

        │
        ▼

[1, 8, 64, 216, 27]
```

---

## 2. The `filter()` Function

The **`filter()`** function selects elements from an iterable based on a condition.

The condition function must return either:

```python
True
```

or

```python
False
```

Elements producing:

```python
True
```

are kept.

Elements producing:

```python
False
```

are discarded.

---

### Syntax

```python
filter(function, iterable)
```

### Parameters

| Parameter | Description |
|------------|------------|
| `function` | Predicate function returning True/False |
| `iterable` | Sequence being filtered |

---

## Example: Keep Values Greater Than 3

### Input

```python
numbers = [1, 2, 4, 6, 3]
```

### Using `filter()`

```python
filtered_result = list(
    filter(
        lambda x: x > 3,
        numbers
    )
)

print(filtered_result)
```

### Output

```text
[4, 6]
```

---

### Visual Flow

```text
Input

[1, 2, 4, 6, 3]

        │
        ▼

Condition

x > 3

        │
        ▼

[4, 6]
```

---

## Another Example: Extract Even Numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)

print(even_numbers)
```

### Output

```text
[2, 4, 6]
```

---

## 3. The `reduce()` Function

Unlike `map()` and `filter()`, which return collections of values, **`reduce()`** repeatedly combines elements together until only one final value remains.

It reduces an entire iterable into a single scalar result.

---

## Import Requirement

`reduce()` is located inside Python's `functools` module.

You must import it first:

```python
from functools import reduce
```

---

### Syntax

```python
reduce(function, iterable)
```

### Parameters

| Parameter | Description |
|------------|------------|
| `function` | Two-argument function |
| `iterable` | Sequence to aggregate |

---

## Example: Sum All Elements

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total_sum = reduce(
    lambda x, y: x + y,
    numbers
)

print(total_sum)
```

### Output

```text
15
```

---

## Step-by-Step Execution

Input:

```python
[1, 2, 3, 4, 5]
```

### Iteration 1

```text
1 + 2 = 3
```

### Iteration 2

```text
3 + 3 = 6
```

### Iteration 3

```text
6 + 4 = 10
```

### Iteration 4

```text
10 + 5 = 15
```

### Final Result

```text
15
```

---

### Visual Flow

```text
[1, 2, 3, 4, 5]

1 + 2 → 3

3 + 3 → 6

6 + 4 → 10

10 + 5 → 15

Final Output → 15
```

---

## Example: Find Maximum Value

```python
from functools import reduce

numbers = [10, 50, 20, 80, 30]

maximum = reduce(
    lambda x, y: x if x > y else y,
    numbers
)

print(maximum)
```

### Output

```text
80
```

---

## Comparison Table

| Function | Syntax | Purpose | Output Type |
|-----------|---------|---------|------------|
| `map()` | `map(function, iterable)` | Transform every element | Iterable of transformed values |
| `filter()` | `filter(function, iterable)` | Keep elements matching a condition | Iterable of filtered values |
| `reduce()` | `reduce(function, iterable)` | Combine all elements into one result | Single scalar value |

---

## Input vs Output Behavior

### `map()`

```text
Input:
[1, 2, 3]

Operation:
x²

Output:
[1, 4, 9]
```

---

### `filter()`

```text
Input:
[1, 2, 3, 4]

Condition:
x > 2

Output:
[3, 4]
```

---

### `reduce()`

```text
Input:
[1, 2, 3, 4]

Operation:
Addition

Output:
10
```

---

## Combined Example

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Step 1: Square all values
squared = list(
    map(
        lambda x: x * x,
        numbers
    )
)

# Step 2: Keep values > 10
filtered = list(
    filter(
        lambda x: x > 10,
        squared
    )
)

# Step 3: Sum remaining values
result = reduce(
    lambda x, y: x + y,
    filtered
)

print(result)
```

### Execution Flow

```text
Original List

[1, 2, 3, 4, 5]

       │
       ▼

map(x²)

[1, 4, 9, 16, 25]

       │
       ▼

filter(x > 10)

[16, 25]

       │
       ▼

reduce(+)

41
```

---

## Key Takeaways

### `map()`

✅ Transforms every element

✅ Preserves collection size

✅ Returns an iterator

---

### `filter()`

✅ Removes unwanted values

✅ Uses a boolean condition

✅ May reduce collection size

---

### `reduce()`

✅ Aggregates values

✅ Produces a single result

✅ Useful for sums, products, maximums, minimums, and custom accumulations

---

## Recommended Professional Usage

Use:

```python
map()
```

when every element needs modification.

Use:

```python
filter()
```

when elements must be screened by a condition.

Use:

```python
reduce()
```

when many values must be combined into one final result.

Together, these three functions form the foundation of functional programming patterns in Python.