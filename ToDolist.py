import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        index = task_listbox.curselection()[0]
        task_listbox.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("4000x300")
root.config(bg="#FFA500")

task_entry = tk.Entry(root, width=40, font=("Arial", 12))
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#FFA500")
button_frame.pack(pady=5)

add_button = tk.Button(button_frame, text="Add Task", width=10, bg="#FFD700", font=("Arial", 10), command=add_task)
add_button.grid(row=0, column=0, padx=5)

remove_button = tk.Button(button_frame, text="Remove Task", width=10, bg="#FFD700", font=("Arial", 10), command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

clear_button = tk.Button(button_frame, text="Clear All", width=10, bg="#FFD700", font=("Arial", 10), command=clear_tasks)
clear_button.grid(row=0, column=2, padx=5)

task_listbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

root.mainloop()
