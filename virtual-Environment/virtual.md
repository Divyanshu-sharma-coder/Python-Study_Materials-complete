# Virtual Environments in Python

A **Virtual Environment** is an isolated Python workspace that contains its own interpreter, packages, and dependencies.

Its primary purpose is to prevent dependency conflicts between different Python projects running on the same machine.

Without virtual environments, packages are installed globally and can easily break existing projects when versions change.

---

## 1. Why Do We Need Virtual Environments?

Imagine you have two projects:

### Project A

Requires:

```text
pandas==1.4.4
```

### Project B

Requires:

```text
pandas==2.2.0
```

If you install packages globally:

```bash
pip install pandas==1.4.4
```

and later:

```bash
pip install pandas==2.2.0
```

Project A may stop working because its required version was replaced.

This problem is known as:

```text
Dependency Conflict
```

Virtual environments solve this by isolating each project's dependencies.

---

## Global Python vs Virtual Environment

```text
System Python
│
├── Project A
│      └── pandas 1.4.4
│
├── Project B
│      └── pandas 2.2.0
│
└── Project C
       └── numpy 1.26.0
```

Each project maintains its own package ecosystem.

---

## 2. What Actually Gets Created?

When you create a virtual environment:

```bash
python -m venv myenv
```

Python generates a folder structure similar to:

```text
myenv/
│
├── Scripts/          (Windows)
├── bin/              (Linux/macOS)
├── Lib/
├── include/
└── pyvenv.cfg
```

Inside this folder exists:

- A separate Python interpreter
- A separate pip installation
- Separate libraries
- Separate package versions

---

## 3. Creating a Virtual Environment

### Windows

```bash
python -m venv myenv
```

### Linux / macOS

```bash
python3 -m venv myenv
```

---

### Example

```bash
python -m venv myenv
```

Output:

```text
myenv/
```

A new environment folder is created.

---

## 4. Activating the Environment

Creating an environment is not enough.

You must activate it.

---

### Windows Command Prompt

```cmd
myenv\Scripts\activate.bat
```

---

### Windows PowerShell

```powershell
myenv\Scripts\Activate.ps1
```

---

### Linux / macOS

```bash
source myenv/bin/activate
```

---

## How to Know It Is Active?

Your terminal changes:

Before:

```text
C:\Projects>
```

After:

```text
(myenv) C:\Projects>
```

The environment name appears in parentheses.

---

## 5. Checking Which Python Is Being Used

### Windows

```bash
where python
```

### Linux / macOS

```bash
which python
```

Output may look like:

```text
myenv/Scripts/python
```

This confirms the virtual environment interpreter is active.

---

## 6. Installing Packages

After activation:

```bash
pip install pandas
```

The package is installed only inside:

```text
myenv/
```

and not globally.

---

### Installing Specific Versions

```bash
pip install pandas==1.4.4
```

```bash
pip install numpy==1.22.4
```

```bash
pip install scikit-learn==1.4.0
```

---

## 7. Viewing Installed Packages

```bash
pip list
```

Example:

```text
Package        Version
-------------- -------
numpy          1.22.4
pandas         1.4.4
pip            24.0
```

---

## 8. Checking Exact Dependency Versions

```bash
pip freeze
```

Output:

```text
numpy==1.22.4
pandas==1.4.4
openpyxl==3.1.0
```

Unlike `pip list`, this format is designed for dependency replication.

---

## 9. Exporting Dependencies

### Create requirements.txt

```bash
pip freeze > requirements.txt
```

Generated file:

```text
numpy==1.22.4
pandas==1.4.4
openpyxl==3.1.0
```

---

## Why requirements.txt Matters

Suppose you upload a project to:

- GitHub
- Kaggle
- AWS
- Azure
- Google Cloud

Instead of sending your entire virtual environment folder, you only share:

```text
requirements.txt
```

This is much smaller and easier to maintain.

---

## 10. Installing Dependencies from requirements.txt

Another developer can recreate your environment.

### Step 1

Create environment:

```bash
python -m venv myenv
```

### Step 2

Activate it:

```bash
myenv\Scripts\activate
```

### Step 3

Install dependencies:

```bash
pip install -r requirements.txt
```

Python automatically installs every package listed.

---

## 11. Deactivating the Environment

When finished:

```bash
deactivate
```

Terminal:

Before:

```text
(myenv) C:\Projects>
```

After:

```text
C:\Projects>
```

You are back to the global Python interpreter.

---

## 12. Best Practices

### Use One Environment Per Project

Good:

```text
Student-ML-Project/
│
├── .venv
├── app.py
└── requirements.txt
```

Bad:

```text
One environment for 20 projects
```

---

### Never Upload Virtual Environments to GitHub

Wrong:

```text
project/
│
├── myenv/
└── app.py
```

The environment folder can be hundreds of MB.

---

### Use .gitignore

```gitignore
venv/
myenv/
.venv/
```

This prevents Git from uploading the environment.

---

### Upload requirements.txt Instead

```text
project/
│
├── app.py
├── requirements.txt
└── .gitignore
```

---

## 13. Virtual Environments in Data Science & ML

Almost every professional ML project uses:

```text
venv
conda
poetry
pipenv
```

because ML libraries frequently require specific versions.

Example:

```text
TensorFlow 2.15
PyTorch 2.4
Scikit-Learn 1.4
```

Different projects often need different combinations.

---

## Common Commands Cheat Sheet

### Create Environment

```bash
python -m venv myenv
```

---

### Activate Environment

Windows:

```cmd
myenv\Scripts\activate
```

Linux/macOS:

```bash
source myenv/bin/activate
```

---

### Install Package

```bash
pip install pandas
```

---

### View Installed Packages

```bash
pip list
```

---

### Freeze Dependencies

```bash
pip freeze
```

---

### Create requirements.txt

```bash
pip freeze > requirements.txt
```

---

### Install From requirements.txt

```bash
pip install -r requirements.txt
```

---

### Exit Environment

```bash
deactivate
```

---

## Summary

| Command | Purpose |
|----------|----------|
| `python -m venv myenv` | Create environment |
| `activate` | Enter environment |
| `pip install package` | Install package |
| `pip list` | View installed packages |
| `pip freeze` | Show exact versions |
| `pip freeze > requirements.txt` | Export dependencies |
| `pip install -r requirements.txt` | Recreate dependencies |
| `deactivate` | Exit environment |

---

## Key Takeaway

Virtual environments isolate Python projects from one another by providing separate interpreters and package installations. They eliminate dependency conflicts, improve project reproducibility, and are considered a standard practice in professional Python development, data science, machine learning, backend engineering, and DevOps workflows.