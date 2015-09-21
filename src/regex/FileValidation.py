#colors dictionary to control the length of each color
global TOWER_COLORS;
TOWER_COLORS = {"green" : 0, "blue" : 0, "orange" : 0, "red" : 0, "hole" : 0};

#store the order of the rows like the user entered them
global ROWS;
ROWS = [];

#final babylon tower for posterior use
global BABYLON_TOWER;
BABYLON_TOWER = [];

#initial function of validation
#param: babylon_tower -> comes of the input file with the regex applied
#returns the final babylon tower
#returns [] if something was wrong
def validate_tower(babylon_tower):
    BABYLON_TOWER = validate_number_rows(babylon_tower);
    for row in BABYLON_TOWER:
        print(row)
    return BABYLON_TOWER

#verifies if the user entry has only 4 rows with its corresponding index
#ex F1,F2,F3,F4
#wrong F1,F1,F2,F3
def validate_number_rows(babylon_tower):
    for row in babylon_tower:
        ROWS.append(int(row[0][1:]))
##    print(ROWS)
    #counts of the number of all the rows
    ones = ROWS.count(1);
    twos = ROWS.count(2);
    threes = ROWS.count(3);
    fours = ROWS.count(4);
    #verify if the indexes are just once
    if( ones == 1 and twos == 1 and threes == 1 and fours == 1):
        print("La cantidad de filas es correcta")
        #proceed with the balls validation
        validate_balls(babylon_tower)
        #validation of the fifth column
##        validate_extra_spot(babylon_tower)
        #validation of the length of each color
        if(TOWER_COLORS["blue"] == 4 and TOWER_COLORS["orange"] == 4 and TOWER_COLORS["red"] == 4 and TOWER_COLORS["green"] == 4 and TOWER_COLORS["hole"] == 1):
            #returns the matrix to work internally
            return create_matrix(ROWS,babylon_tower);
        else:
            print("La cantidad de bolitas por color no es correcta o la muesca está mal colocada")
            #if the colors of the tower or the hole are wrong
            return []
    else:
        print("La numeración de las filas no es correcta")

        
def validate_balls(babylon_tower):
    inputs = []
    #get all the user row's inputs and append them into inputs
    for row in babylon_tower:
        new_row = row[2]+","+row[5];
        inputs.append(new_row.split(","));
##    print(inputs);
    #use the TOWER_COLORS to increase its values
    for row in inputs:
        increase_balls_length(row)

#increase by 1 if the char is equal to a cap letter
#param: ex. ['B','O','R','G','H']
def increase_balls_length(babylon_tower_row):
    for elem in babylon_tower_row:
        if(elem == 'B'):
            TOWER_COLORS["blue"]+=1;
        elif(elem == 'O'):
            TOWER_COLORS["orange"]+=1;
        elif(elem == 'G'):
            TOWER_COLORS["green"]+=1;
        elif(elem == 'R'):
            TOWER_COLORS["red"]+=1;
        elif(elem == "H"):
            TOWER_COLORS["hole"]+=1;

#COLORS-VALUES
##blue = 0
##orange = 1
##green = 2
##red = 3
##hole = 4
##empty = -1
def cast_values(colors_row):
    new_colors_row = []
    for elem in colors_row:
        if(elem == 'B'):
            new_colors_row.append(0)
        elif(elem == 'O'):
            new_colors_row.append(1)
        elif(elem == 'G'):
            new_colors_row.append(2)
        elif(elem == 'R'):
            new_colors_row.append(3)
        elif(elem == 'H'):
            new_colors_row.append(4)
        else:
            new_colors_row.append(-1)
    return new_colors_row;

#params:
#rows_numbers -> the index of each row in the user's entered order
#babylon_tower entered by the user
def create_matrix(rows_numbers,babylon_tower):
    #use a dictionary to order the rows
    unordered_babylon_tower = {}
    count = 0
    while count < len(babylon_tower):
        #row including holes
        complete_row = babylon_tower[count][2] + "," + babylon_tower[count][5]
        #cast the values of the letters with numbers
        numbers_row = cast_values(complete_row.split(","));
        #add the key:value to the dictionary
        unordered_babylon_tower[rows_numbers[count]] = numbers_row;
        count+=1;
    #get all the values from the dictionary ordered by row and
    #insert them into the matrix
    matrix = list(unordered_babylon_tower.values());
    return matrix;
