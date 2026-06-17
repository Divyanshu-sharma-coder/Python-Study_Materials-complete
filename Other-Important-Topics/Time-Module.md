# The `time` Module in Python

## 1. What is the `time` Module?

The `time` module is a built-in Python library used for working with **time-related operations**.

It helps you to:
- Measure execution time
- Pause programs
- Work with timestamps
- Format dates and time

---

## 2. The Epoch Concept

In computing, time starts from a fixed reference point called:

```
Epoch = January 1, 1970 (UTC)
```

---

## `time.time()`

Returns the number of seconds since the Epoch.

---

### Example

```python
import time

seconds = time.time()
print(seconds)
```

---

## What it represents

```
Epoch → Now = total seconds passed
```

---

## 3. Performance Measurement (Benchmarking)

One major use of `time` is measuring execution speed.

---

## Example: For vs While Loop

```python
import time

# For loop timing
start_for = time.time()

for i in range(50000):
    pass

end_for = time.time()

print("For loop time:", end_for - start_for)


# While loop timing
start_while = time.time()

i = 0
while i < 50000:
    i += 1

end_while = time.time()

print("While loop time:", end_while - start_while)
```

---

## Output Idea

```
For loop time: 0.01 sec
While loop time: 0.02 sec
```

(Note: varies by system load)

---

## 4. Pausing Execution with `time.sleep()`

This function pauses program execution.

---

## Syntax

```python
time.sleep(seconds)
```

---

## Example

```python
import time

print("Start")

time.sleep(3)

print("End after 3 seconds")
```

---

## What happens?

```
Program pauses → waits → resumes
```

---

## 5. Working with Date & Time

---

## A. `time.localtime()`

Converts timestamp into structured local time.

---

## Example

```python
import time

t = time.localtime()
print(t)
```

---

## B. `time.strftime()`

Formats time into readable strings.

---

## Format Codes

| Code | Meaning |
|:----:|---------|
| `%Y` | Year |
| `%m` | Month |
| `%d` | Day |
| `%H` | Hour |
| `%M` | Minute |
| `%S` | Second |

---

## Example

```python
import time

current_time = time.localtime()

formatted = time.strftime("%Y-%m-%d %H:%M:%S", current_time)

print("Formatted Time:", formatted)
```

---

## Output

```
Formatted Time: 2026-06-17 20:46:21
```

---

## 6. Key Functions Summary

| Function | Purpose |
|:--------:|---------|
| `time.time()` | Seconds since Epoch |
| `time.sleep()` | Pause execution |
| `time.localtime()` | Convert timestamp |
| `time.strftime()` | Format time |

---

## 7. Real-World Uses

✔ Measuring performance  
✔ Adding delays in bots  
✔ Logging timestamps  
✔ Scheduling tasks  
✔ Simulating real-time systems  

---

## Final Idea

The `time` module is a **core utility for controlling, measuring, and formatting time in Python programs**, especially useful in performance tracking and real-world automation systems.