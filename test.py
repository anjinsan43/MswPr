



def left_click(x,y):
    global sqr_dict
    sq = sqr_dict[coord(x,y)]

    
    def open_field(x,y):
        if (sq.prox_num == 0):
        
        
        sqr_dict[coord(x,y)].button.config( state="disabled",
                                            relief="sunken",
                                            text="" )
    
    if (sq.mine_yn) and (not sq.flag_yn): game_over()
    
    if (sq.prox_num == 0):
        