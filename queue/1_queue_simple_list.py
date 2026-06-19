'''
Queue follows First In First Out (FIFO)

Shows implementation of queue using a simple list in Python

Only diff between using a simple list for a stack and a queue is that
in stack we use .pop()
in queue we use .pop(0)
'''

myQ = []
myQ.append(1)
myQ.append(2)
myQ.append(3)

print(myQ.pop(0))
print(myQ)