class node:
    def  __init__(self, value):
        self.val = value
        self.next = None


# rough implementation of a linked list
head = node(1)
head.next = node(2)
head.next.next = node(3)

# print(head.val)  # 1
# print(head.next.val)  # 2
# print(head.next.next.val)  # 3



# TODO: Check if fully correct ***
class LinkedList:
    def __init__(self):
        self.head = None

    def printLinkedList(self):
        current = self.head
        while current != None:
            print(current.val, end=" ")
            current = current.next

    def insertAtTail(self, value):
        if self.head == None:
            self.head = node(value)
            return
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node(value)

    def insertAtHead(self, value):
        newNode = node(value)
        newNode.next = self.head
        self.head = newNode

    def insert(self, value, k): # insert value at index k
        if k == 0:
            self.insertAtHead(value)  # if k is 0, we insert at head
            return

        current = self.head
        for i in range(k-1):
            if current == None:
                return # index out of bounds
            current = current.next

        # CHECK: if correct?
        if current == None:
            return # index out of bounds

        newNode = node(value)
        newNode.next = current.next
        current.next = newNode

    # TODO: delete Linked List also.

    def middle(self):
        pass


ll1 = LinkedList()
ll1.insertAtTail(1)
ll1.insertAtTail(2)
ll1.insertAtTail(3)

ll1.printLinkedList()  # 1 2 3