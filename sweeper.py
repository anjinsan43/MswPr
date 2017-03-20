import tkinter as tk
#messagebox is not imported automatically w/ tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
import random


def on_closing():
	if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
		try mine_frame.destroy():
			except: pass
		root.destroy()
	
	

def draw_mine_field():

	mine_frame = tk.Toplevel(root)
	mine_frame.grid()
	root.withdraw()

	for a in range(int(x_str.get() )):
		for b in range(int(y_str.get() )):
			ttk.Button(mine_frame, text='[]', width=3 ).grid(column=a, row=b)


	
root = tk.Tk()
root.title("MS")

x_str = tk.StringVar()
x_str.set('20')
y_str = tk.StringVar()
y_str.set('10')


startframe = ttk.Frame(root)


# Y coordinate entry box + label
ttk.Label(root,text="y").grid(row=1,column=1)
y_entry_box = ttk.Entry(root, textvariable=y_str)
y_entry_box.grid(row=1,column=2)

# X coordinate entry box + label
ttk.Label(root,text="x").grid(row=1,column=3)
x_entry_box = ttk.Entry(root, textvariable=x_str)
x_entry_box.grid(row=1,column=4)

#Start and Quit buttons
start_button = ttk.Button(root,text="Start",command=draw_mine_field)
start_button.grid(row=2,column=1)
quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.grid(row=2,column=2)

#user hit 'X' to close window.
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
