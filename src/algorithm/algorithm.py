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

