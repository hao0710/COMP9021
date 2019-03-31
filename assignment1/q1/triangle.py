import sys
try:
    file_name = input('Which data file do you want to use? ')
except FileNotFoundError:
    print('There is no such a file ',file_name)
    sys.exit()
f = open(file_name)
f1 = []
for line in f:
    f1.append(list(map(int,line.split())))
f1.reverse()
# Prepare a set of original lists
path =[]
num_path = [] # num_path here is for the amount of path yielding this maximum sum
leftmost_path = [] # leftmost_path here is for obtaining the leftmost path
for i in range(len(f1)):
    path.append([])
    for j in range(len(f1[i])):
        path[i].append(f1[i][j])
for i in range(len(f1)):
    leftmost_path.append([])
    for j in range(len(f1[i])):
        leftmost_path[i].append([])
for i in range(len(leftmost_path[0])):
    leftmost_path[0][i].append(f1[0][i])
for i in range(len(f1)):
    num_path.append([])
for i in range(len(num_path)):
    if i == 0:
        for j in range(len(path[i])):
            num_path[0].append(1)
    else:
        for k in range(len(path[i])):
            num_path[i].append(0)
# Start filling up the prepared list
for i in range(1,len(f1)+1):
    for j in range(len(path[i-1])-1):
        if path[i-1][j] < path[i-1][j+1]:
            path[i][j] += path[i-1][j+1]
            num_path[i][j] += num_path[i-1][j+1]
            leftmost_path[i][j].append(f1[i][j])
            for k in range(len(leftmost_path[i-1][j+1])):
                leftmost_path[i][j].append(leftmost_path[i-1][j+1][k])
        if path[i-1][j] == path[i-1][j+1]:
            path[i][j] += path[i-1][j]
            num_path[i][j] += num_path[i-1][j]+num_path[i-1][j+1]
            leftmost_path[i][j].append(f1[i][j])
            for k in range(len((leftmost_path[i-1][j]))):
                leftmost_path[i][j].append(leftmost_path[i-1][j][k])
        if path[i-1][j] > path[i-1][j+1]:
            path[i][j] += path[i-1][j]
            num_path[i][j] += num_path[i-1][j]
            leftmost_path[i][j].append(f1[i][j])
            for k in range(len(leftmost_path[i-1][j])):
                leftmost_path[i][j].append(leftmost_path[i-1][j][k])
max_sum = path[-1][-1]
path_amount = num_path[-1][-1]
leftmost_way = leftmost_path[-1][-1]
# Demonstrate the results
print('The largest sum is:',max_sum)
print('The number of paths yielding this sum is:',path_amount)
print('The leftmost path yielding this sum is:',leftmost_way)