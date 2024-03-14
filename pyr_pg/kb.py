def key_wasd(key_ar):
    player_move = None
    if key_ar[3+23] and key_ar[3+1]:
        player_move = "LUP"                    
    elif key_ar[3+23] and key_ar[3+4]:
        player_move = "RUP"                    
    elif key_ar[3+1] and key_ar[3+19] :
        player_move = "LWN"                    
    elif key_ar[3+4]  and key_ar[3+19]:
        player_move = "RWN"                
    elif key_ar[3+23]:
        player_move = "UP"                    
    elif key_ar[3+1]:
        player_move = "LEFT"                    
    elif key_ar[3+19]:
        player_move = "DOWN"
    elif key_ar[3+4]:
        player_move = "RIGHT"
        
    return player_move
