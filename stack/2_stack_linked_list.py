'''
Implementation of a stack using a linked list in Python.
'''

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = Node("head") # dummy node to simplify edge cases
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def push(self, value):
        temp = Node(value)
        temp.next = self.head.next
        self.head.next = temp
        self.size += 1

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        temp = self.head.next
        self.head.next = temp.next
        self.size -= 1
        return temp.val

    def peek(self):
        ''' returns the top element of the stack without removing it '''
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.head.next.val


myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)

print(myStack.getSize())  # 3
print(myStack.peek())  # 3




