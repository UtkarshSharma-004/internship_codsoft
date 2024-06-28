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

        ```
---

### Contact Manager
The Contact Manager is a Tkinter application for managing a list of contacts. You can add, update, delete, and search for contacts.

![Contact Manager Screenshot](https://res.cloudinary.com/ddcxdapoi/image/upload/v1719572625/Screenshot_2024-06-28_163328_bckktj.png)

### Features
- Add new contacts
- Update existing contacts
- Delete contacts
- Search for contacts


### Code Snippet

```python
def add_contact(self):
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required!")
        return

    if not re.match(r'^\d{10}$', phone):
        messagebox.showwarning("Input Error", "Phone number must be 10 digits!")
        return

    if email and not re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email):
        messagebox.showwarning("Input Error", "Email must be a valid Gmail address!")
        return

    self.contacts[phone] = {'Name': name, 'Phone': phone, 'Email': email, 'Address': address}
    self.update_contact_list()
    self.save_contacts()

```

---

### Rock-Paper-Scissors Game

This is a simple Rock-Paper-Scissors game built with Tkinter. Play against the computer and see who wins!

![Rock-Paper-Scissors Game Screenshot](https://res.cloudinary.com/ddcxdapoi/image/upload/v1719572837/Screenshot_2024-06-28_163654_rumylt.png)

![Rock-Paper-Scissors Game Screenshot](https://res.cloudinary.com/ddcxdapoi/image/upload/v1719572838/Screenshot_2024-06-28_163707_dycn0u.png)

### Features
- Play Rock-Paper-Scissors against the computer
- Track scores for multiple rounds
- Display results of each round and overall winner

### Code Snippet

```python
def play_round(player_choice):
    global rounds, player_score, computer_score, round_results

    if rounds >= 5:
        return

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    winner = determine_winner(player_choice, computer_choice)

    if winner == "Player":
        player_score += 1
    elif winner == "Computer":
        computer_score += 1

    rounds += 1

    result = f"Round {rounds}: {player_name.get()} chose {player_choice_emoji[player_choice]}, Computer chose {player_choice_emoji[computer_choice]}. {winner} wins the round!"
    round_results.append(result)
    update_results()

    if rounds == 5:
        if player_score > computer_score:
            final_winner = f"{player_name.get()} wins the game!"
        elif computer_score > player_score:
            final_winner = "Computer wins the game!"
        else:
            final_winner = "The game is a draw!"
        
        messagebox.showinfo("Game Over", final_winner)
        reset_game()
```

---

### Password Generator

A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.

![Password Generator Screenshot](https://res.cloudinary.com/ddcxdapoi/image/upload/v1719572925/Screenshot_2024-06-28_163828_exw5g9.png)

### Features
- User specifies the desired length of the password
- Generates a random password using a combination of characters
- Displays the generated password

### Code Snippet

```python

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the desired length of the password: "))
print("Generated Password: ", generate_password(length))

```

### To-Do List
A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create a command-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists.


![To-Do List Screenshot](https://res.cloudinary.com/ddcxdapoi/image/upload/v1719573036/Screenshot_2024-06-28_164019_ln4irb.png)

### Features
- Create new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as complete
- View all tasks

### Code Snippet

``` python 
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added task: {task}")

def update_task(index, new_task):
    tasks[index] = new_task
    print(f"Updated task at index {index} to: {new_task}")

def delete_task(index):
    task = tasks.pop(index)
    print(f"Deleted task: {task}")

def list_tasks():
    for index, task in enumerate(tasks):
        print(f"{index}: {task}")

add_task("Buy groceries")
add_task("Read a book")
list_tasks()
update_task(1, "Read two books")
delete_task(0)
list_tasks()
```
--- 

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/UtkarshSharma-004/internship_codsoft.git
    cd internship_codsoft
    ```

2. Ensure you have Python installed (preferably Python 3.6 or higher).

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run any of the applications, navigate to the directory containing the Python file and run it using Python.

```bash
python calculator.py
python contact_book.py
python game.py
python password_generator.py
python todo_list.py
```

## Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```