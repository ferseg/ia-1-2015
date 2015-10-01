import constants_module as K

def set_notch(pBabylonTower):
    for row_index, row in enumerate(pBabylonTower):
        for col_index, element in enumerate(row):
            if element == K.NOTCH_SYMBOL:
                return [row_index,col_index]
                

def move_up(pBabylonTower,notch_row,notch_column):
    newState = ()
    newState += pBabylonTower[:notch_row-1]

    newState += (pBabylonTower[notch_row-1][:notch_column]+
                (K.NOTCH_SYMBOL,)+
                pBabylonTower[notch_row-1][notch_column+1:],)
    
    newState += (pBabylonTower[notch_row][:notch_column]+
                (pBabylonTower[notch_row-1][notch_column],)+
                pBabylonTower[notch_row][notch_column+1:],)

    newState += pBabylonTower[notch_row+1:]
    return newState

def move_down(pBabylonTower,notch_row,notch_column):
    newState = ()
    newState += pBabylonTower[:notch_row]
    
    newState += (pBabylonTower[notch_row][:notch_column]+
                (pBabylonTower[notch_row+1][notch_column],)+
                pBabylonTower[notch_row][notch_column+1:],)
    
    newState += (pBabylonTower[notch_row+1][:notch_column]+
                (K.NOTCH_SYMBOL,)+
                pBabylonTower[notch_row+1][notch_column+1:],)
    
    newState += pBabylonTower[notch_row+2:]
    return newState

def move_notch(result,pBabylonTower,pMovements, pDirection,notch_row,notch_column):
    newState = ()
    if pMovements != 0:
        if pDirection == K.UP:
            newState = move_up(pBabylonTower,notch_row,notch_column)
        else:
            newState = move_down(pBabylonTower,notch_row,notch_column)
        result += (newState,)
        return move_notch(result,newState,pMovements-1,pDirection,notch_row+pDirection,notch_column)
    else:
        return result

def get_notch_moves(pBabylonTower):
    [notch_row,notch_column] = set_notch(pBabylonTower)
    result = []
    up_movements = notch_row
    down_movements = 4-notch_row
    result += move_notch([],pBabylonTower,up_movements,K.UP,notch_row,notch_column)
    result += move_notch([],pBabylonTower,down_movements,K.DOWN,notch_row,notch_column)
    return result
