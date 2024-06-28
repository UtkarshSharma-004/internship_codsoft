import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length)
        entry_password.config(state=tk.NORMAL)
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
        entry_password.config(state=tk.DISABLED)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x500")

root.configure(bg="#F0F8FF")  # Light blue background color


# Create and place the widgets with improved UI/UX
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

label_length = tk.Label(frame, text="Enter the desired length of the password:", font=("Arial", 12))
label_length.grid(row=0, column=0, pady=10)

entry_length = tk.Entry(frame, font=("Arial", 12))
entry_length.grid(row=0, column=1, pady=10, padx=10)

button_generate = tk.Button(frame, text="Generate Password", command=on_generate, font=("Arial", 12), bg="#4CAF50", fg="white")
button_generate.grid(row=1, column=0, columnspan=2, pady=10)

label_password = tk.Label(frame, text="Generated Password:", font=("Arial", 12))
label_password.grid(row=2, column=0, pady=10)

entry_password = tk.Entry(frame, font=("Arial", 12), width=30, state=tk.DISABLED)
entry_password.grid(row=2, column=1, pady=10, padx=10)

button_copy = tk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, font=("Arial", 12), bg="#008CBA", fg="white")
button_copy.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()


