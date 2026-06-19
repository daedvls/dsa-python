'''
A deque (double-ended queue) allows O(1) insertion and deletion from both ends.

For DSA, BFS, sliding window, monotonic queue, etc., deque is usually preferred over queue.Queue.
since it is faster


'''

from collections import deque

dq = deque()

# initialising with values
dq = deque([10, 20, 30])


# add to right
dq.append(40)

# add to left
dq.appendleft(5)


# remove from right
x = dq.pop()

# remove from left
x = dq.popleft()

# peek front
front = dq[0]
rear = dq[-1]

print(dq == None)  # check if empty
# OR: len(dq)==0

n = len(dq) # size

dq.reverse()  # reverse

arr = list(dq)  # convert to list


for x in dq:
    print(x)


'''

# TODO: CHECK ALL THIS LATER!!!

Other common applications of queue in DSA, CP, etc:
- BFS
- Level order traversal
- Monotonic queue (sliding window maximum)
- ...

'''