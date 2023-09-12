import tkinter as tk
from calculator import (
    create_tokens,
    convert_to_postfix,
    evaluate_postfix,
)  # Import functions from calculator.py


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Basic Calculator")
        self.master.geometry("400x600")

        self.display_var = tk.StringVar()
        tk.Label(
            self.master, textvariable=self.display_var, font=("Arial", 24), anchor="e"
        ).grid(row=0, column=0, columnspan=4)

        buttons = [
            "7",
            "8",
            "9",
            "+",
            "4",
            "5",
            "6",
            "-",
            "1",
            "2",
            "3",
            "*",
            "0",
            ".",
            "=",
            "/",
            "^",
            "√",
            "C",
            "CE",
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            action = lambda x=button: self.button_click(x)
            tk.Button(
                self.master, text=button, command=action, width=10, height=2
            ).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def button_click(self, button_value):
        current_display = self.display_var.get()

        if button_value in ["+", "-", "*", "/", "^", "√"]:
            self.display_var.set(current_display + button_value)

        elif button_value == "C":
            self.display_var.set("")

        elif button_value == "CE":
            self.display_var.set(current_display[:-1])

        elif button_value == "=":
            try:
                tokens = create_tokens(current_display)
                postfix_tokens = convert_to_postfix(tokens)
                result = evaluate_postfix(postfix_tokens)
                self.display_var.set(result)
            except Exception as e:
                self.display_var.set("Error")

        else:
            self.display_var.set(current_display + button_value)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
