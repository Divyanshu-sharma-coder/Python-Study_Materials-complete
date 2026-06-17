# The `requests` Module in Python

## 1. What is the `requests` Module?

The `requests` module is a simple and powerful **HTTP library for Python**.

It allows you to:
- Send HTTP requests
- Work with APIs
- Fetch web pages
- Handle server responses easily

---

## Installation

Since it is a third-party library:

```bash
pip install requests
```

---

## 2. Handling GET Requests

A **GET request** is used to fetch data from a server.

---

## Example

```python
import requests

# Sending GET request
response = requests.get("https://www.google.com")

# Printing HTML content
print(response.text)
```

---

## What Happens Here?

✔ Sends request to server  
✔ Receives HTML response  
✔ Stores it in `response` object  
✔ `.text` gives raw HTML  

---

## 3. Handling POST Requests

A **POST request** is used to send data to a server.

Common uses:
- Form submission
- Creating database entries
- Sending JSON data to APIs

---

## Example

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "harry bhai",
    "body": "bhai",
    "userId": 12
}

headers = {
    "Content-type": "application/json; charset=UTF-8"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```

---

## What Happens Here?

✔ Data is sent to server  
✔ Server processes JSON payload  
✔ Response is returned  

---

## 4. Practical Use Case: Web Scraping

One of the most powerful uses of `requests` is **web scraping**.

When combined with `BeautifulSoup`, it becomes a full scraping tool.

---

## Example

```python
import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com/blog"

# Step 1: Get HTML content
response = requests.get(url)

# Step 2: Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract headings
for heading in soup.find_all("h2"):
    print(heading.text)
```

---

## 5. How Web Scraping Works

### Step-by-step flow

```
requests → fetch HTML → BeautifulSoup → parse → extract data
```

---

## 6. Important Limitation

### ⚠️ JavaScript-Rendered Pages

If a website loads content using JavaScript:

- `requests.get()` only fetches raw HTML
- Dynamic content will NOT appear

---

## Example Problem

```
Page loads content after JS execution → requests cannot see it
```

---

## 7. Key Features of `requests`

✔ Simple API  
✔ Supports GET / POST / PUT / DELETE  
✔ Handles headers & JSON easily  
✔ Works with REST APIs  
✔ Very readable syntax  

---

## 8. Key Takeaways

✔ GET → Fetch data  
✔ POST → Send data  
✔ `.text` → Raw HTML response  
✔ Combine with BeautifulSoup → scraping  
✔ Does NOT execute JavaScript  

---

## Final Idea

The `requests` module is the **foundation of web communication in Python**, allowing your code to interact with websites and APIs like a browser (without rendering JavaScript).