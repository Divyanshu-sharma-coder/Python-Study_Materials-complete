# The `os` Module in Python

The built-in **`os` (Operating System)** module provides a suite of functions that allow Python scripts to interact directly with the operating system, file system, and directories.

Using the `os` module, you can automate tasks such as creating folders, renaming files, navigating directories, and inspecting file structures.

---

## 1. Directory and Path Lifecycle Management

### Creating Folders (`os.mkdir()`)

To create a single folder:

```python
import os

os.mkdir("data")
```

### Checking Existence Safely (`os.path.exists()`)

Creating an already existing directory causes a `FileExistsError`.

```python
import os

if not os.path.exists("data"):
    os.mkdir("data")
```

### Bulk Folder Creation

```python
import os

for i in range(1, 101):
    folder_path = f"data/tutorial {i}"

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
```

---

## 2. Mass Renaming Workspaces (`os.rename()`)

The `os.rename()` function renames or moves files and directories.

### Example

```python
import os

for i in range(1, 101):
    source = f"data/tutorial {i}"
    destination = f"data/Day {i}"

    if os.path.exists(source):
        os.rename(source, destination)
```

---

## 3. Directory Inspection (`os.listdir()`)

The `os.listdir()` function returns a list of all files and folders inside a directory.

### Example

```python
import os

folders = os.listdir("data")

print(folders)
```

### Traversing Subdirectories

```python
import os

folders = os.listdir("data")

for folder in folders:
    subpath = f"data/{folder}"
    print(f"Contents of {folder}:")
    print(os.listdir(subpath))
```

---

## 4. Current Working Directory (CWD)

Every Python script runs inside a Current Working Directory (CWD).

### Get Current Working Directory (`os.getcwd()`)

```python
import os

print(os.getcwd())
```

### Change Working Directory (`os.chdir()`)

```python
import os

print("Before:", os.getcwd())

os.chdir("/Users")

print("After:", os.getcwd())
```

### Important Warning

If you change the working directory using `os.chdir()`, all future relative paths will be evaluated relative to the new directory.

Example:

```python
os.chdir("/Users")

# Python now searches relative to /Users
os.listdir("data")
```

If the `data` folder does not exist inside `/Users`, Python will raise a `FileNotFoundError`.

---

## Command Reference

| Command | Return Type | Purpose |
|----------|------------|----------|
| `os.mkdir("name")` | `None` | Creates a directory |
| `os.path.exists("path")` | `bool` | Checks if a path exists |
| `os.rename("old", "new")` | `None` | Renames or moves files/folders |
| `os.listdir("folder")` | `list` | Lists directory contents |
| `os.getcwd()` | `str` | Returns current working directory |
| `os.chdir("path")` | `None` | Changes working directory |

---

## Key Takeaway

The `os` module is Python's bridge to the operating system. It enables automation of repetitive file-system tasks such as:

- Creating directories
- Renaming files and folders
- Inspecting directory contents
- Navigating file systems
- Building automation scripts

Mastering the `os` module is an important step toward scripting, automation, DevOps, cybersecurity, and backend development.