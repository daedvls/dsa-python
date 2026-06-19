'''
Notes:
The base node (or the top most node from which all other nodes originate) is called the 'root'

(diagramatically, it looks like an upside down irl tree)

The topmost node would be the root node

We can traverse only from the top to the bottom, ie from the root to the connected (linked) nodes following it
So, the 'parent' node connects/links to the 'child' nodes.

The bottom-most nodes, ie the nodes that have no children are called 'leaf' nodes.

'Edge': is simply a connection between two nodes
'Sibling': two nodes that have the same parent node
'Height of a tree': Height of the tree is the LONGEST distance from the root to any of the leaves
thus, it is equal to the max no. of edges to be covered to go from the root to any of the leaves

'Depth of a node': the no. of edges travelled from the root to reach that node

(Therefore, height of tree = max(all possible depths))



## Types of trees:
1) General Tree (No conditions)
2) Binary tree (Condition: each node can have a maximum of 2 children)
3) Binary Search Tree: it is a binary tree with the added constraint that the (left child < right child)
4) AVL Tree: (TODO:CHECK)
5) Red-black trees
6) B, B+ trees


'''