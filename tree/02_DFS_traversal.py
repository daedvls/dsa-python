'''
Two ways to traverse over any tree:
1) DFS
2) BFS


We can implement DFS in three ways:
- preorder
- inorder
- postorder

In preorder, the order of operations is: print current node val, traverse left subtree, traverse right subtree
The same operation is done recursively for each subtree

In inorder, we do: call left subtree, print val, call right subtree
In postorder, left, right, print




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

'''
1
2         3
4, 5         6
'''


def preorder(currNode):  # preorder DFS traversal
    if currNode == None:
        return

    print(currNode.data, end=" ")
    preorder(currNode.left)
    preorder(currNode.right)

def inorder(currNode):
    if currNode == None:
        return

    inorder(currNode.left)
    print(currNode.data, end=" ")
    inorder(currNode.right)

def postorder(currNode):
    if currNode == None:
        return

    postorder(currNode.left)
    postorder(currNode.right)
    print(currNode.data, end=" ")



# preorder(root)
# inorder(root)
postorder(root)

