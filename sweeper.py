import tkinter as tk
#messagebox is not imported automatically w/ tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
import random


def draw_mine_field():
	global sqr_list
	global mine_frame
	
	sqr_list = []
	
	mine_frame = tk.Toplevel(root)
	mine_frame.grid()
	#user hit 'X' to close window.
	mine_frame.protocol("WM_DELETE_WINDOW", mine_frame_close)
	
	root.withdraw()

	for a in range(int(x_str.get() )):
		for b in range(int(y_str.get() )):
			sqr_list.append(ttk.Button(mine_frame, text='[]', width=3 ).grid(column=a, row=b))

			
def root_close():
	if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
		root.destroy()

def mine_frame_close():
	root.deiconify()  # un-withdraw root
	mine_frame.destroy()

	
root = tk.Tk()
root.title("MS")

x_str = tk.StringVar()
x_str.set('4')
y_str = tk.StringVar()
y_str.set('2')

mines_pct_str = tk.StringVar()
mines_pct_str.set('20')


startframe = ttk.Frame(root)


# Y coordinate entry box + label
ttk.Label(root,text="y").pack() #grid(row=1,column=1)
y_entry_box = ttk.Entry(root, textvariable=y_str)
y_entry_box.pack() #grid(row=1,column=2)

# X coordinate entry box + label
ttk.Label(root,text="x").pack() #grid(row=1,column=3)
x_entry_box = ttk.Entry(root, textvariable=x_str)
x_entry_box.pack() #grid(row=1,column=4)

# number of mines entry box + label
ttk.Label(root,text="percent mines").pack() #grid(row=1,column=3)
mines_entry_box = ttk.Entry(root, textvariable=mines_pct_str)
mines_entry_box.pack() #grid(row=1,column=4)


#Start and Quit buttons
start_button = ttk.Button(root,text="Start",command=draw_mine_field)
start_button.pack() #grid(row=2,column=1)
quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack() #grid(row=2,column=2)

#user hit 'X' to close window.
root.protocol("WM_DELETE_WINDOW", root_close)

root.mainloop()
print(sqr_list)