from movements_module import generate_states_moving_rows
from rotation_module import rotate_matrix_to_left





# Contains all the states that are open
open_states = []

# Contains all the states that are close
closed_states = []



# Testing
print(example_mat)
print(rotate_matrix_to_left(example_mat))
print(generate_states_moving_rows(example_mat, open_states, closed_states))




