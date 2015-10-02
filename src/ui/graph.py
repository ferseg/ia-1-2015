from priorityQueue import *
from movement_module import *
from rotation_module import *
import constants_module as constants_m
import time

def neighbors(pMatrix):
    result = get_notch_moves(pMatrix)
    result += get_shifts(pMatrix)
    return result

def heuristic(current, goal):
    result = 0
    if current[3:] == goal[3:]:
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += 1
    else:
        for row_index,row in enumerate(current):
            for column_index,element in enumerate(row):
                if element != goal[row_index][column_index]:
                    result += constants_m.COST[row_index]
    return result

def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
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



    

