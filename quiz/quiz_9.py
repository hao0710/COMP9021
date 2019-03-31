# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree_adt import *
import math

# Possibly define some functions

leaves = []
difference=[]
def find_all_leaves(tree):
    if tree.value is not None:
        if tree.left_node!= None and tree.right_node != None:
            if tree.left_node.value == None and tree.right_node.value == None:
                leaves.append(tree.value)
    else:
        return
    find_all_leaves(tree.left_node)
    find_all_leaves(tree.right_node)
def max_diff_in_consecutive_leaves(tree):
    find_all_leaves(tree)
    #print(leaves)
    result=0  
    for i in range(0,len(leaves)-1):
        difference.append(abs(leaves[i]-leaves[i+1]))
        #print(difference)
    if len(difference)>=1:
        if result==max(difference):
            result=difference
        if result<max(difference):
            result=max(difference)
    else:
        result = 0    
    return result
        
        
provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
           
