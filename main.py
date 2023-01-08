import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        # Create the display
        self.display = tk.Entry(root, width=40, bg="#eee")
        self.display.grid(row=0, column=0, columnspan=5)

        # Create the buttons
        self.button_1 = tk.Button(root, text="1", command=lambda: self.add_to_display("1"))
        self.button_2 = tk.Button(root, text="2", command=lambda: self.add_to_display("2"))
        self.button_3 = tk.Button(root, text="3", command=lambda: self.add_to_display("3"))
        self.button_4 = tk.Button(root, text="4", command=lambda: self.add_to_display("4"))
        self.button_5 = tk.Button(root, text="5", command=lambda: self.add_to_display("5"))
        self.button_6 = tk.Button(root, text="6", command=lambda: self.add_to_display("6"))
        self.button_7 = tk.Button(root, text="7", command=lambda: self.add_to_display("7"))
        self.button_8 = tk.Button(root, text="8", command=lambda: self.add_to_display("8"))
        self.button_9 = tk.Button(root, text="9", command=lambda: self.add_to_display("9"))
        self.button_0 = tk.Button(root, text="0", command=lambda: self.add_to_display("0"))
        self.button_add = tk.Button(root, text="+", command=lambda: self.add_to_display("+"))
        self.button_subtract = tk.Button(root, text="-", command=lambda: self.add_to_display("-"))
        self.button_multiply = tk.Button(root, text="*", command=lambda: self.add_to_display("*"))
        self.button_divide = tk.Button(root, text="/", command=lambda: self.add_to_display("/"))
        self.button_equal = tk.Button(root, text="=", command=self.calculate)
        self.button_clear = tk.Button(root, text="AC", command=self.clear)

        # Add the buttons to the grid
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)
        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)
        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)
        self.button_0.grid(row=4, column=0)
        self.button_add.grid(row=4, column=1)
        self.button_subtract.grid(row=4, column=2)
        self.button_multiply.grid(row=5, column=0)
        self.button_divide.grid(row=5, column=1)
        self.button_equal.grid(row=5, column=2)
        self.button_clear.grid(row=6, column=1)
        
    def add_to_display(self, value):
        self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

root = tk.Tk()
calculator = Calculator(root)
root.mainloop()