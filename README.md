# Python Interenship Projects (Codsoft)  by Utkarsh Sharma

## Table of Contents
- [Simple Calculator](#simple-calculator)
- [Contact Manager](#contact-manager)
- [Rock-Paper-Scissors Game](#rock-paper-scissors-game)
- [Password Generator](#password-generator)
- [To-Do List](#to-do-list)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Simple Calculator

This is a simple calculator application built with Tkinter that can perform basic arithmetic operations like addition, subtraction, multiplication, and division.

![Simple Calculator Screenshot](https://res.cloudinary.com/ddcxdapoi/image/upload/v1719571832/Screenshot_2024-06-28_161944_koe5jb.png)

### Features
- Addition, subtraction, multiplication, and division
- Clear button to reset input fields and result

### Code Snippet
```python
def calculate(operation):
    try:
        num1 = int(Input_num_1.get())
        num2 = int(Input_num_2.get())
        
        if operation == "Addition":
            result.set(num1 + num2)
        elif operation == "Subtraction":
            result.set(num1 - num2)
        elif operation == "Multiplication":
            result.set(num1 * num2)
        elif operation == "Division":
            if (num2 != 0):
                result.set(num1 / num2)
            else:
                result.set("Error: Division by zero")
        else:
            result.set("Invalid operation")
    except ValueError:
        result.set("Error: Invalid input")
