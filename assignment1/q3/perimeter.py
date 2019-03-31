from fractions import gcd
from functools import reduce
from itertools import chain


def print_pixels(pixels, range_x, range_y):
	for i in range(range_y-1, -1, -1):
		for j in range(range_x):
			print(pixels[i][j],end=' ')
		print('\n')


file_name = input('Which data file do you want to use? ')
try:
    f = open(file_name)
except FileNotFoundError:
    print('There is no such file: "{}"'.format(file_name))
    exit()
L = []

for line in f:
    L.append(list(map(int, line.split())))
if len(L) ==0:
    print('It is an empty file')
    exit()

#print(L)
L_onedimension=list(chain.from_iterable(L))
#print(L_onedimension)
L_x = []
L_y = []
for i in range(len(L_onedimension)):
	if i%2 == 0:
		L_x.append(L_onedimension[i])
	else:
		L_y.append(L_onedimension[i])

#print(L_x)
#print(L_y)


min_x = min(x for x in L_x)
max_x = max(x for x in L_x)
min_y = min(y for y in L_y)
max_y = max(y for y in L_y)

L_x_shifted = [x - min_x for x in L_x]
L_y_shifted = [y - min_y for y in L_y]

x_resolution = reduce(gcd, L_x_shifted)
y_resolution = reduce(gcd, L_y_shifted)

#print(L_x_shifted)
#print(L_y_shifted)
#print(x_resolution,y_resolution)


range_x = int((max_x - min_x)/x_resolution) + 2
range_y = int((max_y - min_y)/y_resolution) + 2

pixels = [[0 for x in range(range_x)] for y in range(range_y)] ## int pixels[range_x][range_y] = {}


#print_pixels(pixels,range_x,range_y)
#print(range_x,range_y)


for k in range(len(L)):
	left  = int((L[k][0] -min_x)/x_resolution + 1)
	right = int((L[k][2] -min_x)/x_resolution + 1) ## shift x coordinate
	down  = int((L[k][1] -min_y)/y_resolution + 1)
	up    = int((L[k][3] -min_y)/y_resolution + 1) ## shift y coordinate

	[left,right] = [min([left,right]), max([left,right])]
	[down,up]    = [min([up,down]),    max([up,down])   ]

	#print(left,right,down,up)
	for i in range(down,up):
		for j in range(left,right):
			pixels[i][j] = 1

#print_pixels(pixels,range_x,range_y)

perimeter = 0
for i in range(1,range_y-1):
	for j in range(1,range_x-1):
		if pixels[i][j] == 1:
			if pixels[i-1][j] ==0:
				perimeter += y_resolution
			if pixels[i+1][j] ==0:
				perimeter += y_resolution
			if pixels[i][j-1] ==0:
				perimeter += x_resolution
			if pixels[i][j+1] ==0:
				perimeter += x_resolution
#print_pixels(pixels, range_x, range_y)
print('The perimeter is: {}'.format(perimeter))





