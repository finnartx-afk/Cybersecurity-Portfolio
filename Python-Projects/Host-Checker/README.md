# Day 5 - Cybersecurity Host Checker

## Description

A beginner Python project that practices Python functions and program organization.

## 📖 Challenge

Build a simple **Cybersecurity Host Checker**.

The program asks the user to enter a hostname, validates the input, and then simulates a basic host scan


## 📝 Example Program

```text
===== Cybersecurity Host Checker =====

Enter hostname: google.com

Checking host...

Target: google.com

Scan completed.
```

---

## ✅ Requirements

### 1. Create a function named:

```python
def get_host():
```

Responsibilities:

- Get the hostname from the user.
- Return the hostname using `return`.
- Do not print anything inside this function.

---

### 2. Create a function named:

```python
def scan(host):
```

Responsibilities:

Print:

```text
Checking host...

Target: google.com

Scan completed.
```

Requirements:

- Accept the hostname as a parameter.
- Do not use `input()` inside this function.

---

### 3. Main Program

Your main program should:

- Display the project title.
- Call `get_host()`.
- Store the returned value in a variable.
- Check whether the hostname is empty.
- If the hostname is valid, call:

```python
scan(host)
```

---

## ⭐ Bonus Challenge

If the user presses **Enter** without typing anything:

```text
Enter hostname:
```

Display:

```text
Hostname cannot be empty.
```

instead of running the scan.

---

## 🎯 Skills Practiced

- Python Functions
- Function Parameters
- Return Statements
- Variables
- Scope
- User Input
- Conditional Statements
- Basic Program Organization
