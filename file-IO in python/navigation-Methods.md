# Advanced File Navigation in Python: `seek()`, `tell()`, and `truncate()`

When working with standard file handling tools, operations like `read()` or `write()` process data sequentially from beginning to end.

However, if you need to manipulate a specific portion of a large text document or binary stream—such as updating a character at byte position 500—reading and rewriting the entire file becomes inefficient.

Python provides built-in methods to precisely control and manipulate the **file cursor** (also known as the file pointer) anywhere inside a file stream.

---

## 1. Setting the Pointer Position (`seek()`)

The **`seek()`** method allows you to move the file cursor to a specific position.

The position is specified as an offset measured in **bytes** from the beginning of the file.

### Syntax

```python
file.seek(offset)
```

### Parameters

| Parameter | Description |
|------------|------------|
| `offset` | Number of bytes from the beginning of the file |

---

### Code Demonstration

Assume we have a file named `sample.txt` containing:

```text
0123456789abcdef
```

#### Example

```python
with open("sample.txt", "r") as f:
    # Move cursor to byte position 10
    f.seek(10)

    # Read next 5 characters
    data = f.read(5)

    print(data)
```

#### Output

```text
abcde
```

### Explanation

File contents:

```text
0123456789abcdef
          ^
          Cursor at index 10
```

After calling:

```python
f.seek(10)
```

the cursor skips the first 10 bytes and begins reading from the character `a`.

---

## 2. Tracking Cursor Position (`tell()`)

When processing files, it is often useful to know the current cursor position.

The **`tell()`** method returns the current location of the file pointer as an integer.

### Syntax

```python
file.tell()
```

### Return Value

```text
Current cursor position in bytes
```

---

### Code Demonstration

```python
with open("sample.txt", "r") as f:

    # Read first 4 bytes
    f.read(4)

    # Check current position
    position = f.tell()

    print(f"Current file pointer position: {position}")

    # Move 3 bytes ahead
    f.seek(position + 3)

    print(f"New pointer position: {f.tell()}")
```

#### Output

```text
Current file pointer position: 4
New pointer position: 7
```

---

### Visual Representation

Initial File:

```text
0123456789abcdef
^^^^
```

After:

```python
f.read(4)
```

Cursor Position:

```text
0123456789abcdef
    ^
```

`tell()` returns:

```text
4
```

---

## 3. Resizing and Trimming Files (`truncate()`)

The **`truncate()`** method changes the size of a file.

If the file is larger than the specified size, the extra data is permanently removed.

If the file is smaller, operating-system behavior may vary (often padding with null bytes).

---

### Syntax

```python
file.truncate(size)
```

### Parameters

| Parameter | Description |
|------------|------------|
| `size` | Desired file size in bytes |

---

### Important Requirement

> ⚠️ The file must be opened in a writable mode such as:

```python
"w"
"a"
"r+"
```

Attempting to truncate a file opened in read-only mode will raise an error.

---

### Code Demonstration

#### Step 1: Create File

```python
with open("truncate_demo.txt", "w") as f:
    f.write("Hello World!")
```

Current File Contents:

```text
Hello World!
```

---

#### Step 2: Truncate File

```python
with open("truncate_demo.txt", "a") as f:
    f.truncate(5)
```

---

#### Step 3: Verify Result

```python
with open("truncate_demo.txt", "r") as f:
    print(f.read())
```

#### Output

```text
Hello
```

---

### Visual Representation

Before Truncation:

```text
Hello World!
```

Byte Count:

```text
12 Bytes
```

After:

```python
f.truncate(5)
```

Result:

```text
Hello
```

Everything after the first 5 bytes is permanently removed.

---

## Summary Reference Table

| Method | Syntax Parameter | Primary Function |
|----------|-----------------|------------------|
| `seek(offset)` | Integer byte offset | Moves the file cursor to a specific position |
| `tell()` | None | Returns the current cursor position |
| `truncate(size)` | Integer byte size | Resizes or clips the file to a specified size |

---

## Combined Example

```python
with open("sample.txt", "r") as f:

    print("Initial Position:", f.tell())

    f.seek(5)

    print("After seek():", f.tell())

    data = f.read(3)

    print("Data Read:", data)

    print("Current Position:", f.tell())
```

### Possible Output

```text
Initial Position: 0
After seek(): 5
Data Read: 567
Current Position: 8
```

---

## Key Takeaways

### `seek()`

- Moves the file cursor to a specific location.
- Allows random access within a file.
- Useful for large files and binary data.

### `tell()`

- Returns the current cursor position.
- Helpful when tracking parsing progress.
- Commonly used alongside `seek()`.

### `truncate()`

- Changes the file size.
- Removes data beyond a specified limit.
- Requires a writable file mode.

---

## Recommended Professional Usage

### Random File Access

```python
with open("data.txt", "r") as f:
    f.seek(100)
    print(f.read(20))
```

### Cursor Tracking

```python
with open("data.txt", "r") as f:
    print(f.tell())
```

### File Trimming

```python
with open("log.txt", "a") as f:
    f.truncate(1000)
```

These methods provide low-level control over file streams and are essential when working with large datasets, binary files, log processing systems, and advanced storage operations.