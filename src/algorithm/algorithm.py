from copy import copy, deepcopy

P = 0
Y = 1
O = 2
G = 3
H = 4
E = -1

T_RIGHT = 0
T_LEFT = 1

MAXIMUN_NUMBER_OF_ROWS = 5
MAXIMUN_NUMBER_OF_ROW_TRANSFORMATION = 2

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

# Generates the all available states depending on the current matrix (pMatrix)
def generate_states_moving_rows(pMatrix):
    result = []
    for current_row_index in range(0, MAXIMUN_NUMBER_OF_ROWS):
        for current_transformation_type in range(0, MAXIMUN_NUMBER_OF_ROW_TRANSFORMATION):
            # A copy of the initial matrix
            tmp_matrix = deepcopy(pMatrix)
            # the row to be modified
            current_row = tmp_matrix[current_row_index]
            # the transformation depending on the required type
            fun = select_transformation_type(current_transformation_type)
            # resulting row after applying the transformation
            resulting_row = fun(current_row)
            tmp_matrix[current_row_index] = resulting_row
            if not is_matrix_on_states(tmp_matrix):
                result += [tmp_matrix]
    return result

def select_transformation_type(pType):
    if pType == T_LEFT:
        return move_row_to_left
    elif pType == T_RIGHT:
        return move_row_to_right


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
            tmp_matrix = move_notch(abs(movements),direction)
            if not is_matrix_on_states(tmp_matrix):
                result += [tmp_mmatrix]
    return result

def is_matrix_on_states(pMatrix):
    global closed_states
    global open_states
    for current_matrix_index in range(0, len(closed_states)):
        current_matrix = closed_states[current_matrix_index]
        if current_matrix == pMatrix:
            return True
    for current_matrix_index in range(0, len(open_states)):
        current_matrix = open_states[current_matrix_index]
        if current_matrix == pMatrix:
            return True
    return False

# Moves the elements of the row one space to the right
def move_row_to_right(pRow):
    result = []
    result += [pRow[len(pRow) - 1]]
    result += pRow[:-1]
    return result

# Moves the elements of the row one space to the left
def move_row_to_left(pRow):
    result = []
    result += pRow[1:]
    result += [pRow[0]]
    return result



# Testing
#print(init_babylon_tower(example_mat))
#closed_states = generate_states_moving_rows(example_mat)
#print(closed_states)
#closed_states += generate_states_moving_rows(example_mat)
#print(closed_states)
#print_data()















