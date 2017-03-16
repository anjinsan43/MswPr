import tkinter as tk
from tkinter import messagebox as tkMessageBox  #messagebox is not imported automatically.
from tkinter import ttk
import random



def on_closing():
	if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()
	
	

def draw_mine_field(x=5, y=3):

	mine_frame = tk.Toplevel(root)
	mine_frame.grid()
	root.withdraw()

	for a in range(x):
		for b in range(y):
			ttk.Button(mine_frame, text='[]', width=3 ).grid(column=a, row=b)


			
root = tk.Tk()
root.title("MS")

x_str = tk.StringVar()
y_str = tk.StringVar()
startframe = ttk.Frame(root)

ttk.Label(root,text="y").grid(row=1,column=1)
y_entry_box = ttk.Entry(root).grid(row=1,column=2)

ttk.Label(root,text="x").grid(row=1,column=3)
x_entry_box = ttk.Entry(root).grid(row=1,column=4)

start_button = ttk.Button(root,text="Start",command=draw_mine_field)
start_button.grid(row=2,column=1)
quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.grid(row=2,column=2)

root.protocol("WM_DELETE_WINDOW", on_closing)  #user hit 'X' to close window.

root.mainloop()
