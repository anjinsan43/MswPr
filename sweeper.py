from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Mine Sweeper")

mainframe = ttk.Frame(root)


for y in range(5):
	for x in range(5):
		ttk.Button(root, text='*', width=3 ).grid(column=x, row=y)

root.mainloop()