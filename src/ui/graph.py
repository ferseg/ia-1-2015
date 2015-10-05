from priorityQueue import *
from movement_module import *
from rotation_module import *
from fileReader import *
import constants_module as constants_m
import time

def neighbors(pMatrix):
    nodes = []
    labels = []
    group = get_notch_moves(pMatrix) + get_shifts(pMatrix)
    for element in group:
        nodes += [element[0]]
        labels += [element[1]]
    return nodes,labels
    
def get_current_goal(start,goal):
    color = 0
    for index,element in enumerate(start):
        color = goal[index]
        if element != color:
            return color,index
    return color

def heuristic(current, goal):
    result = 0
    if current[3:] == goal[3:]:
        for row_index,row in enumerate(current):
            if row_index > 2:
                break
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += constants_m.COST[5]
    
    elif current[4] == goal[4]:
        for row_index,row in enumerate(current):
            if row_index > 3:
                break
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += constants_m.COST[row_index]
    else:
        currentGoal,index = get_current_goal(current[4],goal[4])
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    col_value = abs(index-column_index)
                    row_value = 4-row_index
                    if element == currentGoal:
                        result += col_value
                    else:
                        result += col_value*2

##                    col_value = abs(index-column_index)
##                    row_value = 4-row_index
##                    if element == currentGoal:
##                        result += row_value + 2*col_value
##                    else:
##                        result += row_value + 2*col_value


    return result

def a_star_search(start, goal):
    start = init_notch(start)
    goal = init_notch(goal)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = (None,None)
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        (nodes,labels) = neighbors(current)
        for nodeIndex,next in enumerate(nodes):
            new_cost = cost_so_far[current] + heuristic(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next,goal)
                frontier.put(next, priority)
                came_from[next] = (current,labels[nodeIndex])
    path = reconstruct_path(came_from,start,goal)
    return path

def reconstruct_path(came_from, start, goal):
    txtContent = ""
    current = goal
    path = [current]
    labels = [came_from[goal][1]]
    while current != start:
        (current,current_label) = came_from[current]
        path.append(current)
        labels.append(current_label)
    labels.append(None)
    labels.reverse()
    path.reverse()
    step_index = 1
    for index,element in enumerate(path):
        txt = labels[index]
        if txt != None:
            txtContent += constants_m.STEP + str(step_index)+".\n"
            txtContent += txt + "\n"
            step_index += 1
        for row in element:
            txtContent += "("
            for entry in row:
                txtContent += constants_m.COLOR_DIC[entry]
            txtContent += ")\n"
        txtContent += "\n"
    writer = FileReader(constants_m.TXT_NAME,"w+")
    writer.write(txtContent)
    writer.closeFile()
    return path
    

