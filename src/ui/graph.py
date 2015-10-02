from priorityQueue import *
from movement_module import *
from rotation_module import *
<<<<<<< HEAD
from fileReader import *
=======
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
import constants_module as constants_m
import time

def neighbors(pMatrix):
<<<<<<< HEAD
    nodes = []
    labels = []
    group = get_notch_moves(pMatrix) + get_shifts(pMatrix)
    for element in group:
        nodes += [element[0]]
        labels += [element[1]]
    return nodes,labels
=======
    result = get_notch_moves(pMatrix)
    result += get_shifts(pMatrix)
    return result
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3

def heuristic(current, goal):
    result = 0
    if current[3:] == goal[3:]:
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
<<<<<<< HEAD
                    result += constants_m.COST[5]
=======
                    result += 1
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    else:
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += constants_m.COST[row_index]
    return result

def a_star_search(start, goal):
<<<<<<< HEAD
    #start = init_notch(pStart)
    #goal = init_notch(pGoal)
=======
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
<<<<<<< HEAD
    label_to = {}
    came_from[start] = None
    label_to[start] = None
=======
    came_from[start] = None
>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
<<<<<<< HEAD
        (nodes,labels) = neighbors(current)
        for nodeIndex,next in enumerate(nodes):
            new_cost = cost_so_far[current] + heuristic(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                label_to[next] = labels[nodeIndex]
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
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
    for index,element in enumerate(path):
        txt = labels[index]
        if txt != None:
            txtContent += txt + "\n"
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

"""
start = time.time()
parents = a_star_search(constants_m.mat, constants_m.matZ)
end = time.time()
print(end-start)
"""
=======
        for next in neighbors(current):
            new_cost = cost_so_far[current] + heuristic(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path;



>>>>>>> b57a739fd0d5c763e10e167fefa954130a9321c3
    

