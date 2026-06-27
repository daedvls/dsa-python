# Some useful Python in-built features

## Fast Input

### Single integer
```python
n = int(input())
```

### Multiple integers
```python
a, b = map(int, input().split())
```

### List of integers
```python
arr = list(map(int, input().split()))
```

### List of strings
```python
arr = input().split()
```

### Read N integers (one per line)
```python
arr = [int(input()) for _ in range(n)]
```

### Read N arrays
```python
matrix = [list(map(int, input().split())) for _ in range(n)]
```

---

# Output

### Print without newline
```python
print(x, end="")
```

### Print with spaces
```python
print(*arr)
```

### Print line by line
```python
for x in arr:
    print(x)
```

---

# Loops

### Repeat N times
```python
for _ in range(n):
    ...
```

### Loop with index
```python
for i in range(len(arr)):
    ...
```

### Loop over values
```python
for x in arr:
    ...
```

### Loop over index and value
```python
for i, x in enumerate(arr):
    ...
```

### Reverse loop
```python
for i in range(n-1, -1, -1):
    ...
```

---

# Useful List Operations

### Create list
```python
arr = [0] * n
```

### 2D list
```python
grid = [[0]*m for _ in range(n)]
```

Never do:
```python
grid = [[0]*m]*n
```

---

### Append
```python
arr.append(x)
```

### Extend
```python
arr.extend(other)
```

### Insert
```python
arr.insert(i, x)
```

### Remove first occurrence
```python
arr.remove(x)
```

### Remove by index
```python
arr.pop(i)
```

### Last element
```python
arr[-1]
```

### Reverse
```python
arr.reverse()
```

### Sorted copy
```python
new = sorted(arr)
```

### Sort in-place
```python
arr.sort()
```

Descending

```python
arr.sort(reverse=True)
```

Sort by key

```python
arr.sort(key=lambda x: x[1])
```

---

# Strings

Length

```python
len(s)
```

Reverse

```python
s[::-1]
```

Join

```python
" ".join(words)
```

Split

```python
input().split()
```

Lowercase

```python
s.lower()
```

Uppercase

```python
s.upper()
```

Count

```python
s.count('a')
```

Replace

```python
s.replace("old", "new")
```

---

# Sets

Create

```python
st = set()
```

From list

```python
st = set(arr)
```

Add

```python
st.add(x)
```

Remove

```python
st.remove(x)
```

Discard (no error)

```python
st.discard(x)
```

Membership

```python
if x in st:
```

Intersection

```python
a & b
```

Union

```python
a | b
```

Difference

```python
a - b
```

---

# Dictionaries

Create

```python
mp = {}
```

Default value

```python
from collections import defaultdict

mp = defaultdict(int)
```

Increment frequency

```python
mp[x] += 1
```

Safe lookup

```python
mp.get(x, 0)
```

Loop

```python
for k, v in mp.items():
    ...
```

---

# Counter

```python
from collections import Counter

cnt = Counter(arr)
```

Most common

```python
cnt.most_common(3)
```

Frequency

```python
cnt[x]
```

---

# Deque

```python
from collections import deque

dq = deque()
```

Append

```python
dq.append(x)
```

Append left

```python
dq.appendleft(x)
```

Pop

```python
dq.pop()
```

Pop left

```python
dq.popleft()
```

---

# Heap (Priority Queue)

```python
import heapq

heap = []
```

Push

```python
heapq.heappush(heap, x)
```

Pop minimum

```python
heapq.heappop(heap)
```

Peek

```python
heap[0]
```

Max heap

```python
heapq.heappush(heap, -x)
```

Pop

```python
-largest = -heapq.heappop(heap)
```

---

# Bisect

```python
import bisect
```

Lower bound

```python
bisect.bisect_left(arr, x)
```

Upper bound

```python
bisect.bisect_right(arr, x)
```

Insert

```python
bisect.insort(arr, x)
```

---

# Math

```python
import math
```

GCD

```python
math.gcd(a, b)
```

LCM

```python
math.lcm(a, b)
```

Square root

```python
math.sqrt(x)
```

Ceil

```python
math.ceil(x)
```

Floor

```python
math.floor(x)
```

Factorial

```python
math.factorial(n)
```

Power

```python
pow(a, b)
```

Modulo power

```python
pow(a, b, mod)
```

Infinity

```python
INF = float('inf')
```

---

# Useful Built-ins

Maximum

```python
max(arr)
```

Minimum

```python
min(arr)
```

Sum

```python
sum(arr)
```

Length

```python
len(arr)
```

Absolute

```python
abs(x)
```

Zip

```python
for a, b in zip(A, B):
```

Enumerate

```python
for i, x in enumerate(arr):
```

Any

```python
any(arr)
```

All

```python
all(arr)
```

---

# List Comprehensions

Squares

```python
[x*x for x in arr]
```

Filter

```python
[x for x in arr if x % 2 == 0]
```

Flatten

```python
[x for row in matrix for x in row]
```

---

# Lambda

Sort by second element

```python
arr.sort(key=lambda x: x[1])
```

Descending

```python
arr.sort(key=lambda x: -x[1])
```

---

# Binary Search Template

```python
l, r = 0, n-1

while l <= r:
    mid = (l + r) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        l = mid + 1
    else:
        r = mid - 1

return -1
```

---

# Prefix Sum

```python
prefix = [0]

for x in arr:
    prefix.append(prefix[-1] + x)
```

Range sum

```python
prefix[r+1] - prefix[l]
```

---

# Matrix Directions

```python
dirs = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1)
]
```

8-direction

```python
dirs = [
(-1,-1),(-1,0),(-1,1),
(0,-1),         (0,1),
(1,-1),(1,0),(1,1)
]
```

---

# Swap

```python
a, b = b, a
```

---

# Reverse List

```python
arr[::-1]
```

---

# Unique Elements

```python
arr = list(set(arr))
```

Keep sorted

```python
arr = sorted(set(arr))
```

---

# Transpose Matrix

```python
list(zip(*matrix))
```

---

# Character ↔ ASCII

```python
ord('a')
```

```python
chr(97)
```

---

# Binary

To binary

```python
bin(x)
```

Without prefix

```python
bin(x)[2:]
```

---

# Common Bit Operations

Check ith bit

```python
x & (1 << i)
```

Set bit

```python
x |= (1 << i)
```

Clear bit

```python
x &= ~(1 << i)
```

Toggle bit

```python
x ^= (1 << i)
```

---

# Recursion Limit

```python
import sys
sys.setrecursionlimit(10**6)
```

---

# Fast IO (CP)

```python
import sys

input = sys.stdin.readline
```

---

# Interview Data Structures

```python
from collections import deque
from collections import Counter
from collections import defaultdict

import heapq
import bisect
import math
```

---

# Handy Idioms

### Frequency map
```python
freq = {}
for x in arr:
    freq[x] = freq.get(x, 0) + 1
```

### Find max with index
```python
idx, val = max(enumerate(arr), key=lambda x: x[1])
```

### Sort dictionary by value
```python
sorted(mp.items(), key=lambda x: x[1])
```

### Reverse dictionary iteration
```python
for k in reversed(list(mp)):
    ...
```

### Check palindrome
```python
s == s[::-1]
```

### Remove duplicates while preserving order
```python
arr = list(dict.fromkeys(arr))
```

### Count truthy values
```python
sum(bool(x) for x in arr)
```

### Merge dictionaries
```python
d = d1 | d2
```