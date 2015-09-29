def rotate_and_compare(pMatrix, pSolution):
	

def color_matching_percentage(pMatrix, pSolution):
	quantity = 0
	matrix_row_quantity = len(pMatrix)
	matrix_column_quantity = len(pSolution[0])
	if matrix_row_quantity == len(pSolution) and len(pMatrix[0]) == matrix_column_quantity:
		for current_row_index in range(0, matrix_row_quantity):
			for current_column_index in range(0, matrix_column_quantity):
				quantity += pMatrix[current_row_index][current_column_index] == pSolution[current_row_index][current_column_index]
	total_items = matrix_row_quantity * matrix_column_quantity
	return (quantity * 100) / total_items