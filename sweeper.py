import tkinter as tk
from tkinter import ttk
import random


def draw_mine_field(x=5, y=3):

	mine_frame = tk.Toplevel(root)
	mine_frame.grid()
	root.withdraw()

	for b in range(y):
		for a in range(x):
			ttk.Button(mine_frame, text='*', width=3 ).grid(column=a, row=b)


root = tk.Tk()
root.title("MS")

startframe = ttk.Frame(root)

ttk.Label(root,text="y").grid(row=1,column=1)
y_entry_box = ttk.Entry(root).grid(row=1,column=2)

ttk.Label(root,text="x").grid(row=1,column=3)
x_entry_box = ttk.Entry(root).grid(row=1,column=4)

ttk.Button(root,text="Start",command=draw_mine_field).grid(row=2,column=1)
ttk.Button(root,text="Quit",command=root.destroy).grid(row=2,column=2)


root.mainloop()
