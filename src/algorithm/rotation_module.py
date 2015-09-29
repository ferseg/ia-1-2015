from copy import copy, deepcopy

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

# Rotates the tower to the left.
def rotate_matrix_to_left(pMatrix):
    result = deepcopy(pMatrix)
    for current_row_index in range(0, len(pMatrix)):
        rotated_row = move_row_to_left(result[current_row_index])
        result[current_row_index] = rotated_row
    return result








    

