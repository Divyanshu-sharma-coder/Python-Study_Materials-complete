# AsyncIO in Python

## 1. What is AsyncIO?

`asyncio` (Asynchronous Input/Output) is a Python library used to write **concurrent code** using:

- `async`
- `await`

Unlike multithreading or multiprocessing, `asyncio` runs on:

```
Single Thread + Single CPU Core
```

It achieves concurrency using an:

```
Event Loop
```

---

## How It Works

When a task is waiting (e.g., network response, file download, API call):

✔ `asyncio` pauses that task  
✔ Switches to another task  
✔ Uses idle waiting time efficiently  

---

## Best Use Case

✔ I/O-bound tasks:
- Web requests
- Database queries
- File downloads
- API calls

---

## 2. The Problem with Sequential Execution

```python
import time

def function1():
    time.sleep(3)
    print("Function 1 Done")

def function2():
    time.sleep(3)
    print("Function 2 Done")

def function3():
    time.sleep(3)
    print("Function 3 Done")


function1()
function2()
function3()
```

---

### Output Behavior

```
Function 1 Done
Function 2 Done
Function 3 Done
```

---

### Total Time

```
3 + 3 + 3 = 9 seconds
```

Because everything runs one after another.

---

## 3. Introducing `async` and `await`

To make functions asynchronous, we use:

- `async` → defines a coroutine  
- `await` → pauses execution without blocking the program  

---

### Example (Sequential Async Calls)

```python
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("Function 1 Done")
    return "Result 1"

async def function2():
    await asyncio.sleep(1)
    print("Function 2 Done")

async def function3():
    await asyncio.sleep(4)
    print("Function 3 Done")


async def main():
    await function1()
    await function2()
    await function3()


asyncio.run(main())
```

---

### Important Note

Even though functions are async:

```
await function1()
await function2()
await function3()
```

This still runs **sequentially**, not concurrently.

---

## 4. True Concurrency using `asyncio.gather()`

To run tasks in parallel-like behavior:

```python
import asyncio
import time

async def function1():
    print("Started Function 1")
    await asyncio.sleep(4)
    print("Finished Function 1")
    return "Harry"

async def function2():
    print("Started Function 2")
    await asyncio.sleep(1)
    print("Finished Function 2")
    return "None1"

async def function3():
    print("Started Function 3")
    await asyncio.sleep(1)
    print("Finished Function 3")
    return "None2"


async def main():
    start_time = time.perf_counter()

    results = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )

    print("Results:", results)

    end_time = time.perf_counter()
    print(f"Total time: {end_time - start_time:.2f} seconds")


asyncio.run(main())
```

---

## Execution Behavior

✔ All tasks start together  
✔ Event loop switches between them  
✔ Fast tasks finish early  
✔ Slowest task decides total time  

---

## Output Behavior

```
Started Function 1
Started Function 2
Started Function 3

Finished Function 2
Finished Function 3
Finished Function 1

Total time: ~4 seconds
```

---

## 5. Alternative: `asyncio.create_task()`

This schedules tasks in the background.

```python
async def main():
    task1 = asyncio.create_task(function1())
    task2 = asyncio.create_task(function2())
    task3 = asyncio.create_task(function3())

    await task1
    await task2
    await task3
```

---

## 6. Key Differences

| Feature | AsyncIO | Multithreading | Multiprocessing |
|:--------|:--------|:---------------|:----------------|
| Model | Event Loop | Threads | Processes |
| CPU Usage | Single core | Single core | Multi-core |
| Best For | I/O tasks | I/O tasks | CPU tasks |
| Speed | Very efficient for I/O | Moderate | High (CPU tasks) |

---

## 7. Key Concepts

✔ `async` → defines coroutine  
✔ `await` → pauses without blocking  
✔ Event Loop → manages task switching  
✔ `gather()` → runs tasks concurrently  
✔ `create_task()` → schedules background execution  

---

## Final Idea

`asyncio` is the most efficient way in Python to handle **large-scale I/O-bound concurrency using a single thread**, by intelligently switching tasks instead of waiting idle.