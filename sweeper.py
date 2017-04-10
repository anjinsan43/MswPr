import tkinter as tk
#messagebox is not imported automatically w/ tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
from random import random as rand
from functools import partial


class Square(object):
    """ class to use for each square """
    def __init__(self):
        self.mine_yn = False
        self.flag_yn = False
        # prox_num is thenumber of nearby mines,
        # parse_mines() will fill this in.
        self.prox_num = 0
        self.button = None  # for ttk.Button instance(s).
        
        
        
def create_mine_field():
    global mine_frame
    global sqr_dict

    mine_frame = tk.Toplevel(root)
    mine_frame.grid()
    #what to do if user hit 'X' to close window.
    mine_frame.protocol("WM_DELETE_WINDOW", mine_frame_close)
    
    root.withdraw()

    # create grid of squares (buttons)
    for x in range(int(x_str.get() )):
        for y in range(int(y_str.get() )):
            sqr_dict[coord(x,y)] = Square()
            
            #populate with mines
            if ( rand()*100 < int(mines_pct_str.get()) ):
                sqr_dict[coord(x,y)].mine_yn = True
            else:
                sqr_dict[coord(x,y)].mine_yn = False 

            # draw boxes
            if sqr_dict[coord(x,y)].mine_yn:  
                t = '*'
            else: t = ' '
            cmd = partial(left_click, x, y)
            sqr_dict[coord(x,y)].button = ttk.Button(mine_frame,
                                          text=t, width=3,command=cmd)
            sqr_dict[coord(x,y)].button.grid(column=x, row=y)
            #mine_frame.update() #???
            
    parse_mines()


def parse_mines():
    """Look at how many mines are next to a given square,
    store this number in each Square instance. Each
    Square instance is stored inside of sqr_dict. """
    
    global sqr_dict
    global mine_frame
    #print('in parse_mines, sqr_dict='+str(sqr_dict))

    def try_a_square(x,y): #sq = coordinate string(key)
        try:
            if sqr_dict[coord(x,y)].mine_yn == True:  return 1
            if sqr_dict[coord(x,y)].mine_yn == False: return 0
        except KeyError:
            #print('KeyError for '+sq)
            return 0
            
    n = 0
    for x in range(int(x_str.get() )):
        for y in range(int(y_str.get() )):
            #check the 8 adjacent squares.
            n = n + try_a_square( x+1,y+1 ) #SE
            n = n + try_a_square( x+1,y   ) #E
            n = n + try_a_square( x+1,y-1 ) #NE
            n = n + try_a_square( x,  y+1 ) #S
            n = n + try_a_square( x,  y-1 ) #N
            n = n + try_a_square( x-1,y+1 ) #SW
            n = n + try_a_square( x-1,y   ) #W
            n = n + try_a_square( x-1,y-1 ) #NW

            if sqr_dict[coord(x,y)].mine_yn == False:
                sqr_dict[coord(x,y)].prox_num = n
                sqr_dict[coord(x,y)].button.configure(text=str(n)) #(debug) show n on each button.
            n = 0
        mine_frame.update()
    
    
def root_close():
    if tkMessageBox.askokcancel("Quit", "You don't want to quit."):
        root.destroy()

def mine_frame_close(): #back to main menu
    root.deiconify()  # un-withdraw root
    mine_frame.destroy()


    
def coord(x,y):
    return 'x'+str(x)+'y'+str(y)
    

def left_click(x,y):
    print(coord(x,y))

sqr_dict = {}
root = tk.Tk()
root.title("MS")

x_str = tk.StringVar()
x_str.set('25')
y_str = tk.StringVar()
y_str.set('15')

mines_pct_str = tk.StringVar()
mines_pct_str.set('30')


startframe = ttk.Frame(root)


# X coordinate entry box + label
ttk.Label(root,text="x").pack() #grid(row=1,column=3)
x_entry_box = ttk.Entry(root, textvariable=x_str)
x_entry_box.pack() #grid(row=1,column=4)

# Y coordinate entry box + label
ttk.Label(root,text="y").pack() #grid(row=1,column=1)
y_entry_box = ttk.Entry(root, textvariable=y_str)
y_entry_box.pack() #grid(row=1,column=2)

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