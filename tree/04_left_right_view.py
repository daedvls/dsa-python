'''
Different views of a tree:

Left view is what we see when we look at the tree from the left side
Basically, it is the same as a list of the left-most children of the tree

For ex: our tree is:
1
2       3
4, 5    _, 6


Then the left view would be [1, 2, 4]

Right view would be: [1, 3, 6]

To do this, we would need to go level by level
Hence sth similar to a BFS (or in this case, we will use what we used to implement BFS,
ie, queue)

Here, we will maintain a queue, such as follows:
first we will add 'None' into the Q
Then we add first node into Q

Now, we traverse through the Q. First element of Q is 1. we append the children of 1 into the Q
After this we pop 1 from the Q
Then we see next element in Q -- None. Whenever we encounter None, we will pop it and again add it
to the end of the Q. (Notice that in this manner, the 'None' acts as a divider between difft levels within the Q)



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



from queue import Queue  # in-built queue

def leftView(root):
    nodes = Queue()
    nodes.put(None)
    nodes.put(root)

    while nodes.empty() == False:
        currNode = nodes.get()  # eqvt to pop

        if currNode == None:
            if nodes.empty():
                break

            currNode = nodes.get()
            print(currNode.data, end=" ")
            nodes.put(None)

        if currNode.left != None:
            nodes.put(currNode.left)
        if currNode.right != None:
            nodes.put(currNode.right)



# almost same as leftView code
def rightView(root):
    nodes = Queue()
    nodes.put(None)
    nodes.put(root)

    while nodes.empty() == False:
        currNode = nodes.get()  # eqvt to pop

        if currNode == None:
            if nodes.empty():
                break

            # currNode = nodes.get()
            # print(currNode.data, end=" ")
            nodes.put(None)  # Do nothing
            continue

        if nodes.queue[0] == None:          # eqvt to Q.peek()  (access data without popping it from Q)
            print(currNode.data, end=" ")

        if currNode.left != None:
            nodes.put(currNode.left)
        if currNode.right != None:
            nodes.put(currNode.right)



leftView(root)
print()
rightView(root)

