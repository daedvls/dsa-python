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





# Postfix notation evaluation using stack
def evalPostFix(expressionStr):
    ops = ["+", "-", "/", "*"]
    myStack = Stack()
    for i in expressionStr:
        if i in ops:
            second = myStack.pop()
            first = myStack.pop()

            if i == '+':
                myStack.push(first + second)
            elif i == '-':
                myStack.push(first-second)
            elif i == '/':
                myStack.push(first/second)
            else:
                myStack.push(first*second)

        else:
            myStack.push(int(i))

    return myStack.pop() # final answer


# Postfix to Infix Notation conversion
def PostFixtoInfix(expressionStr):
    ops = ["+", "-", "/", "*"]
    myStack = Stack()
    for i in expressionStr:
        if i in ops:
            second = myStack.pop()
            first = myStack.pop()
            myStack.push("("+first + i + second+")")

        else:
            myStack.push(i)

    return myStack.pop() # final answer



# Infix to Postfix Notation conversion
def getPriority(operation):
    if operation == '*' or operation == '/':
        return 1
    return 0


# TODO: THIS IS WRONG, CHECK AND FIX
def InfixtoPostfix(expressionStr):
    ops = ["+", "-", "/", "*"]
    myStack = Stack()
    result = ""
    for i in expressionStr:
        if i not in ops:
            result += i
        else:
            if myStack.isEmpty():
                myStack.push(i)
            else:
                if getPriority(i):
                    myStack.push(i)
                else:
                    if getPriority(myStack.peek()):
                        while getPriority(myStack.peek()):
                            result += myStack.pop()
                    else:
                        myStack.push(i)
    while not myStack.isEmpty():
        result += myStack.pop()
    return result


# infix_str = "1*2+3"
# print(InfixtoPostfix(infix_str))
# print(PostFixtoInfix(InfixtoPostfix(infix_str)))


