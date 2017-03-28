import tkinter as tk
#messagebox is not imported automatically w/ tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
from random import random as rand


class Square(object):
    """ container class to use for each square """
    def __init__(self):
        self.mine_yn = False
        self.flag_yn = False
        self.prox_num = 0   # parser() will change this.
        self.button = None  # ttk.Button instance.
        

def create_mine_field():
    global sqr_list
    global mine_frame
    global sqr_dict
    
    sqr_dict = {}
    
    mine_frame = tk.Toplevel(root)
    mine_frame.grid()
    
    #what to do if user hit 'X' to close window.
    mine_frame.protocol("WM_DELETE_WINDOW", mine_frame_close)
    
    root.withdraw()

    # create grid of squares (buttons)
    for x in range(int(x_str.get() )):
        for y in range(int(y_str.get() )):
            coord = 'x'+str(x) + 'y'+str(y)
            sqr_dict[coord] = Square #sqr_list.append(Square)
            #sqr_list[-1].x = x
            #sqr_list[-1].y = y
            
            #populate with mines
            if ( rand()*100 < int(mines_pct_str.get()) ):
                sqr_dict[coord].mine_yn = True #sqr_list[-1].mine_yn = True
            else:
                sqr_dict[coord].mine_yn = False #sqr_list[-1].mine_yn = False

            # draw boxes
            if sqr_dict[coord].mine_yn:  #sqr_list[-1].mine_yn:
                t = '*'
            else: t = ' '
            
            #sqr_list[-1].button = ttk.Button(mine_frame, text=t, width=3 )
            #sqr_list[-1].button.grid(column=x, row=y)
            sqr_dict[coord].button = ttk.Button(mine_frame, text=t, width=3 )
            sqr_dict[coord].button.grid(column=x, row=y)
            # done, next: parse!

def parse_mines():
    #loop over dictionary keys(coordinates)
        #look at the 8 adjacent squares
        #catch NameError for edges of board
    def try_a_sqare(sq): #sq = Square instance
        try:
            if sqr_dict[sq].mine_yn = True:  return 1
            if sqr_dict[sq].mine_yn = False: return 0
        except NameError:
            return 0
            

    for i in sqr_dict:  # i is a key/string
		#use regex for splitting x,y
		
		
def root_close():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def mine_frame_close():
    root.deiconify()  # un-withdraw root
    mine_frame.destroy()

    
root = tk.Tk()
root.title("MS")

x_str = tk.StringVar()
x_str.set('6')
y_str = tk.StringVar()
y_str.set('4')

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
start_button = ttk.Button(root,text="Start",command=create_mine_field)
start_button.pack() #grid(row=2,column=1)
quit_button = ttk.Button(root,text="Quit",command=root.destroy)
quit_button.pack() #grid(row=2,column=2)

#user hit 'X' to close window.
root.protocol("WM_DELETE_WINDOW", root_close)

root.mainloop()