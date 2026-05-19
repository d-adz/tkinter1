from tkinter import *
from tkinter import ttk


class calculations:
    def __init__(self,root):
        root.title("Calculator")

        mainframe = ttk.Frame(root, padding=(3,3,12,12))
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
      
        self.num1 = StringVar()
        ttk.Label(mainframe, text="Number 1:").grid(column=2, row=3, sticky=E)
        ttk.Entry(mainframe, width=7, textvariable=self.num1).grid(column=3, row=3, sticky=(W,E))

        self.num2 = StringVar()
        ttk.Label(mainframe, text="Number 2:").grid(column=2, row=4, sticky=E)
        ttk.Entry(mainframe, width=7, textvariable=self.num2).grid(column=3, row=4, sticky=(W,E))

        ttk.Label(mainframe, text="Welcome to Calculator").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="Select an Operation Below:").grid(column=3, row=2, sticky=W)

        ttk.Button(mainframe, text=" + ", command=self.addition).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text=" - ", command=self.subtraction).grid(column=4, row=5, sticky=W)
        ttk.Button(mainframe, text=" / ", command=self.division).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text=" X ", command=self.multiplication).grid(column=4, row=6, sticky=W)

        self.result = StringVar()
        ttk.Label(mainframe, text="Result: ").grid(column=6, row=4, sticky=W)
        ttk.Entry(mainframe, width=7, textvariable=self.result).grid(column=6, row=5, sticky=(W))


        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(3, weight=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def addition(self, *args): 
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.result.set(a+b)
        except ValueError:
            pass

       

    def subtraction(self, *args): 
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.result.set(a-b)
        except ValueError:
            pass


    def division(self, *args): 
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.result.set(a/b)
        except ValueError:
            pass

    def multiplication(self, *args): 
        try:
            a = float(self.num1.get())
            b = float(self.num2.get())
            self.result.set(a*b)
        except ValueError:
            pass




    



    

root = Tk()
calculations(root)
root.mainloop()