'''
Using the in-built queue data structure in python

NOTE: Generally for competitive programming, leetcode etc, queue.Queue is NOT USED

Reason: it is 'thread-safe'(?) and slightly slower
Better method is to use collections.deque

See 4_deque_in-built.py

'''

from queue import Queue

q = Queue()

# q = Queue(maxsize=5)   # q with a max size limit


# inserting elements
q.put(10)
q.put(20)
q.put(30)
# front -> 10, 20, 30 <- rear


# remove and returns the front element (similar to pop())
x = q.get()
print(x)
# now q = [20, 30]

print(q.empty())   # check if empty

print(q.qsize())   # returns size of q


# peek front element (peek() fn)
front = q.queue[0]
reat = q.queue[-1]

# print entire q in list form
print(list(q.queue))

# traverse through q wihtout destroying it
for x in q.queue:
    print(x)
