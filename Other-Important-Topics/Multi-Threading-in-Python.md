# Multithreading in Python

## 1. What is Multithreading?

Multithreading is a programming technique that allows a single process to execute **multiple threads concurrently**.

It is mainly used to improve performance in:
- Web scraping
- Network requests
- File I/O operations
- API calls

---

## Core Idea (I/O-Bound Tasks)

When you run tasks sequentially:
- Each task waits for the previous one to finish
- CPU stays idle during waiting (network/server delay)

Multithreading fixes this by:
- Running multiple tasks at the same time
- Utilizing waiting time efficiently

---

## Example Analogy

If 10 files are downloading:
- ❌ Sequential → one after another (slow)
- ✔ Multithreaded → all at once (faster)

---

## 2. Sequential Execution (Problem)

```python
import time

def demo_task(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return seconds


start_time = time.perf_counter()

demo_task(4)
demo_task(2)
demo_task(1)

end_time = time.perf_counter()

print(f"Total sequential time: {end_time - start_time:.2f} seconds")
```

---

### Output

```
Sleeping for 4 seconds...
Sleeping for 2 seconds...
Sleeping for 1 seconds...
Total sequential time: 7.00 seconds
```

---

## 3. Approach 1: Using `threading.Thread`

This method manually creates threads.

---

### Code

```python
import threading
import time

def demo_task(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)


start_time = time.perf_counter()

t1 = threading.Thread(target=demo_task, args=(4,))
t2 = threading.Thread(target=demo_task, args=(2,))
t3 = threading.Thread(target=demo_task, args=(1,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end_time = time.perf_counter()

print(f"Total multithreaded time: {end_time - start_time:.2f} seconds")
```

---

## ✔ Key Thread Methods

### `.start()`
- Starts execution of thread
- Runs in background

### `.join()`
- Waits for thread to finish
- Blocks main program until completion

---

## Output

```
Sleeping for 4 seconds...
Sleeping for 2 seconds...
Sleeping for 1 seconds...
Total multithreaded time: 4.00 seconds
```

---

## 4. Approach 2: `ThreadPoolExecutor` (Recommended)

A modern and scalable way to handle threads.

---

## Method A: Using `submit()`

```python
from concurrent.futures import ThreadPoolExecutor
import time

def demo_task(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Done {seconds}s"


with ThreadPoolExecutor() as executor:
    future1 = executor.submit(demo_task, 3)
    future2 = executor.submit(demo_task, 2)
    future3 = executor.submit(demo_task, 4)

    print(future1.result())
    print(future2.result())
    print(future3.result())
```

---

## Method B: Using `.map()`

```python
from concurrent.futures import ThreadPoolExecutor
import time

def demo_task(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    return f"Completed {seconds}s"


sleep_times = [3, 5, 1, 2]

with ThreadPoolExecutor() as executor:
    results = executor.map(demo_task, sleep_times)

    for r in results:
        print(r)
```

---

## 5. Threading vs Multiprocessing

| Feature | Multithreading | Multiprocessing |
|:--------|:--------------|:----------------|
| Execution | Concurrent | Parallel |
| Memory | Shared | Separate |
| Best For | I/O tasks | CPU-heavy tasks |
| Speed Gain | Moderate | High |

---

## 6. Important Concepts

### ✔ `start()`
Runs thread in background

### ✔ `join()`
Waits for thread completion

### ✔ ThreadPoolExecutor
- Manages thread pool automatically
- Best for real-world applications

---

## Final Idea

Multithreading improves performance by **running multiple tasks simultaneously while waiting for I/O operations**, making programs faster and more efficient in real-world networking and file-based systems.