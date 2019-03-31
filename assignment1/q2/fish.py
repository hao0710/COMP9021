# Written by *** for COMP9021
# Insert your code here
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
for line in f:
    L.append(list(map(int, line.split())))
if len(L) ==0:
    print('It is an empty file')
    exit()
dist = [row[0] for row in L]
fish = [row[1] for row in L]

#min_avg = int((sum(fish) - (max(dist)-min(dist)))/len(L))
max_avg = int(sum(fish)/len(L))
for cur_avg in range(max_avg,0,-1):
    fish_carried = 0
    for i in range(len(L)-1):
        fish_now = fish[i]+fish_carried
        fish_carrying = fish_now - cur_avg
        if fish_carrying < 0:
            fish_carried = fish_carrying - dist[i+1] + dist[i]
        elif fish_carrying < dist[i+1] - dist[i]:
            fish_carried = 0
        else:
            fish_carried = fish_carrying - dist[i+1] + dist[i]
    if fish_carried + fish[len(L)-1] >= cur_avg:
        avg = cur_avg
        break
print('The maximum quantity of fish that each town can have is {}.'.format(avg))

