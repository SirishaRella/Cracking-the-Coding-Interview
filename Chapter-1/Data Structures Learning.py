#Array
print("******Array*******")
from array import *
array1 = array('i', [10,20,30,40,50])
array1.insert(2, 60)
print(array1)

#List
print("*****List*********")
array_one = [1,1,1,2,3]
array_one.insert(1, "insertion")
array_one.append("Stack insertion")
array_one.remove(2)
del array_one[-3]
print(array_one)

#Stacks are similar to arrays
#Push is similar to append
#pop is pop onlt
print("********Stack*******")
stack_one = ['a', 'b', 'c']
stack_one.append('d')
stack_one.append('e')
stack_one.pop()
print(stack_one)

#Queue
print("*********Queue********")
from collections import deque
queue = deque(['q1', 'q2', 'q3'])
print(queue)
queue.append('q4')
queue.popleft()
print(queue)

#Linked lists
class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class Slinkedlist:
    def __init__(self):
        self.headval = None
    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtEnd(self, newdata):
        if self.headval is None:
            self.headval = newdata
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = newdata


print("**************Linked List********")
list = Slinkedlist()
list.headval = Node("Mon")

e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

#Printing Linked List
list.printlist()

#Heap
print("*******Heapify*****")
import heapq
H = [21,1,45,78,3,5]
heapq.heapify(H)
print(H)






