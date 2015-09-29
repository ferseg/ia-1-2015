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

#NOTCH_SYMBOL = 4
#UP = -1
#DOWN = 1

#notch_row = 0
#notch_column = 0
#babylon_tower = []




# Contains all the states that are open
open_states = []

# Contains all the states that are close
closed_states = []



# Testing
print(example_mat)
print(rotate_matrix_to_left(example_mat))
print(generate_states_moving_rows(example_mat, open_states, closed_states))




