from copy import copy, deepcopy
import constants_module as constants_m


# Moves the elements of the row one space to the right
def move_row_to_right(pRow):
    result = ()
    result += (pRow[len(pRow) - 1],)
    result += pRow[:-1]
    return result

# Moves the elements of the row one space to the left
def move_row_to_left(pRow):
    result = ()
    result += pRow[1:]
    result += (pRow[0],)
    return result

# Rotates the tower to the left.
def rotate_matrix_to_left(pMatrix):
    result = deepcopy(pMatrix)
    for current_row_index in range(0, len(pMatrix)):
        rotated_row = move_row_to_left(result[current_row_index])
        result[current_row_index] = rotated_row
    return result

def shift(pBabylonTower,pRow,pDirection):
    message = ""
    newRow = ()
    newState = ()
    newRow += pBabylonTower[:pRow]
    if pDirection == constants_m.RIGHT:
        newRow += (move_row_to_right(pBabylonTower[pRow]),)
        message = constants_m.SHR_MESSAGE.replace("%i",str(pRow+1))
    else:
        newRow += (move_row_to_left(pBabylonTower[pRow]),)
        message = constants_m.SHL_MESSAGE.replace("%i",str(pRow+1))
    newRow += pBabylonTower[pRow+1:]
    newState += (newRow,message)
    return newState

def get_shifts(pBabylonTower):
    result = []
    for row_index, row in enumerate(pBabylonTower):
        shl = shift(pBabylonTower,row_index,constants_m.LEFT)
        shr = shift(pBabylonTower,row_index,constants_m.RIGHT)
        if (pBabylonTower == shl[0]) and (pBabylonTower == shr[0]):
            pass
        elif shl[0] == shr[0]:
            result += (shl,)
        else:
            result += (shl,shr,)
    return result




    

