import constants_module as K


def set_notch(pBabylonTower):
    for row_index, row in enumerate(pBabylonTower):
        for col_index, element in enumerate(row):
            if element == K.NOTCH_SYMBOL:
                return [row_index,col_index]
                

def move_notch(pBabylonTower,pMovements, pDirection):
    notch = set_notch(pBabylonTower)
    notch_row = notch[0]
    notch_column = notch[1]
    newState = pBabylonTower
    direction_counter = pDirection
    while pMovements != 0:
        temp = pBabylonTower[notch_row+pDirection][notch_column]
        newState[notch_row][notch_column] = temp
        newState[notch_row+pDirection][notch_column] = K.NOTCH_SYMBOL
        notch_row += pDirection
        pMovements -= 1
        return newState

def get_notch_moves(pBabylonTower):
    notch = set_notch(pBabylonTower)
    notch_row = notch[0]
    notch_column = notch[1]
    result = []
    direction = 0
    movements = 0
    for index,row in enumerate(pBabylonTower):
        movements = index - notch_row
        if movements != 0:
            if movements < 0:
                direction = K.UP
            else:
                direction = K.DOWN
            result += [move_notch(pBabylonTower,abs(movements),direction)]
    return result
