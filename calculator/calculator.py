from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('250x380')
        master.resizable(False, False)
        master.config(bg='black')   

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, font=('Arial', 20), textvariable=self.equation, bd=20, insertwidth=4, width=14, bg='powder blue', justify='right').grid(row=0, column=0, columnspan=4)

        buttons = [
            ('(', ')', '%', '/'),
            ('1', '2', '3', '*'),
            ('4', '5', '6', '-'),
            ('7', '8', '9', '+'),
            ('c', '0', '.', '='),
        ]

        for i, button_row in enumerate(buttons):
            for j, button_text in enumerate(button_row):
                if button_text == '=':
                    Button(master, text=button_text, font=('Arial', 20), bg='green', fg='white', command=self.slove).grid(row=i+1, column=j, padx=1, pady=1)
                elif button_text == 'c':
                    Button(master, text=button_text, font=('Arial', 20), bg='red', fg='white', command=self.clear).grid(row=i+1, column=j, padx=1, pady=1)
                else:
                    Button(master, text=button_text, font=('Arial', 20), bg='gray', fg='white', command=lambda text=button_text: self.show(text)).grid(row=i+1, column=j, padx=1, pady=1)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def slove(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()