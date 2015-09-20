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
