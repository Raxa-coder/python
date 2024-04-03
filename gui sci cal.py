import math
import tkinter as tk
from tkinter import messagebox

# Function to evaluate mathematical expressions
def evaluate_expression(expression):
    try:
        result = str(eval(expression))
        return result
    except Exception as e:
        return "Error"

# Function to handle button clicks
def button_click(event):
    # Get the text from the clicked button
    text = event.widget.cget("text")

    # Handling the clear button
    if text == "C":
        expression.set("")
    # Handling the equals button
    elif text == "=":
        result = evaluate_expression(expression.get())
        expression.set(result)
    else:
        # Append the clicked button's text to the expression
        expression.set(expression.get() + text)

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Create a StringVar to store the expression
expression = tk.StringVar()

# Create the entry widget for input and display
entry = tk.Entry(root, textvariable=expression, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, ipadx=10, ipady=10)

# Define the buttons and their positions
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("+", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("*", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("/", 4, 3),
    ("(", 1, 4), (")", 2, 4), ("^", 3, 4), ("sqrt", 4, 4),
]

# Create and place the buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 15), padx=20, pady=10)
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", button_click)

# Run the main loop
root.mainloop()
