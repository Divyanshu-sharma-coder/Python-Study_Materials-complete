# How Import Works in Python

In Python, **importing** is the mechanism used to load external modules, libraries, or custom Python files into your current program.

When Python imports a module, it executes that module once and makes its functions, classes, and variables available for use in your script.

---

## 1. Basic Import Syntax

### Importing an Entire Module

```python
import math

print(math.sqrt(9))   # Output: 3.0
print(math.pi)        # Output: 3.141592653589793
```

### How It Works

```text
math module
    │
    ├── sqrt()
    ├── sin()
    ├── cos()
    ├── pi
    └── ...
```

After importing:

```python
math.sqrt()
math.sin()
math.pi
```

The module name acts like a namespace.

---

## 2. Importing Specific Components

Instead of importing the entire module, you can import only the components you need.

```python
from math import sqrt, pi

print(sqrt(9))
print(pi)
```

Output:

```text
3.0
3.141592653589793
```

Notice:

```python
sqrt(9)
```

works directly without:

```python
math.sqrt(9)
```

because `sqrt` was imported directly into the current namespace.

---

## 3. Wildcard Imports

You can import everything from a module.

```python
from math import *

print(sqrt(16))
print(pi)
print(sin(0))
```

### Why It Is Dangerous

Suppose:

```python
from math import *

pi = 100
```

Now:

```python
print(pi)
```

Output:

```text
100
```

You accidentally overwrote the mathematical constant.

Because of these naming conflicts:

```python
from module import *
```

is strongly discouraged in professional code.

---

## 4. Using Aliases with `as`

Aliases provide shorter or more readable names.

### Module Alias

```python
import pandas as pd

df = pd.DataFrame()
```

Instead of:

```python
import pandas

df = pandas.DataFrame()
```

---

### Function Alias

```python
from math import sqrt as square_root

print(square_root(25))
```

Output:

```text
5.0
```

---

## Common Industry Aliases

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
```

You'll see these everywhere in Data Science and AI projects.

---

## 5. Creating Custom Modules

Any Python file can become a module.

---

### Step 1: Create a File

File:

```text
harry.py
```

Contents:

```python
def welcome():
    print("Hey, you are welcome my friend!")

status = "Harry is a good boy"
```

---

### Step 2: Import It

File:

```text
main.py
```

```python
import harry

harry.welcome()
print(harry.status)
```

Output:

```text
Hey, you are welcome my friend!
Harry is a good boy
```

---

## 6. Import Specific Components from Custom Modules

Instead of importing the entire module:

```python
from harry import welcome, status

welcome()
print(status)
```

Output:

```text
Hey, you are welcome my friend!
Harry is a good boy
```

---

## 7. Using Aliases with Custom Modules

```python
import harry as hr

hr.welcome()
print(hr.status)
```

This is useful when module names are long.

---

## 8. What Happens Internally During Import?

Consider:

```python
import math
```

Python performs:

### Step 1

Checks whether the module is already loaded.

```python
sys.modules
```

---

### Step 2

If not loaded:

```text
Search Path:
```

1. Current directory
2. Standard library
3. Site-packages directory

---

### Step 3

Loads the module into memory.

---

### Step 4

Executes all top-level code.

Example:

```python
# demo.py

print("Module Loaded")

x = 10
```

Importing:

```python
import demo
```

Output:

```text
Module Loaded
```

because top-level statements execute during import.

---

## 9. The Special `__name__` Variable

Every Python file automatically receives a special variable:

```python
__name__
```

---

### Example

```python
print(__name__)
```

Running file directly:

```python
python test.py
```

Output:

```text
__main__
```

---

Imported from another script:

```python
import test
```

Output:

```text
test
```

(the filename becomes the module name)

---

## 10. The `if __name__ == "__main__"` Pattern

This is one of the most important Python patterns.

```python
def welcome():
    print("Hello")

if __name__ == "__main__":
    welcome()
```

---

Running directly:

```bash
python harry.py
```

Output:

```text
Hello
```

---

Importing:

```python
import harry
```

Output:

```text
(nothing)
```

because:

```python
if __name__ == "__main__":
```

becomes False during imports.

---

### Why Use It?

Allows a file to act as:

- A reusable module
- A standalone program

at the same time.

---

## 11. Exploring Modules Using `dir()`

The `dir()` function shows everything exposed by a module.

```python
import math

print(dir(math))
```

Partial Output:

```text
[
 'acos',
 'asin',
 'atan',
 'ceil',
 'cos',
 'degrees',
 'exp',
 'factorial',
 'floor',
 'pi',
 'pow',
 'sin',
 'sqrt',
 'tan'
]
```

Useful when learning unfamiliar libraries.

---

## 12. Viewing Documentation with `help()`

```python
import math

help(math.sqrt)
```

Output:

```text
Help on built-in function sqrt:

sqrt(x)
    Return the square root of x.
```

Very useful during development.

---

## 13. Common Import Styles

### Recommended

```python
import math

math.sqrt(25)
```

---

### Also Good

```python
from math import sqrt

sqrt(25)
```

---

### Common in AI/ML

```python
import pandas as pd
import numpy as np
```

---

### Avoid

```python
from math import *
```

---

## Import Hierarchy in Real AI Projects

```python
# Standard Library
import os
import sys
import json

# Third-Party Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Local Modules
from preprocessing import clean_data
from model import train_model
```

This ordering is considered professional and follows PEP 8 guidelines.

---

## Summary Cheat Sheet

| Syntax | Example | Use Case |
|----------|----------|----------|
| Import Module | `import math` | Clean and safest approach |
| Import Specific Items | `from math import sqrt` | Import only what you need |
| Alias Module | `import pandas as pd` | Shorter names |
| Alias Function | `from math import sqrt as sr` | Rename imported objects |
| Wildcard Import | `from math import *` | Avoid in production |
| Custom Module | `import harry` | Reuse your own code |
| Inspect Module | `dir(math)` | View available functions |
| Documentation | `help(math.sqrt)` | Learn function details |

---

## Key Takeaway

Python's import system allows code reuse, modular design, and package management. Every professional Python project—from Data Science and Machine Learning to Backend Development and DevOps—relies heavily on imports. Understanding modules, aliases, custom packages, `dir()`, and the `__name__ == "__main__"` pattern is essential for writing scalable and maintainable Python applications.