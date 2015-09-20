# 0 = P
# 1 = Y
# 2 = O
# 3 = G
# 4 = H
# -1 = Empty
example_mat = [[-1,4,-1,-1],
			   [0, 1, 0, 2],
			   [2, 3, 2, 3],
			   [3, 0, 3, 1],
			   [1, 2, 1, 0]]

NOTCH_SYMBOL = 4
UP = -1
DOWN = 1


notch_row = 0
notch_column = 0
babylon_tower = []


def init_babylon_tower(p_initial_state):
    global babylon_tower
    babylon_tower = p_initial_state
    set_notch()

def set_notch():
    global notch_column
    global notch_row
    for row_index, row in enumerate(babylon_tower):
        for col_index, element in enumerate(row):
            if element == NOTCH_SYMBOL:
                notch_column = col_index
                notch_row = row_index

def move_notch(p_movements,p_direction):
    global notch_row
    global notch_column
    global babylon_tower
    direction_counter = p_direction
    while p_movements != 0:
        temp = babylon_tower[notch_row+p_direction][notch_column]
        babylon_tower[notch_row][notch_column] = temp
        babylon_tower[notch_row+p_direction][notch_column] = NOTCH_SYMBOL
        notch_row += p_direction
        p_movements -= 1
    
def print_Data():
    print (notch_row)
    print (notch_column)
    print (babylon_tower)


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

print(move_row_to_right(example_mat[1]))
print(move_row_to_left(example_mat[1]))

