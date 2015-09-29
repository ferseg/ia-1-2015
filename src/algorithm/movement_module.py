import constants_module as K


example_mat = [[K.E,K.H, K.E, K.E],
			   [K.P, K.Y, K.P, K.O],
			   [K.O, K.G, K.O, K.G],
			   [K.G, K.P, K.G, K.Y],
			   [K.Y, K.O, K.Y, K.P]]


notch_row = 0
notch_column = 0

def set_notch(pBabylonTower):
    global notch_row
    global notch_column
    for row_index, row in enumerate(pBabylonTower):
        for col_index, element in enumerate(row):
            if element == K.NOTCH_SYMBOL:
                notch_column = col_index
                notch_row = row_index

def move_notch(pBabylonTower,pMovements, pDirection):
    global notch_column
    global notch_row
    set_notch(pBabylonTower)
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
    global notch_column
    global notch_row
    set_notch(pBabylonTower)
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
