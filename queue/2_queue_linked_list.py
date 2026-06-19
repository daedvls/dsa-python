'''
Implementation of Queue using linked list

Operations required:
1. Enqueue (Add element to the end)
2. Dequeue (Remove first element)
3. isEmpty (Check if empty)
4. size (current size of q)
5. front (peek the first value of the queue)
'''


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


class Q:
    def __init__(self):
        self.head = Node("dummy")
        self.tail = self.head
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size==0

    def enQ(self, value):
        self.tail.next = Node(value)
        self.size += 1
        self.tail = self.tail.next

    def deQ(self):
        if self.isEmpty:
            print("Q is empty")
            return

        removed = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1

        return removed.value

    def front(self):
        if self.isEmpty:
            print("Q is empty")
            return
        return self.head.next.val


