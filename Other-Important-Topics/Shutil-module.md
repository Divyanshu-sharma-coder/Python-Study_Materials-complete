# The `shutil` Module in Python

## 1. What is the `shutil` Module?

The `shutil` (Shell Utilities) module is a **built-in Python library** used for high-level file operations.

It is mainly used for:
- Copying files
- Moving files
- Copying folders
- Deleting directories
- Archiving files

---

## Difference: `os` vs `shutil`

| Module | Purpose |
|:------:|---------|
| `os` | Low-level OS operations (paths, environment, files) |
| `shutil` | High-level file operations (copy, move, delete, archive) |

---

## Real-World Use Case

Imagine:
- Thousands of folders
- Scattered files everywhere
- Manual sorting is impossible

✔ `shutil` automates all of this in seconds.

---

## 2. Core Functions of `shutil`

---

## A. `shutil.copy()`

Copies a file from source to destination.

### Syntax:
```python
shutil.copy(src, dst)
```

### Example:

```python
import shutil

shutil.copy("main.py", "main_backup.py")
```

### Notes:
✔ Copies file content  
✔ Does NOT copy metadata (timestamps, etc.)  

---

## B. `shutil.copy2()`

Copies file + preserves metadata.

### Example:

```python
import shutil

shutil.copy2("main.py", "main_exact_backup.py")
```

---

## Difference:

| Function | Copies Content | Copies Metadata |
|:--------:|:--------------:|:---------------:|
| `copy()` | ✔ | ❌ |
| `copy2()` | ✔ | ✔ |

---

## C. `shutil.copytree()`

Copies an entire directory recursively.

### Example:

```python
import shutil

shutil.copytree("my_folder", "backup_folder")
```

---

## Important Rule:
✔ Destination folder must NOT exist

---

## D. `shutil.move()`

Moves files or folders from one location to another.

### Example:

```python
import shutil

shutil.move("nested_folder/data.txt", "data.txt")
```

---

## What it does:
- Moves file
- Or renames file if same directory

---

## E. `shutil.rmtree()`

Deletes entire directory tree permanently.

### Example:

```python
import shutil

shutil.rmtree("backup_folder")
```

---

## ⚠ Warning

```
This deletion is PERMANENT
No recycle bin
No recovery
```

---

## 3. Deleting Single Files

❌ `shutil.rmtree()` cannot delete files

✔ Use `os.remove()` instead

---

### Example:

```python
import os

os.remove("data.txt")
```

---

## 4. Practical Automation Use Case

### Example: Auto Folder Generator

Used in:
- Video editing pipelines
- Software projects
- Daily content creation systems

---

## Idea

Instead of manually creating folders like:

```
Day_1
Day_2
Day_3
...
Day_100
```

You automate it using `shutil.copytree()`.

---

## 5. Key Functions Summary

| Function | Purpose |
|:--------:|---------|
| `copy()` | Copy file |
| `copy2()` | Copy file + metadata |
| `copytree()` | Copy folder |
| `move()` | Move/rename |
| `rmtree()` | Delete folder |

---

## 6. Key Takeaways

✔ `shutil` = high-level file automation tool  
✔ Used for copying, moving, deleting directories  
✔ Safer and faster than manual file handling  
✔ Extremely useful for automation scripts  

---

## Final Idea

The `shutil` module turns Python into a **file automation engine**, allowing you to manage large-scale file systems with minimal code and maximum efficiency.