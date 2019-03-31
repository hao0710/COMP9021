# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''


import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []

# Replace this comment with your code
copy_L=L##copy L for future usage
sort_L=sorted(copy_L)## sort the L
set_L=set(copy_L)## make L in a set
sorted_set_L=sorted(set_L)# sort the set of L
list_sorted_set_L=list(sorted_set_L)# convert the sorted set of L to a list
if len(list_sorted_set_L)%2==0:
    elements_to_keep=list_sorted_set_L[0:len(list_sorted_set_L)+1:2]
else:
    elements_to_keep=list_sorted_set_L[0:len(list_sorted_set_L):2]
##L_1 is the elements of L which exists in elements to keep
for i in range(len(copy_L)):
    if copy_L[i] in elements_to_keep:
        L_1.append(L[i])
#L_2 is L_1 after repeat number
seen=set()
for j in L_1:
    if j not in seen:
        L_2.append(j)
        seen.add(j)
##get L_3
i = 0
j = 1
while i < len(copy_L):
    L_slice = set(copy_L[i:j+1])
    if (max(L_slice) - min(L_slice)) == len(L_slice) - 1 and len(copy_L[i:j+1]) > len(L_3):
        L_3 = copy_L[i:j+1]
    j += 1
    if j >= len(copy_L):
        i += 1
        j = i + 1
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)

