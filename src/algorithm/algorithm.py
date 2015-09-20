from copy import copy, deepcopy

P = 0
Y = 1
O = 2
G = 3
H = 4
E = -1

MAXIMUN_NUMBER_OF_ROWS = 5

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

def generate_states_moving_rows(matrix):
    result = []
    for current_row_index in range(0, MAXIMUN_NUMBER_OF_ROWS):
        # The resulting matrix when the transformation "right" is applied
        tmp_matrix_right = deepcopy(matrix)
        # The resulting matrix when the transformation "right" is applied
        tmp_matrix_left = deepcopy(matrix)

        # >> Begin right transformation <<
        current_row = matrix[current_row_index]
        # resulting_row for the right transformation of the current row
        resulting_row = move_row_to_right(current_row)
        tmp_matrix_right[current_row_index] = resulting_row
        result += [tmp_matrix_right]
        # >> End right transformation <<

        # >> Begin left transformation <<
        # resulting_row for the right transformation of the current row
        resulting_row = move_row_to_left(current_row)
        tmp_matrix_left[current_row_index] = resulting_row
        result += [tmp_matrix_left]
        # >> End left transformation <<
    return result


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

def move_notch(pMovements,pDirection):
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
print(move_row_to_right(example_mat[1]))
print(move_row_to_left(example_mat[1]))
print(init_babylon_tower(example_mat))
print(generate_states_moving_rows(example_mat))
print_data()
#print(move_row_to_right(example_mat[1]))
#print(move_row_to_left(example_mat[1]))





