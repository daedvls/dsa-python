'''
Diameter of a tree:
The maximum number of edges to be travelled from any one node to reach any other node in the tree

Ie, the distance between the two 'furthest apart' nodes in terms of the tree

'''



class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


# defining an example tree
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



# height of tree (from q_01)
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



# TODO: DOUBT!! CHECK HOW THIS WORKS!!
def diameter(node):
    if node == None:
        return 0

    l = diameter(node.left)
    r = diameter(node.right)

    global ans

    ans = max(ans, l+r)
    return max(l, r) + 1

ans = 0
print(diameter(root))


