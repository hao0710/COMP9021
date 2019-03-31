# Written by **** for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self):
        smallest_index, smallest = self.findSmallest()
        new_linkedlist = LinkedList()
        temp_index = smallest_index
        new_linkedlist.append(smallest)
        while len(new_linkedlist) <= len(self):
            temp_index -= 1
            new_linkedlist.append(self.value_at(temp_index))
            if len(new_linkedlist) == len(self):
                self.copyList(new_linkedlist)
                return
            if temp_index + 3 >= len(self):
                temp_index = (temp_index + 3) - len(self)
            else:
                temp_index += 3
            new_linkedlist.append(self.value_at(temp_index))
        self.copyList(new_linkedlist)
        return
        # Replace pass above with your code

    def copyList(self, L):
        h1 = self.head
        h2 = L.head
        while h1 and h2:
            h1.value = h2.value
            h1 = h1.next_node
            h2 = h2.next_node

    def findSmallest(self):
        smallest_index, smallest = 0, self.head.value
        temp = self.head.next_node
        temp_index = 1
        while temp is not None:
            if temp.value < smallest:
                smallest = temp.value
                smallest_index = temp_index
            temp_index += 1
            temp = temp.next_node
        return smallest_index, smallest
