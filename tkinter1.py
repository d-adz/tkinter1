from tkinter import *
from tkinter import ttk

class FeetToMetres:

    def __init__(self, root):
        root.title("Feet Conversion")

        mainframe = ttk.Frame(root, padding=(3,3,12,12))
        mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

        # --- Metres section ---
        self.feet = StringVar()
        feet_entry = ttk.Entry(mainframe, width=7, textvariable=self.feet)
        feet_entry.grid(column=2, row=1, sticky=(W,E))

        self.meters = StringVar()
        ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W,E))

        ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

        # --- Inches section ---
        self.feet2 = StringVar()
        feet_entry2 = ttk.Entry(mainframe, width=7, textvariable=self.feet2)
        feet_entry2.grid(column=2, row=4, sticky=(W,E))  # entry on row 4

        self.inches = StringVar()
        ttk.Label(mainframe, textvariable=self.inches).grid(column=2, row=5, sticky=(W,E))  # result on row 5

        ttk.Button(mainframe, text="Calculate", command=self.calculate2).grid(column=3, row=6, sticky=W)

        ttk.Label(mainframe, text="feet").grid(column=3, row=4, sticky=W)
        ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=5, sticky=E)
        ttk.Label(mainframe, text="inches").grid(column=3, row=5, sticky=W)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        mainframe.columnconfigure(2, weight=1)
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        feet_entry.focus()
        root.bind("<Return>", self.calculate)

    def calculate(self, *args):
        try:
            value = float(self.feet.get())
            self.meters.set(round(0.3048 * value, 4))
        except ValueError:
            pass

    def calculate2(self, *args):
        try:
            value = float(self.feet2.get())
            self.inches.set(round(12 * value, 4))
        except ValueError:
            pass

root = Tk()
FeetToMetres(root)
root.mainloop()