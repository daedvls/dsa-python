'''
Each node can have atmost two children

This is an implementation of a simple binary tree
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.right = Node(6)

root.right.right.left = Node(7)

'''
NOTE: Here, I have created an entire tree manually. Usually in interviews and coding platforms, this is not the case.
The root node will usually be provided to us and it would already be constructed for us (~)
'''