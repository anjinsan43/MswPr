import tkinter as tk
#messagebox is not imported automatically w/ tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
from random import random as rand
from functools import partial
from time import sleep



class Square(object):
    """ class to use for each square """
    def __init__(self):
        self.mine_yn = False
        self.flag_yn = False
        self.Qmark_yn = False
        self.cleared = False
        # prox_num is the number of nearby mines,
        # parse_mines() will fill this in.
        self.prox_num = 0
        self.button = None  # for tk.Button instance(s).
        
        
        
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
            #create button for square with command callback func.
            cmd_L = partial(left_click, x, y)
            cmd_R = partial(right_click, x, y)
            sqr_dict[coord(x,y)].button = tk.Button(mine_frame,
                                          text=t, width=1,
                                          command=cmd_L)
            sqr_dict[coord(x,y)].button.bind('<Button-3>', cmd_R) #right click
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

    def try_a_square(x,y): 
        try:
            if sqr_dict[coord(x,y)].mine_yn == True:  return 1
            if sqr_dict[coord(x,y)].mine_yn == False: return 0
        except KeyError:
            return 0
            
    n = 0
    for x in range(int(x_str.get() )):
        for y in range(int(y_str.get() )):
            #check the 8 adjacent squares.
            n = n + try_a_square( x,  y-1 ) #N
            n = n + try_a_square( x,  y+1 ) #S
            n = n + try_a_square( x+1,y   ) #E
            n = n + try_a_square( x-1,y   ) #W
            n = n + try_a_square( x+1,y-1 ) #NE
            n = n + try_a_square( x-1,y-1 ) #NW
            n = n + try_a_square( x+1,y+1 ) #SE
            n = n + try_a_square( x-1,y+1 ) #SW

            if sqr_dict[coord(x,y)].mine_yn == False:
                sqr_dict[coord(x,y)].prox_num = n
                 #(debug) show n on each button.
                sqr_dict[coord(x,y)].button.configure(text=str(n))
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
    

def clear_sq(x,y):
    global sqr_dict
    sqr_dict[coord(x,y)].button.config( state="disabled",
                                        relief="sunken",
                                        text="x" )
    sqr_dict[coord(x,y)].cleared = True
    sleep(0.075)
    mine_frame.update()
    
    
def check_can_open(x,y):
    global sqr_dict
    
    try:
        sq = sqr_dict[coord(x,y)]
    except KeyError:
        print('no-go: ' + coord(x,y))
        return False
        
    if ((not sq.cleared and sq.prox_num == 0) and
       (not (sq.flag_yn or sq.Qmark_yn))):
        return True
    else:
        return False
        
        
            
def left_click(x,y):
    global sqr_dict
    sq = sqr_dict[coord(x,y)]
    
    #Hit a mine.
    if (sq.mine_yn) and (not sq.flag_yn): game_over()

    #Hit an open square, now open up field...
    # non-recursive depth first search algorithm
    if check_can_open(x,y):
        S = [[x,y]]
        while len(S):
            x,y = S.pop()
            sq = sqr_dict[coord(x,y)]
            clear_sq(x,y)
            
            #check North
            if check_can_open(x,y-1):
                S.append([x,y-1])
                
            #check South
            if check_can_open(x,y+1):
                S.append([x,y+1])
                
            #check East
            if check_can_open(x+1,y):
                S.append([x+1,y])
                
            #check West
            if check_can_open(x-1,y):
                S.append([x-1,y])
        
    
    
def right_click(x,y,b):
    global sqr_dict
    print('Right click on ' + coord(x,y))
    
    sq = sqr_dict[coord(x,y)]
    if not sq.cleared:
        if not sq.flag_yn and not sq.Qmark_yn:
            sqr_dict[coord(x,y)].flag_yn = True
            sqr_dict[coord(x,y)].Qmark_yn = False
            sqr_dict[coord(x,y)].button.config(text='F')
            return
        if sq.flag_yn:
            sqr_dict[coord(x,y)].flag_yn = False
            sqr_dict[coord(x,y)].Qmark_yn = True
            sqr_dict[coord(x,y)].button.config(text='?')
            return
        if sq.Qmark_yn:
            sqr_dict[coord(x,y)].flag_yn = False
            sqr_dict[coord(x,y)].Qmark_yn = False
            sqr_dict[coord(x,y)].button.config(text=' ')
            return
            
    
def game_over(): mine_frame_close()
    

sqr_dict = {}
root = tk.Tk()
root.title("MS")

x_str = tk.StringVar()
x_str.set('35')
y_str = tk.StringVar()
y_str.set('20')

mines_pct_str = tk.StringVar()
mines_pct_str.set('10')


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