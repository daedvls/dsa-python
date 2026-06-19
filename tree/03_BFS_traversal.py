'''
NOTE: Aka "level-order traversal"

In order to implement BFS traversal, we use a queue
First, push the root node to our queue.
Then look at the queue: now go through all elements in the queue and for each element of the queue,
add their children to the end of the queue

Once the children have been pushed to the end of the queue, we can print the value of that node, and then pop it off from
the queue


'''

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

'''
1
2         3
4, 5         6
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(7)



def levelorder(node):
    Q = []
    Q.append(node)

    while len(Q) != 0:
        currNode = Q.pop(0)
        if currNode.left != None:
            Q.append(currNode.left)
        if currNode.right != None:
            Q.append(currNode.right)
        print(currNode.data, end=" ")


levelorder(root)
