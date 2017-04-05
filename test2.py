import tkinter as tk
#messagebox is not imported automatically w/ tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import ttk
from random import random as rand


class Square(object):
    """ class to use for each square """
    def __init__(self):
        self.mine_yn = False
        self.flag_yn = False
        self.prox_num = 0   # number of nearby mines, parse_mines() will fill this in.
        self.button = None  # ttk.Button instance.
        
        
def parse_mines():
    """Look at how many mines are next to a given square,
    store in each Square instance that is inside of sqr_dict. """
    global sqr_dict
    global mine_frame
    print('in parse_mines, sqr_dict='+str(sqr_dict))

    def try_a_square(sq): #sq = coordinate string(key)
        try:
            if sqr_dict[sq].mine_yn == True:  return 1
            if sqr_dict[sq].mine_yn == False: return 0
        except KeyError:
            print('KeyError for '+sq)
            return 0
            
    n = 0
    for x in range(5):
        for y in range(4):
            #check the 8 adjacent squares.
            n = n + try_a_square('x'+str(x+1)+'y'+str(y+1))
            n = n + try_a_square('x'+str(x+1)+'y'+str(y  ))
            n = n + try_a_square('x'+str(x+1)+'y'+str(y-1))
            n = n + try_a_square('x'+str(x  )+'y'+str(y+1))
            n = n + try_a_square('x'+str(x  )+'y'+str(y-1))
            n = n + try_a_square('x'+str(x-1)+'y'+str(y+1))
            n = n + try_a_square('x'+str(x-1)+'y'+str(y  ))
            n = n + try_a_square('x'+str(x-1)+'y'+str(y-1))
            if sqr_dict[('x'+str(x)+'y'+str(y))].mine_yn == False:
                (sqr_dict[('x'+str(x)+'y'+str(y))]).prox_num = n
            
            print('x'+str(x)+'y'+str(y)+': '+str(n)) #(debug) print n for each sq
            #sqr_dict[('x'+str(x)+'y'+str(y))].button.text=(str(n)) #(debug) show n on each button.
            n = 0
            
            

def create_mine_field():
    global mine_frame
    global sqr_dict
    
    sqr_dict = {}
    
    mine_frame = tk.Toplevel(root)
    mine_frame.grid()
    
    #what to do if user hit 'X' to close window.
    mine_frame.protocol("WM_DELETE_WINDOW", mine_frame_close)
    

    # create grid of squares (buttons)
    for x in range(5):
        for y in range(4):
            coord = 'x'+str(x) + 'y'+str(y)
            sqr_dict[coord] = Square()
            #print('coord='+coord) #debug
            #populate with mines
            if ( rand()*100 < mines_pct ):
                sqr_dict[coord].mine_yn = True
                print(str(sqr_dict[coord].mine_yn))
            else:
                sqr_dict[coord].mine_yn = False 

                
            if sqr_dict[coord].mine_yn:  
                t = '*'
            else: t = ' '
            # draw boxes
            sqr_dict[coord].button = ttk.Button(mine_frame, text=t, width=3 )
            sqr_dict[coord].button.grid(column=x, row=y)
            # done, next: parse!
            print('in create_mines, sqr_dict='+str(sqr_dict))
            
    parse_mines()



def root_close():
    root.destroy()

def mine_frame_close():
    root.destroy()


root = tk.Tk()
root.title("MineSweeper")

mines_pct = 20
start_button = ttk.Button(root,text="Start",command=create_mine_field)
start_button.grid()
root.mainloop()