# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid():
    result = dict()
    new_grid = rotate(grid)
    for direc in ('E', 'S', 'W', 'N'):
        if len(triangles_towards_North(new_grid)) > 0:
            result[direc] = triangles_towards_North(new_grid)
        new_grid = rotate(new_grid)
    return result

    # Replace return {} above with your code

# Possibly define other functions
def triangles_towards_North(grid_new):
    result = list()
    pair = dict()
    for i in range(len(grid_new) - 1):
        for j in range(1, len(grid_new) - 1):
            temp = 0
            if grid_new[i][j] >= 1:
                for k in range(1, 1 + min(j, len(grid_new) - 1 - i, len(grid_new) - 1 - j)):
                    if 0 not in grid_new[i + k][j - k:j + k + 1]:
                        temp += 1
                        if k < min(j, len(grid_new) - i - 1, len(grid_new) - j - 1):
                            continue
                    if temp == 0:
                        break
                    else:
                        size = temp + 1
                        if size in pair.keys():
                            pair[size] += 1
                        else:
                            pair[size] = 1
                        break
    for size, num in pair.items():
        result.append((size, num))
    result.sort(reverse=True)
    return result

def rotate(grid_to_rotate):
    grid_after_rotation = [[0 for col in range(len(grid_to_rotate))] for row in range(len(grid_to_rotate))]
    for i in range(len(grid_to_rotate)):
        for j in range(len(grid_to_rotate)):
            grid_after_rotation[i][j] = grid_to_rotate[j][len(grid_to_rotate) - 1 - i]
    return grid_after_rotation

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles = triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')
print(len(grid))