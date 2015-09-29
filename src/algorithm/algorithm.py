from movements_module import generate_states_moving_rows
from rotation_module import rotate_matrix_to_left

P = 0
Y = 1
O = 2
G = 3
H = 4
E = -1


example_mat = [[E, H, E, E],
			   [P, Y, P, O],
			   [O, G, O, G],
			   [G, P, G, Y],
			   [Y, O, Y, P]]

NOTCH_SYMBOL = 4
UP = -1
DOWN = 1

notch_row = 0
notch_column = 0
babylon_tower = []

# Contains all the states that are open
open_states = []

# Contains all the states that are close
closed_states = []



def init_babylon_tower(pInitialState):
    global babylon_tower
    babylon_tower = pInitialState
    set_notch()

def set_notch():
    global notch_column
    global notch_row
    for row_index, row in enumerate(babylon_tower):
        for col_index, element in enumerate(row):
            if element == NOTCH_SYMBOL:
                notch_column = col_index
                notch_row = row_index

def move_notch(pMovements, pDirection):
    global notch_row
    global notch_column
    global babylon_tower
    newState = babylon_tower
    direction_counter = pDirection
    while pMovements != 0:
        temp = babylon_tower[notch_row+pDirection][notch_column]
        newState[notch_row][notch_column] = temp
        newState[notch_row+pDirection][notch_column] = NOTCH_SYMBOL
        notch_row += pDirection
        pMovements -= 1
        return newState
    
def print_data():
    print (notch_row)
    print (notch_column)
    print (babylon_tower)

def get_notch_moves():
    result = []
    direction = 0
    movements = 0
    for index,row in enumerate(babylon_tower):
        movements = index - notch_row
        if movements != 0:
            if movements < 0:
                direction = UP
            else:
                direction = DOWN
            result += move_notch(abs(movements),direction)
    return result


# Testing
print(example_mat)
print(rotate_matrix_to_left(example_mat))
print(generate_states_moving_rows(example_mat, open_states, closed_states))




