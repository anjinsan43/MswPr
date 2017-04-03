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
    print('in parse_mines, sqr_dict='+str(sqr_dict))

    def try_a_square(sq): #sq = coordinate string(key)
        try:
            if sqr_dict[sq].mine_yn == True:  return 1
            if sqr_dict[sq].mine_yn == False: return 0
        except KeyError:
            print('KeyError for '+sq)
            return 0
            
    n = 0
    for x in range(int(x_str.get() )):
        for y in range(int(y_str.get() )):
            #check the 8 adjacent squares.
            n = n + try_a_square('x'+str(x+1)+'y'+str(y+1))
            n = n + try_a_square('x'+str(x+1)+'y'+str(y  ))
            n = n + try_a_square('x'+str(x+1)+'y'+str(y-1))
            n = n + try_a_square('x'+str(x  )+'y'+str(y+1))
            n = n + try_a_square('x'+str(x  )+'y'+str(y-1))
            n = n + try_a_square('x'+str(x-1)+'y'+str(y+1))
            n = n + try_a_square('x'+str(x-1)+'y'+str(y  ))
            n = n + try_a_square('x'+str(x-1)+'y'+str(y-1))
            if sqr_dict['x'+str(x)+'y'+str(y)].mine_yn == False:
                sqr_dict['x'+str(x)+'y'+str(y)].prox_num = n
            
            print('x'+str(x)+'y'+str(y)+': '+str(n)) #(debug) print n for each sq
            sqr_dict['x'+str(x)+'y'+str(y)].button.text=(str(n)) #(debug) show n on each button. (not working)
            n = 0
            #root.update()
            
        
        
def create_mine_field():
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
            sqr_dict[coord] = Square 
            #print('coord='+coord) #debug
            #populate with mines
            if ( rand()*100 < int(mines_pct_str.get()) ):
                sqr_dict[coord].mine_yn = True 
            else:
                sqr_dict[coord].mine_yn = False 

            # draw boxes
            if sqr_dict[coord].mine_yn:  
                t = '*'
            else: t = ' '
            
            sqr_dict[coord].button = ttk.Button(mine_frame, text=t, width=3 )
            sqr_dict[coord].button.grid(column=x, row=y)
            # done, next: parse!
            print('in create_mines, sqr_dict='+str(sqr_dict))
            #mine_frame.update() #???
            parse_mines()



def root_close():
    if tkMessageBox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def mine_frame_close(): #back to main menu
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