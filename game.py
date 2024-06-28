import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner of a single round
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Draw"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "Player"
    else:
        return "Computer"

# Function to handle a player's choice
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

# Function to reset the game
def reset_game():
    global rounds, player_score, computer_score, round_results
    rounds = 0
    player_score = 0
    computer_score = 0
    round_results = []
    results_display.delete(1.0, tk.END)

# Function to update the results display
def update_results():
    results_display.delete(1.0, tk.END)
    for result in round_results:
        results_display.insert(tk.END, result + '\n')

# Initialize main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x500")
root.configure(bg="#F0F8FF")  # Light blue background color

# Initialize game variables
rounds = 0
player_score = 0
computer_score = 0
round_results = []

# Mapping choices to emojis
player_choice_emoji = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

# Widgets
tk.Label(root, text="Enter your name:", font=('Helvetica', 14), pady=10, bg="#F0F8FF").pack()
player_name = tk.StringVar()
tk.Entry(root, textvariable=player_name, font=('Helvetica', 14), bd=3, relief='sunken').pack(pady=5)

tk.Label(root, text="Choose your move:", font=('Helvetica', 14), pady=10, bg="#F0F8FF").pack()

button_frame = tk.Frame(root, bg="#F0F8FF")
button_frame.pack(pady=10)

button_style = {
    'font': ('Helvetica', 14),
    'padx': 10,
    'pady': 5,
    'relief': 'raised',
    'bd': 3,
    'width': 10,
    'height': 2
}

tk.Button(button_frame, text="🪨 Rock", command=lambda: play_round("Rock"), bg="#ADD8E6", **button_style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="📄 Paper", command=lambda: play_round("Paper"), bg="#90EE90", **button_style).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="✂️ Scissors", command=lambda: play_round("Scissors"), bg="#FFB6C1", **button_style).grid(row=0, column=2, padx=5)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, font=('Helvetica', 14), pady=10, bg="#F0F8FF").pack()

# Text widget to display round results
results_display = tk.Text(root, height=10, width=45, font=('Helvetica', 12), bd=3, relief='sunken', wrap='word')
results_display.pack(pady=10)

# Insert initial text into the Text widget
results_display.insert(tk.END, "Rock ~ Paper ~ Scissor by Utkarsh Sharma\n\n")

# Start the Tkinter event loop
root.mainloop()
