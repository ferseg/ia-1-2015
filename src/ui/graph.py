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
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += constants_m.COST[5]
    elif current[4] == goal[4]:
    #else:
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += constants_m.COST[row_index]
    
    else:
        currentGoal,index = get_current_goal(current[4],goal[4])
        #print(goal[4])
        #print(currentGoal)
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    if element == currentGoal:
                        result += constants_m.COST_BOT[row_index]+(abs(index-column_index))
                    else:
                        result += constants_m.COST_BOT[1]+(abs(index-column_index))
    
    return result

def a_star_search(start, goal):
    start = init_notch(start)
    goal = init_notch(goal)
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    #label_to = {}
    #came_from[start] = None
    #label_to[start] = None
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
                #label_to[next] = labels[nodeIndex]
                #came_from[next] = current
    path = reconstruct_path(came_from,label_to,start,goal)
    return path

def reconstruct_path(came_from,labels_to, start, goal):
    txtContent = ""
    current = goal
    path = [current]
    labels = [labels_to[goal]]
    while current != start:
        current = came_from[current]
        current_label = labels_to[current]
        path.append(current)
        labels.append(current_label)
    labels.reverse()
    path.reverse()
    index = 1
    for index,element in enumerate(path):
        txt = labels[index]
        if txt != None:
            txtContent += constants_m.STEP + str(index)+".\n"
            txtContent += txt + "\n"
        for row in element:
            txtContent += "("
            for entry in row:
                txtContent += constants_m.COLOR_DIC[entry]
            txtContent += ")\n"
        txtContent += "\n"
        index += 1
    writer = FileReader(constants_m.TXT_NAME,"w+")
    writer.write(txtContent)
    writer.closeFile()
    return path

"""
start = time.time()
parents = a_star_search(constants_m.mat, constants_m.matZ)
end = time.time()
print(end-start)
"""
    

