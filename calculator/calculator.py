from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title('Calculator')
        master.geometry('400x600')
        master.resizable(False, False)
        master.config(bg='black')   

        self.equation = StringVar()
        self.entry_value = ''
        Entry(master, font=('Arial', 20), textvariable=self.equation, bd=20, insertwidth=4, width=17, bg='powder blue', justify='right').grid(row=0, column=0, columnspan=4)

        Button(master, text='7', font=('Arial', 20), command=lambda: self.show(7)).grid(row=1, column=0)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def slove(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()