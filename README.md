# Multi-Utility Toolkit

## Project: Modular & Packager

### Overview

Multi-Utility Toolkit is a Python-based application that integrates multiple built-in modules, custom modules, and packages to perform a variety of tasks. The project demonstrates Python's modular programming concepts using datetime, time, random, uuid, and importlib modules.

---

## Features

### 1. Datetime and Time Operations

* Display current date and time
* Calculate difference between two dates
* Format dates into custom formats
* Stopwatch
* Countdown Timer

### 2. Mathematical Operations

* Factorial Calculation
* Compound Interest Calculation
* Trigonometric Calculations
* Area of Geometric Shapes

### 3. Random Data Generation

* Generate Random Numbers
* Generate Random Lists
* Generate Random Passwords
* Generate Random OTPs

### 4. UUID Generation

* Generate unique identifiers using UUID4

### 5. File Operations (Custom Module)

* Create File
* Write to File
* Read from File
* Append Data to File

### 6. Module Exploration

* Explore built-in and custom module attributes using dir()

---

## Project Structure

```text
project/
│
├── main.py
│
└── utility/
    ├── __init__.py
    ├── math_utility.py
    └── file_operations.py
```

---

## Modules Used

### Built-in Modules

* datetime
* time
* random
* string
* uuid
* importlib

### Custom Modules

* math_utility.py
* file_operations.py

### Package

* utility

---

## How to Run

1. Open terminal in project folder.
2. Run the following command:

```bash
python main.py
```

3. Select options from the menu.

---

## Example Output

### UUID Generation

```text
Generated UUID:
550e8400-e29b-41d4-a716-446655440000
```

### Random Password

```text
Generated Password:
A7@kP2#m
```

### File Read Operation

```text
File Content:
Hello Python
```

### Module Exploration

```text
Enter Module Name: math

Available Attributes:
['acos', 'asin', 'atan', 'ceil', 'cos', 'factorial', 'pi', 'sin', 'sqrt', 'tan']
```

---

## Learning Outcomes

* Understanding Python Modules and Packages
* Creating Custom Modules
* Using **init**.py for Package Initialization
* Implementing Menu-Driven Applications
* Working with Built-in Python Modules
* Exploring Modules Dynamically using dir()

---

## Author

Student Name: jalpa nakrani

Course: Python Programming

Project Title: Multi-Utility Toolkit
