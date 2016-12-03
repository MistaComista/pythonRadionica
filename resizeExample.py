from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root, padding=(3,3,3,3))
frame = ttk.Frame(content, borderwidth=5, relief="sunken", width=200, height=50)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()

onevar.set(True)
twovar.set(True)
threevar.set(False)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))
namelbl.grid(column=2, row=0, columnspan=2, sticky=(N, W), padx=5)
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
name.grid(column=3, row=1, columnspan=2, sticky=(N, E, W), pady=5, padx=5)
one.grid(column=0, row=2)
two.grid(column=1, row=2)
three.grid(column=2, row=2)
ok.grid(column=3, row=2, sticky=(N, S, E, W))
cancel.grid(column=4, row=2, sticky=(N, S, E, W))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=1)
content.columnconfigure(1, weight=2)
content.columnconfigure(2, weight=0)
content.columnconfigure(3, weight=0)
content.columnconfigure(4, weight=0)
content.rowconfigure(0, weight=0)
content.rowconfigure(1, weight=0)
content.rowconfigure(2, weight=2)

root.mainloop()