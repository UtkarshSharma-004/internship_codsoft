import tkinter as tk

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
            if num2 != 0:
                result.set(num1 / num2)
            else:
                result.set("Error: Division by zero")
        else:
            result.set("Invalid operation")
    except ValueError:
        result.set("Error: Invalid input")

def clear_fields():
    Input_num_1.delete(0, tk.END)
    Input_num_2.delete(0, tk.END)
    result.set("")

# Initialize main window
root = tk.Tk()
root.title("Simple Calculator By Utkarsh Sharma")
root.geometry("400x500")
root.configure(bg="#F0F8FF")  # Light blue background color

tk.Label(root, text="Enter First Number:", font=('Helvetica', 14), pady=10, bg="#F0F8FF").pack()
Input_num_1 = tk.Entry(root, font=('Helvetica', 14), bd=3, relief='sunken')
Input_num_1.pack(pady=5)

tk.Label(root, text="Enter Second Number:", font=('Helvetica', 14), pady=10, bg="#F0F8FF").pack()
Input_num_2 = tk.Entry(root, font=('Helvetica', 14), bd=3, relief='sunken')
Input_num_2.pack(pady=5)

tk.Label(root, text="Choose Operator:", font=('Helvetica', 14), pady=10, bg="#F0F8FF").pack()

button_frame = tk.Frame(root, bg="#F0F8FF")
button_frame.pack(pady=10)

button_style = {
    'font': ('Helvetica', 14),
    'padx': 10,
    'pady': 5,
    'relief': 'raised',
    'bd': 4,
    'width': 10,
    'height': 2
}

tk.Button(button_frame, text="+", command=lambda: calculate("Addition"), bg="#ADD8E6", **button_style).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="-", command=lambda: calculate("Subtraction"), bg="#90EE90", **button_style).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="*", command=lambda: calculate("Multiplication"), bg="#D4ABC1", **button_style).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="/", command=lambda: calculate("Division"), bg="#FFB6C1", **button_style).grid(row=0, column=3, padx=5)

# Clear button
tk.Button(root, text="Clear", command=clear_fields, bg="#FFD700", **button_style).pack()

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=('Helvetica', 14), pady=10, bg="#F0F8FF")
result_label.pack()

# Start the Tkinter event loop
root.mainloop()
