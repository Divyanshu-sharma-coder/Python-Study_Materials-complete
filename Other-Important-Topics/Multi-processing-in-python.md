# Multiprocessing in Python

## 1. What is Multiprocessing?

Multiprocessing is a built-in Python module that allows you to run **multiple processes simultaneously**.

Each process:
- Runs independently
- Has its own memory space
- Can use separate CPU cores

---

## Multiprocessing vs Multithreading

### ✔ Multithreading
- Runs multiple threads inside a single process  
- Shares same memory space  
- Best for **I/O-bound tasks** (web scraping, file reading, APIs)

### ✔ Multiprocessing
- Runs multiple processes independently  
- Does NOT share memory  
- Best for **CPU-bound tasks** (image processing, ML, heavy computation)  
- Avoids Python **GIL (Global Interpreter Lock)**

---

## 2. Approach 1: `multiprocessing.Process`

This method manually creates and manages processes.

### Example: Parallel File Downloading

```python
import multiprocessing
import requests

def download_file(url, name):
    print(f"Started downloading file_{name}...")
    response = requests.get(url)
    
    with open(f"files/file_{name}.jpg", "wb") as f:
        f.write(response.content)
        
    print(f"Finished downloading file_{name}!")


if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    
    processes = []

    # Creating multiple processes
    for i in range(5):
        p = multiprocessing.Process(
            target=download_file,
            args=(url, i)
        )
        p.start()
        processes.append(p)

    # Waiting for all processes to complete
    for p in processes:
        p.join()

    print("All parallel downloads completed!")
```

---

## 3. Approach 2: `ProcessPoolExecutor` (Recommended)

A higher-level and cleaner abstraction for multiprocessing.

### Key Idea:
- Automatically manages process pool
- Uses `.map()` for parallel execution

---

### Example

```python
from concurrent.futures import ProcessPoolExecutor
import requests

def download_file(url, name):
    print(f"Started downloading file_{name}...")
    response = requests.get(url)
    
    with open(f"files/file_{name}.jpg", "wb") as f:
        f.write(response.content)
        
    print(f"Finished downloading file_{name}!")


if __name__ == "__main__":
    url_base = "https://picsum.photos/2000/3000"

    urls = [url_base for _ in range(50)]
    names = [i for i in range(50)]

    with ProcessPoolExecutor() as executor:
        executor.map(download_file, urls, names)

    print("Process Pool execution completed!")
```

---

## 4. Key Notes & Best Practices

### ✔ `__main__` Guard

Always use:

```python
if __name__ == "__main__":
```

### Why?

Because:
- Each process starts a fresh Python interpreter
- Without this guard → infinite process spawning risk

---

### ✔ Resource Management

Avoid:
- Creating too many processes at once
- Overloading CPU/RAM

---

## 5. When to Use Multiprocessing

✔ Use it for:
- Heavy computations
- Image processing
- ML training tasks
- Data analysis pipelines

❌ Avoid it for:
- Simple tasks
- I/O-heavy lightweight operations (use threading instead)

---

## Final Idea

Multiprocessing = **True parallel execution using multiple CPU cores**, making Python capable of handling heavy workloads efficiently.