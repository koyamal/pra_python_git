from tkinter import *
from tkinter import ttk

def get_text():
    text = tx1.get()
    com = combo.get()
    print("text: " + text)
    print("com: " + com)

root = Tk()
root.title("Use Tkinter")

tx1 = StringVar()
label = ttk.Label(root, text="Hello Python!")
entry = ttk.Entry(root, textvariable=tx1)
button = ttk.Button(root, text="OK", command=lambda: get_text())

combo = ttk.Combobox(root, state='readonly')

combo["values"] = ("A", "B", "C")

combo.current(0)

label.grid(row=0, column=0)
entry.grid(row=0, column=1)
combo.grid(row=1, column=0)
button.grid(row=2, column=0)

root.mainloop()