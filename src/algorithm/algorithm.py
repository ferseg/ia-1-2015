import transformation_module as transformation_m
import rotation_module as rotation_m
import constants_module as constants_m
import comparison_module as comparison_m

example_mat = [[constants_m.E, constants_m.H, constants_m.E, constants_m.E],
			   [constants_m.P, constants_m.Y, constants_m.P, constants_m.O],
			   [constants_m.O, constants_m.G, constants_m.O, constants_m.G],
			   [constants_m.G, constants_m.P, constants_m.G, constants_m.Y],
			   [constants_m.Y, constants_m.O, constants_m.Y, constants_m.P]]

example_mat2 = [[constants_m.E, constants_m.H, constants_m.E, constants_m.E],
               [constants_m.P, constants_m.Y, constants_m.P, constants_m.O],
               [constants_m.O, constants_m.G, constants_m.O, constants_m.G],
               [constants_m.G, constants_m.P, constants_m.G, constants_m.P],
               [constants_m.Y, constants_m.O, constants_m.Y, constants_m.Y]]



# Contains all the states that are open
open_states = []

# Contains all the states that are close
closed_states = []


# Testing
print(example_mat)
print(rotation_m.rotate_matrix_to_left(example_mat))
print(transformation_m.generate_states_moving_rows(example_mat, open_states, closed_states))
print(comparison_m.color_matching_percentage(example_mat[1:], example_mat2[1:]))





