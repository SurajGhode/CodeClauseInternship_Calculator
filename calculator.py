import tkinter as tk
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x800")

        self.result_var = tk.StringVar()

        entry = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right')
        entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'sqrt', 'pow', 'sin',
            'cos', 'tan', 'log'
        ]

        row_val = 1
        col_val = 0

        for button_text in buttons:
            button = tk.Button(self, text=button_text, width=8, height=4, font=("Arial", 16), command=lambda b=button_text: self.on_button_click(b))
            button.grid(row=row_val, column=col_val, padx=10, pady=10)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, button_text):
        current_result = self.result_var.get()

        if button_text == '=':
            try:
                result = str(eval(current_result))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'C':
            self.result_var.set("")  # Clear the entry field
        elif button_text == 'sqrt':
            try:
                result = str(math.sqrt(eval(current_result)))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'pow':
            try:
                result = str(eval(current_result) ** 2)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'sin':
            try:
                result = str(math.sin(math.radians(eval(current_result))))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'cos':
            try:
                result = str(math.cos(math.radians(eval(current_result))))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'tan':
            try:
                result = str(math.tan(math.radians(eval(current_result))))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        elif button_text == 'log':
            try:
                result = str(math.log10(eval(current_result)))
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_result += button_text
            self.result_var.set(current_result)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
