# def subtract(n1, n2):
#     return n1 - n2

# def multiply(n1, n2):
#     return n1 * n2

# def divide(n1, n2):
#     return n1 / n2

# operation = {

#      "+": add,
#      "-": subtract,
#      "*": multiply,
#      "/": divide,    
# }

# def calculator():
#     should_accumulate = True
#     num1 = float(input("What is the first number: "))

#     while should_accumulate:

#         for symbol in operation:
#             print(symbol)

#         operation_symbol = input("Pick a operation: ")
#         num2 = float(input("What is the next number: "))
#         answer = operation[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")

#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n'to start new calculation: ")

#         if choice == "y":
#            num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20) 
#         calculator()

# calculator()          

import tkinter as tk
from tkinter import messagebox

# --- Calculator Functions ---
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        messagebox.showerror("Error", "Division by Zero is not allowed!")
        return None
    return n1 / n2

# Dictionary for operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# --- GUI Calculator Class ---
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        self.expression = ""  # Stores user input expression

        # --- Display ---
        self.entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, padx=10, sticky="nsew")

        # --- Buttons ---
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(root, text=text, font=("Arial", 16), width=6, height=2,
                            command=lambda t=text: self.on_button_click(t))
            btn.grid(row=row, column=col, padx=5, pady=5)

        # Clear button
        clear_btn = tk.Button(root, text="C", font=("Arial", 16), width=28, height=2,
                              bg="tomato", command=self.clear)
        clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

    # Handle button press
    def on_button_click(self, char):
        if char == "=":
            try:
                result = self.calculate(self.expression)
                if result is not None:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(tk.END, str(result))
                    self.expression = str(result)
            except Exception:
                messagebox.showerror("Error", "Invalid Expression")
                self.clear()
        else:
            self.expression += str(char)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

    # Evaluate expression
    def calculate(self, expr):
        for op in operations:
            if op in expr:
                left, right = expr.split(op, 1)
                try:
                    left, right = float(left), float(right)
                    return operations[op](left, right)
                except ValueError:
                    return None
        return None

    # Clear screen
    def clear(self):
        self.expression = ""
        self.entry.delete(0, tk.END)

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
