<div align="center">
  <h1>📚 Python — Study Materials</h1>
  <p>A comprehensive repository of clean, well-documented concepts, source code, and logic breakdowns from my Python learning journey.</p>

  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version" />
  <img src="https://img.shields.io/badge/Status-In_Progress-orange?style=for-the-badge" alt="Repository Status" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" />
  <img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen?style=for-the-badge" alt="Maintained" />
</div>

---

## 📖 Overview

Welcome to my Python self-study vault! This repository serves as a structured documentation of my daily coding sessions, focusing on conceptual clarity, source code annotations, and mental models for algorithmic edge cases. 

Whether you are revising core concepts or looking through reference materials, these modules break down native features step-by-step.

---

## 📑 Table of Contents

| Day | Module Topic | Core Concepts Covered |
| :---: | :--- | :--- |
| **Day 14** | [Strings in Python](#-day-11-strings-in-python) | Sequence declarations, Multiline syntax, Character index tracking |
| **Day 12** | [String Slicing & Operations](#-day-12-string-slicing--operations) | Substring syntax `[start:end]`, Slicing defaults, Negative indexing formulas |
| **Day 13** | [String Native Methods](#-day-13-string-methods) | Immutability rules, Case mutation, Stripping, Search indices (`find` vs `index`) |
| **Day 21** | [Function Arguments](#-day-21-function-arguments) | Default/Required logic, Keyword signatures, Variable-length vectors (`*args`, `**kwargs`) |

---

## 🔍 Module Summaries

### 🔹 Day 11: Strings in Python
* **Concept:** Text blocks represented as ordered Unicode character vectors.
* **Key Takeaway:** Demonstrates handling embedded quotes using different wrappers (`'...'` vs `"..."`) and setting up continuous multi-line blocks using triple quotes (`"""..."""`). It introduces sequential character index tracking starting at zero.

### 🔹 Day 12: String Slicing & Operations
* **Concept:** Extracting segments from string targets cleanly using bounds constraints.
* **Key Takeaway:** Uses the inclusive-start, exclusive-end system: `[start:end]`. Features a complete breakdown of negative index wrapping, showing how Python adds `len(string)` internally to translate negative inputs into positive coordinates.

### 🔹 Day 13: String Methods
* **Concept:** Operating on variables via Python's native string utility suite.
* **Key Takeaway:** Emphasizes string **immutability**—demonstrating that string methods yield entirely new instances rather than rewriting existing blocks. Covers formatting layouts (`.capitalize()`, `.title()`), sanitization (`.rstrip()`), and lookup bounds comparisons (`.find()` vs `.index()`).

### 🔹 Day 21: Function Arguments
* **Concept:** Designing flexible configurations for receiving data inputs in definitions.
* **Key Takeaway:** Breaks down structural variations including:
  * **Default / Required Arguments:** Handling parameter fallbacks.
  * **Keyword Arguments:** Freeing function calls from strict rotational order.
  * **Variable-Length Containers:** Bundling runtime variables dynamically into **Tuples** (`*args`) or named parameter lists into **Dictionaries** (`**kwargs`).

---

## ⚙️ Repository Setup & Local Development

Want to test these scripts locally on your machine?

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Divyanshu-sharma-coder/Python-Study_Materials-complete.git
   cd Python-Study_Materials-complete