# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by *** and Eric Martin for COMP9021

import time
import sys
from random import seed, randrange

from queue_adt import *

#start = time.time()
dim = 10
grid = [[0] * dim for i in range(dim)]

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def find_next_direction(current_direction):
    if current_direction == '':
        return ['S', 'E']
    elif current_direction == 'N':
        return ['E', 'N', 'W']
    elif current_direction == 'S':
        return ['W', 'S', 'E']
    elif current_direction == 'E':
        return ['S', 'E', 'N']
    else:
        return ['N', 'W', 'S']

def find_new_p(new_d, current_p):
    if new_d == 'N':
        new_p = (current_p[0] - 1, current_p[1])
    elif new_d == 'S':
        new_p = (current_p[0] + 1, current_p[1])
    elif new_d == 'E':
        new_p = (current_p[0], current_p[1] + 1)
    else:
        new_p = (current_p[0], current_p[1] - 1)
    return new_p

def leftmost_longest_path_from_top_left_corner():
    if not grid[0][0]:
        return []
    track = Queue()
    track.enqueue(([(0, 0)], ''))

    while not track.is_empty():
        (path, previous_d) = track.dequeue()
        current_p = path[-1]
        next_direction = find_next_direction(previous_d)
        for new_d in next_direction:
            new_p = find_new_p(new_d, current_p)
            if new_p[0] not in range(dim):
                continue
            if new_p[1] not in range(dim):
                continue
            if new_p in path:
                continue
            if not grid[new_p[0]][new_p[1]]:
                continue
            path_copy = list(path)
            path_copy.append(new_p)
            track.enqueue((path_copy, new_d))
    return path
    # Replace pass above with your code


provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path})')

#end = time.time()
#print ('The lasting time is','%0.2f'%(end - start),'s')          
