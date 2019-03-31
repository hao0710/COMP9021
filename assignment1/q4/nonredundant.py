# Written by *** for COMP9021
import sys
from copy import deepcopy
try:
	file_name = input('Which data file do you want to use? ')
except FileNotFoundError:
    print('There is no such file: "{}"'.format(file_name))
    exit()
f=open(file_name)
L = []
for line in f:
    L.append(list(map(int,line.replace('R',' ').replace('(',' ').replace(',',' ').replace(')',' ').split())))
L1 = deepcopy(L)
a = {}
i = 0
while i <len(L):
    try:
        a[L[i][1]].append(L[i][0])
        i += 1
    except KeyError:
        a[L[i][1]] = []
b = deepcopy(a)
key = list(b.keys())
for i in range(len(key)):
   j = 0
   while j < len(a[key[i]]):
       try:
           a[key[i]] += b[a[key[i]][j]]
           j += 1
       except KeyError:
           j += 1
i = 0
while i < len(key):
    for x in a[key[i]]:
        if a[key[i]].count(x) > 1:
            try:
                L1.remove([x,key[i]])
            except ValueError:
                continue
    i =i+1
print('The nonredundant facts are:')
for i in range(len(L1)):
    print('R({},{})'.format(L1[i][0],L1[i][1]))
	
# Insert your code here
