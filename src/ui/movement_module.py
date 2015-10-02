import constants_module as K
<<<<<<< HEAD
from rotation_module import *


notch_pos = 0

def init_notch(pBabylonTower):
    [notch_row,notch_column] = set_notch(pBabylonTower)
    [space_row,space_column] = set_free_space(pBabylonTower)

    while notch_column != space_column:
        pBabylonTower = shift(pBabylonTower,space_row,K.RIGHT)
        [space_row,space_column] = set_free_space(pBabylonTower)
    while notch_row != 0:
        pBabylonTower = move_up(pBabylonTower,notch_row,notch_column)
        notch_row -= 1
    return pBabylonTower
=======
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3

def set_notch(pBabylonTower):
    for row_index, row in enumerate(pBabylonTower):
        for col_index, element in enumerate(row):
            if element == K.NOTCH_SYMBOL:
                return [row_index,col_index]
<<<<<<< HEAD

def set_free_space(pBabylonTower):
    for row_index, row in enumerate(pBabylonTower):
        for col_index, element in enumerate(row):
            if element != K.E:
                return [row_index,col_index]


def move_up(pBabylonTower,notch_row,notch_column,id_move):
=======
                

def move_up(pBabylonTower,notch_row,notch_column):
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    newState = ()
    newState += pBabylonTower[:notch_row-1]

    newState += (pBabylonTower[notch_row-1][:notch_column]+
                (K.NOTCH_SYMBOL,)+
                pBabylonTower[notch_row-1][notch_column+1:],)
    
    newState += (pBabylonTower[notch_row][:notch_column]+
                (pBabylonTower[notch_row-1][notch_column],)+
                pBabylonTower[notch_row][notch_column+1:],)

    newState += pBabylonTower[notch_row+1:]
<<<<<<< HEAD
    return (newState,K.NOTCH_UP_MESSAGE.replace("%i",str(id_move)))

def move_down(pBabylonTower,notch_row,notch_column,id_move):
=======
    return newState

def move_down(pBabylonTower,notch_row,notch_column):
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    newState = ()
    newState += pBabylonTower[:notch_row]
    
    newState += (pBabylonTower[notch_row][:notch_column]+
                (pBabylonTower[notch_row+1][notch_column],)+
                pBabylonTower[notch_row][notch_column+1:],)
    
    newState += (pBabylonTower[notch_row+1][:notch_column]+
                (K.NOTCH_SYMBOL,)+
                pBabylonTower[notch_row+1][notch_column+1:],)
    
    newState += pBabylonTower[notch_row+2:]
<<<<<<< HEAD
    return (newState,K.NOTCH_DOWN_MESSAGE.replace("%i",str(id_move)))

def move_notch(result,pBabylonTower,pMovements, pDirection,notch_row,notch_column):
    newState = ()
    global notch_pos
    if pMovements != 0:
        if pDirection == K.UP:
            newState = move_up(pBabylonTower,notch_row,notch_column,abs(notch_pos-notch_row-pDirection))
        else:
            newState = move_down(pBabylonTower,notch_row,notch_column,abs(notch_pos-notch_row-pDirection))
        result += (newState,)
        return move_notch(result,newState[0],pMovements-1,pDirection,notch_row+pDirection,notch_column)
=======
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
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    else:
        return result

def get_notch_moves(pBabylonTower):
    [notch_row,notch_column] = set_notch(pBabylonTower)
<<<<<<< HEAD
    global notch_pos
    notch_pos = notch_row
=======
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    result = []
    up_movements = notch_row
    down_movements = 4-notch_row
    result += move_notch([],pBabylonTower,up_movements,K.UP,notch_row,notch_column)
    result += move_notch([],pBabylonTower,down_movements,K.DOWN,notch_row,notch_column)
    return result
<<<<<<< HEAD

"""
print(K.mat)
#print(move_down(K.mat,0,1))
#print(move_notch([],K.mat,1,1,0,1))
result = get_notch_moves(K.mat)
for element in result:
    print(element)

((0, 3, 0, 1), (1, 2, 1, 2), (-1, 4, -1, -1), (2, 0, 2, 3), (3, 1, 3, 0))
(((0, 3, 0, 1), (1, 4, 1, 2), (-1, 2, -1, -1), (2, 0, 2, 3), (3, 1, 3, 0)), 'Mover muesca hacia arriba 1 espacios.')
(((0, 4, 0, 1), (1, 3, 1, 2), (-1, 2, -1, -1), (2, 0, 2, 3), (3, 1, 3, 0)), 'Mover muesca hacia arriba 2 espacios.')
(((0, 3, 0, 1), (1, 2, 1, 2), (-1, 0, -1, -1), (2, 4, 2, 3), (3, 1, 3, 0)), 'Mover muesca hacia abajo 1 espacios.')
(((0, 3, 0, 1), (1, 2, 1, 2), (-1, 0, -1, -1), (2, 1, 2, 3), (3, 4, 3, 0)), 'Mover muesca hacia abajo 2 espacios.')
"""

=======
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
