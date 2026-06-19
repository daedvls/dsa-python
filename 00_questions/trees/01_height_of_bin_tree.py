'''
Return height of a binary tree

Method: Use recursion
Height of tree = max(height(left_sub_tree), height(right_sub_tree))
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



def treeHeight(node):
    if node == None:
        return -1

    if node.left == None and node.right == None:
        return 0

    l = 0
    r = 0

    if node.left != None:
        l = treeHeight(node.left)
    if node.right != None:
        r = treeHeight(node.right)

    return 1 + max(l, r)

print(treeHeight(root))
