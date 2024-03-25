import tkinter as tk
import math

def evaluate_expression(expression):
    # Remplacement des noms des fonctions par leurs équivalents mathématiques
    expression = expression.replace("sin", "math.sin")
    expression = expression.replace("cos", "math.cos")
    expression = expression.replace("tan", "math.tan")
    expression = expression.replace("ln", "math.log")
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return "Error"

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        expression = entry.get()
        result = evaluate_expression(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in ["sin", "ln", "tan"]:
        entry.insert(tk.END, f"{text}(")
    elif text == ")":
        entry.insert(tk.END, ")")
    elif text == "(":
        entry.insert(tk.END, "(")
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0),
    ("ln", 1, 4), ("sin", 2, 4), ("cos", 3, 4), ("tan", 4, 4),
    ("(", 5, 2), (")", 5, 1)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=10, bd=5, bg="#f0f0f0", activebackground="#cccccc", highlightthickness=0)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", click)

root.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
root.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)
#yes
root.mainloop()