class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        self.orientation = 0   # NEW attribute for the purpose of this

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


'''
Top view essentially means all the nodes that would be 'visible' when looked from above

To formalise it, we introduce "orientation" of a node wrt its parent:
Let the orientation of a node be the integer n, then the orientation of its left child would be n-1
and right child would be n+1
Also the root node would have an orientation of 0 by default

Thus essentially (TAKE A PEN AND PAPER AND DRAW AND MAKE SURE) top view is equivalent to
the nodes with consecutive orientation values

Therefore, in order to get the top view, we would need to first assign orientation values to all nodes.
And (THINK!) this can be done only via BFS (since DFS would mess with the numbering)

'''

from queue import Queue

def topView(root):
    nodes = Queue()
    visited = dict()

    nodes.put(root)

    while not nodes.empty():
        currNode = nodes.get()
        currOrientation = currNode.orientation

        if currOrientation not in visited:
            visited[currOrientation] = currNode.data

        if currNode.left != None:
            currNode.left.orientation = currOrientation - 1
            nodes.put(currNode.left)

        if currNode.right != None:
            currNode.right.orientation = currOrientation + 1
            nodes.put(currNode.right)

    for i in sorted(visited):
        print(visited[i], end=" ")


topView(root)




'''
Bottom view : TODO

'''