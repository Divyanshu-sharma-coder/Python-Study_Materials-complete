# Understanding `if __name__ == "__main__"` in Python

The statement:

```python
if __name__ == "__main__":
```

is one of the most important patterns in Python.

It allows a file to behave differently depending on whether it is:

1. Executed directly by Python.
2. Imported into another script as a module.

This makes Python files reusable, modular, and safe from accidental execution.

---

## 1. The Problem Without `__name__`

Consider the following file.

### `harry.py`

```python
def welcome():
    print("Hey, you are welcome from Harry!")

welcome()
```

---

### `main.py`

```python
import harry

harry.welcome()
```

---

## What Happens?

Run:

```bash
python main.py
```

Output:

```text
Hey, you are welcome from Harry!
Hey, you are welcome from Harry!
```

---

### Why Twice?

When Python encounters:

```python
import harry
```

it performs:

1. Opens `harry.py`
2. Executes all top-level code
3. Creates the module object

Since:

```python
welcome()
```

exists globally, it runs immediately.

Then:

```python
harry.welcome()
```

runs again.

Result:

```text
Two executions
```

---

## Real Danger

Imagine this code:

```python
connect_to_database()

delete_temp_files()

send_email()
```

If these statements exist globally inside a module:

```python
import module
```

would execute them automatically.

This is extremely dangerous.

---

## 2. The Hidden Variable `__name__`

Every Python file automatically receives a special variable:

```python
__name__
```

Python assigns a value to it depending on how the file is launched.

---

### Scenario 1: Direct Execution

File:

```python
harry.py
```

```python
print(__name__)
```

Run:

```bash
python harry.py
```

Output:

```text
__main__
```

---

### Scenario 2: Imported

File:

```python
main.py
```

```python
import harry
```

Output:

```text
harry
```

---

Python automatically sets:

```python
__name__ = "harry"
```

because the file is being used as a module.

---

## Visual Representation

Direct Execution:

```text
harry.py
    ↓
Python
    ↓
__name__ = "__main__"
```

---

Import Execution:

```text
main.py
    ↓
import harry
    ↓
__name__ = "harry"
```

---

## 3. The Solution

Use:

```python
if __name__ == "__main__":
```

to protect code that should run only when the file is executed directly.

---

### Updated `harry.py`

```python
def welcome():
    print("Hey, you are welcome from Harry!")

if __name__ == "__main__":
    welcome()
```

---

## Running Directly

```bash
python harry.py
```

Python sets:

```python
__name__ = "__main__"
```

Condition:

```python
if "__main__" == "__main__":
```

Result:

```python
True
```

Output:

```text
Hey, you are welcome from Harry!
```

---

## Running Through Import

```python
import harry
```

Python sets:

```python
__name__ = "harry"
```

Condition:

```python
if "harry" == "__main__":
```

Result:

```python
False
```

The protected code does not execute.

Only function definitions are loaded.

---

## 4. Why This Pattern Exists

A Python file can serve two purposes simultaneously:

### As a Program

```bash
python calculator.py
```

Runs directly.

---

### As a Library

```python
import calculator
```

Used by another script.

---

The `if __name__ == "__main__"` block allows one file to support both roles safely.

---

## 5. Professional Example

### `calculator.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(10, 4))
```

---

Direct execution:

```bash
python calculator.py
```

Output:

```text
8
6
```

---

Importing:

```python
import calculator

print(calculator.add(7, 2))
```

Output:

```text
9
```

The test code never runs.

---

## 6. Why Professionals Use It

### Unit Testing

```python
if __name__ == "__main__":
    run_tests()
```

---

### Debugging

```python
if __name__ == "__main__":
    print("Debug Mode")
```

---

### Example Usage

```python
if __name__ == "__main__":
    demo()
```

---

### Command-Line Scripts

```python
if __name__ == "__main__":
    main()
```

This is the most common pattern.

---

## 7. The Industry Standard Structure

```python
def function1():
    pass

def function2():
    pass

def main():
    print("Program Started")
    function1()
    function2()

if __name__ == "__main__":
    main()
```

---

### Why Create `main()`?

Benefits:

- Cleaner architecture
- Easier debugging
- Easier testing
- Easier maintenance

This structure appears in:

- Data Science projects
- Machine Learning pipelines
- Backend systems
- Automation scripts
- Open-source repositories

---

## Execution Flow Diagram

```text
File Starts
     │
     ▼
Load Functions
     │
     ▼
Check __name__
     │
 ┌───┴────┐
 │        │
 ▼        ▼
Direct   Imported
Run      Skip
main()   main()
```

---

## Common Beginner Mistake

### Wrong

```python
def main():
    print("Hello")

main()
```

This runs every time the module is imported.

---

### Correct

```python
def main():
    print("Hello")

if __name__ == "__main__":
    main()
```

Now it runs only when intended.

---

## Summary Table

| Situation | Value of `__name__` | Main Block Runs? |
|------------|--------------------|------------------|
| `python script.py` | `"__main__"` | ✅ Yes |
| `import script` | `"script"` | ❌ No |

---

## Key Takeaway

The statement:

```python
if __name__ == "__main__":
```

creates a boundary between code meant for direct execution and code meant for reuse through imports.

It allows a Python file to function both as:

- A standalone executable program
- A reusable module

without causing accidental execution when imported into other projects.

For professional Python development, this pattern is considered essential and appears in virtually every serious codebase.