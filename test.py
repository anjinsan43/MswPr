

def clear_sq(x,y):
    global sqr_dict
    sqr_dict[coord(x,y)].button.config( state="disabled",
                                        relief="sunken",
                                        text="" )
                                        
def open_field(x,y):
    global sqr_dict
    sq = sqr_dict[coord(x,y)]
    
    clear_sq(x,y)
    
    if sqr_dict[coord(x,y)]
                                        

def left_click(x,y):
    global sqr_dict
    sq = sqr_dict[coord(x,y)]
    
    if (sq.mine_yn) and (not sq.flag_yn): game_over()
    
    if (sq.prox_num == 0) and
            (not (sq.flag_yn or sq.Qmark_yn))): clear_sq(x,y)
        
        