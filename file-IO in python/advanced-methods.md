# Advanced File I/O Methods in Python: `readline()` and `writelines()`

Building upon standard text stream operations, Python provides precise line-by-line reading and structured multi-line sequence dumping capabilities.

These operations are particularly powerful when parsing comma-separated tracking files, handling tabular analytical datasets, or bulk-exporting array logs.

---

## 1. Line-by-Line Parsing (`readline()`)

The `.read()` method loads an entire file's content into memory as a single block.

For very large text logs, this can consume significant memory.

In contrast, the **`.readline()`** method retrieves **one line at a time** up to the next newline (`\n`) character.

---

### Implementation Structure

When calling `.readline()` repeatedly inside a loop, Python continues scanning the file until it reaches the End of File (EOF).

At EOF, `.readline()` returns an empty string (`""`).

This behavior allows us to terminate the loop safely.

#### Example

```python
# Iteratively parsing a text file line by line
with open("myfile.txt", "r") as f:
    while True:
        line = f.readline()

        if not line:
            break  # EOF reached

        print(line, end="")  # Prevents extra blank lines
```

---

### Analytical Use Case: Parsing Delimited Rows

Consider a file named `marks.txt` containing student scores.

#### File Contents

```text
56,45,67
12,34,63
13,64,23
```

Each line represents:

```text
Math,Science,English
```

You can use `.readline()` together with `.split()` to extract and process the values.

#### Example

```python
with open("marks.txt", "r") as f:
    student_idx = 1

    while True:
        line = f.readline()

        if not line:
            break

        # Split row into separate values
        scores = line.split(",")

        # Convert strings into integers
        math = int(scores[0])
        science = int(scores[1])
        english = int(scores[2])

        print(f"Student #{student_idx}")
        print(f"Math Score: {math}")
        print(f"Science Score: {science}")
        print(f"English Score: {english}")
        print()

        student_idx += 1
```

---

## 2. Mass Bulk Array Exporting (`writelines()`)

The `.writelines()` method allows you to write an iterable collection of strings (such as a list or tuple) into a file in a single operation.

---

### Important Behavior

> ⚠️ The name `writelines()` can be misleading.

It **does not automatically add newline characters (`\n`)** between elements.

If your strings do not contain `\n`, everything will be written continuously on a single line.

---

### Incorrect Example

```python
lines = [
    "Line 1",
    "Line 2",
    "Line 3"
]

with open("output.txt", "w") as f:
    f.writelines(lines)
```

#### Output File

```text
Line 1Line 2Line 3
```

---

### Correct Example

```python
lines_list = [
    "Line 1 content block configuration.\n",
    "Line 2 secondary validation parameter.\n",
    "Line 3 final workspace terminal confirmation.\n"
]

with open("export.txt", "w") as f:
    f.writelines(lines_list)
```

#### Output File

```text
Line 1 content block configuration.
Line 2 secondary validation parameter.
Line 3 final workspace terminal confirmation.
```

---

## Summary Command Reference

| Command Syntax | Operation Type | Behavior |
|---------------|---------------|----------|
| `f.readline()` | Read | Retrieves text from the current file pointer up to the next newline (`\n`). Returns `""` at EOF. |
| `f.writelines(iterable)` | Write | Writes a collection of strings to a file without automatically inserting newline characters. |

---

## Key Takeaways

### `readline()`

- Reads one line at a time.
- Memory efficient for large files.
- Returns an empty string at EOF.
- Commonly used with loops.

### `writelines()`

- Writes multiple strings at once.
- Accepts lists, tuples, or other iterables.
- Does not insert newline characters automatically.
- Requires explicit `\n` when multi-line output is desired.

---

## Recommended Professional Usage

### Reading Large Files

```python
with open("large_log.txt", "r") as f:
    while True:
        line = f.readline()

        if not line:
            break

        process(line)
```

### Writing Multiple Lines

```python
data = [
    "First Entry\n",
    "Second Entry\n",
    "Third Entry\n"
]

with open("data.txt", "w") as f:
    f.writelines(data)
```

These techniques provide efficient and scalable file handling for real-world Python applications.