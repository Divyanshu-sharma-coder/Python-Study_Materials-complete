# Creating Command Line Utilities in Python

## 1. What is a Command Line Utility?

A **Command Line Interface (CLI) utility** is a program that runs inside the terminal.

Instead of using:
- GUI buttons
- input() prompts

It uses:
- Arguments
- Flags
- Commands

---

## Examples of CLI tools

```
git
curl
wget
python
```

---

## Why CLI tools are powerful?

✔ Fast execution  
✔ Automatable  
✔ Script-friendly  
✔ Used in real production systems  

---

## 2. Argument Parsing with `argparse`

Python provides a built-in module:

```
argparse
```

It helps to:
- Read terminal inputs
- Handle flags like `-o`
- Auto-generate help menus
- Validate inputs

---

## Steps to Use `argparse`

### 1. Create parser
### 2. Add arguments
### 3. Parse inputs

---

## 3. Project: File Downloader CLI Tool

This tool:
- Takes a URL
- Downloads file
- Saves it locally
- Optionally renames output file

---

## Source Code

```python
import argparse
import requests


def download_file(url, output_filename):
    print(f"Connecting to: {url}")

    response = requests.get(url)

    with open(output_filename, "wb") as file:
        file.write(response.content)

    print(f"Saved as: {output_filename}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="CLI tool to download files from a URL"
    )

    # Required argument
    parser.add_argument(
        "url",
        help="File URL to download"
    )

    # Optional argument
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Output filename (optional)"
    )

    args = parser.parse_args()

    # Decide filename
    if args.output is None:
        filename = args.url.split("/")[-1]

        if not filename:
            filename = "downloaded_file.tmp"
    else:
        filename = args.output

    download_file(args.url, filename)
```

---

## 4. How It Works

```
Terminal → argparse → Python variables → download logic → file saved
```

---

## 5. Usage in Terminal

---

### ✔ Help Command

```bash
python main.py --help
```

### Output

```
usage: main.py [-h] [-o OUTPUT] url

CLI tool to download files from a URL

positional arguments:
  url                   File URL to download

optional arguments:
  -h, --help            show help message
  -o OUTPUT, --output   Output filename (optional)
```

---

## 6. Running the Tool

---

### ✔ Basic Usage

```bash
python main.py https://example.com/file.pdf
```

✔ Saves as:
```
file.pdf
```

---

### ✔ Custom Filename

```bash
python main.py https://example.com/file.pdf -o myfile.pdf
```

✔ Saves as:
```
myfile.pdf
```

---

## 7. Logic Breakdown

### Filename resolution

```
if output not given:
    extract filename from URL
else:
    use custom name
```

---

## 8. Key Features of `argparse`

✔ Handles CLI arguments  
✔ Supports optional + required inputs  
✔ Auto-generates help text  
✔ Prevents invalid usage  

---

## 9. Real-World Uses

CLI tools are used in:

- DevOps automation
- Deployment scripts
- Data pipelines
- System utilities
- API tools

---

## Final Idea

A command line utility turns Python into a **system-level automation tool**, allowing programs to be executed directly from the terminal using structured commands and arguments.