import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 18), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

for (text, row, column) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), padx=20, pady=10, bd=5, bg="#f0f0f0", activebackground="#cccccc", highlightthickness=0)
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")
    button.bind("<Button-1>", click)

root.grid_columnconfigure((0, 1, 2, 3), weight=1)
root.grid_rowconfigure((1, 2, 3, 4, 5), weight=1)

root.mainloop()
#test

#zafezafezfe