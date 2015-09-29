from rotation_module import move_row_to_right, move_row_to_left
from copy import copy, deepcopy

MAXIMUN_NUMBER_OF_ROWS = 5
MAXIMUN_NUMBER_OF_ROW_TRANSFORMATION = 2

# Right transformation
T_RIGHT = 0
# Left transformation
T_LEFT = 1

# Generates the all available states depending on the current matrix (pMatrix)
def generate_states_moving_rows(pMatrix, pOpenStates, pClosedStates):
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
            if not is_matrix_on_states(tmp_matrix, pOpenStates, pClosedStates):
                result += [tmp_matrix]
    return result

def select_transformation_type(pType):
    if pType == T_LEFT:
        return move_row_to_left
    elif pType == T_RIGHT:
        return move_row_to_right

def is_matrix_on_states(pMatrix, pOpenStates, pClosedStates):
    states = [pOpenStates, pClosedStates]
    for current_state_index in range(0, 2):
        current_state = states[current_state_index]
        for current_matrix_index in range(0, len(current_state)):
            current_matrix = current_state[current_matrix_index]
            if current_matrix == pMatrix:
                return True
    return False