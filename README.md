# **Assessment-100 Beginner**

This repository contains a series of beginner-friendly Python tasks designed to help students practice fundamental programming concepts. Each task is structured as a standalone module with its corresponding test file, ensuring modularity and ease of testing.

## **Project Structure**

The repository is organized as follows:

```plaintext
tasks/
├── task1_greeting.py       # Task 1: Greeting Function
├── task2_sum.py            # Task 2: Sum of a Range
├── task3_vowels.py         # Task 3: Count Vowels
├── task4_max.py            # Task 4: Find Maximum
├── task5_fizzbuzz.py       # Task 5: FizzBuzz
tests/
├── test_task1_greeting.py  # Tests for Task 1
├── test_task2_sum.py       # Tests for Task 2
├── test_task3_vowels.py    # Tests for Task 3
├── test_task4_max.py       # Tests for Task 4
├── test_task5_fizzbuzz.py  # Tests for Task 5

## **Getting Started**

### **Prerequisites**
To run this project and the tests, ensure you have the following installed:

- Python (version 3.8 or above)
- `pytest` (a testing framework for Python)

You can install `pytest` using pip:

```bash
pip install pytest

## **How to Use**

### **Solve the Tasks**
Each task file in the `tasks/` directory contains a function skeleton with a detailed docstring. Implement the logic for each function following the provided instructions.

### **Test the Solutions**
For each task, there is a corresponding test file in the `tests/` directory. These test files validate the correctness of your solution.

## **How to Run Tests**

### **Run All Tests**
To test all tasks at once, navigate to the project root directory and run:
```bash
pytest tests/

## **Run Tests for a Specific Task**

### **To run tests for a specific task, use the following commands:**
```bash
pytest tests/test_task1_greeting.py

```bash
pytest tests/test_task2_sum.py

```bash
pytest tests/test_task3_vowels.py

```bash
pytest tests/test_task4_max.py

```bash
pytest tests/test_task5_fizzbuzz.py
