# Python Dictionaries & `sorted()` Interview Cheat Sheet

## Dictionary Patterns

### 1. Frequency Counting ⭐⭐⭐⭐⭐

One of the most common interview patterns.

Without `defaultdict`:

```python
count = {}

for x in nums:
    if x not in count:
        count[x] = 0
    count[x] += 1
```

With `defaultdict`:

```python
from collections import defaultdict

count = defaultdict(int)

for x in nums:
    count[x] += 1
```

---

### 2. Grouping ⭐⭐⭐⭐⭐

Example: Group Anagrams

```python
from collections import defaultdict

groups = defaultdict(list)

for word in words:
    key = ...
    groups[key].append(word)
```

General pattern:

```python
groups = defaultdict(list)

for item in items:
    groups[key(item)].append(item)
```

---

### 3. Membership Lookup

Instead of

```python
if x in my_list:
```

prefer

```python
if x in my_dict:
```

or

```python
if x in my_set:
```

Average Time Complexity:

| Data Structure | Membership   |
| -------------- | ------------ |
| List           | O(n)         |
| Dict           | O(1) average |
| Set            | O(1) average |

---

### 4. Iterating Through Dictionaries

Keys

```python
for k in d:
```

or

```python
for k in d.keys():
```

Values

```python
for v in d.values():
```

Both

```python
for k, v in d.items():
```

---

### 5. Safe Lookup

Instead of

```python
if key in d:
    value = d[key]
```

use

```python
value = d.get(key)
```

or

```python
value = d.get(key, default_value)
```

Example

```python
freq[word] = freq.get(word, 0) + 1
```

---

### 6. `setdefault()`

```python
groups.setdefault(key, []).append(word)
```

Equivalent to

```python
if key not in groups:
    groups[key] = []

groups[key].append(word)
```

---

## `defaultdict`

Creates a default value **when a missing key is first accessed**.

```python
from collections import defaultdict

d = defaultdict(list)

d["A"].append(1)
```

is equivalent to

```python
if "A" not in d:
    d["A"] = []

d["A"].append(1)
```

Common default factories:

```python
defaultdict(int)      # 0
defaultdict(list)     # []
defaultdict(set)      # set()
defaultdict(dict)     # {}
defaultdict(float)    # 0.0
defaultdict(str)      # ""
defaultdict(bool)     # False
defaultdict(lambda: 100)
```

---

# `sorted()` Cheat Sheet

## Syntax

```python
sorted(iterable, key=None, reverse=False)
```

Returns a **new sorted list**.

---

## Sort Numbers

```python
sorted(nums)
```

Descending

```python
sorted(nums, reverse=True)
```

---

## Sort Strings by Length

```python
sorted(words, key=len)
```

---

## Sort Tuples

```python
students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85)
]
```

Sort by marks

```python
sorted(students, key=lambda x: x[1])
```

Sort by name

```python
sorted(students, key=lambda x: x[0])
```

---

## Sort Dictionary by Keys

```python
sorted(d)
```

or

```python
sorted(d.keys())
```

---

## Sort Dictionary by Values ⭐⭐⭐⭐⭐

```python
sorted(d, key=d.get)
```

Returns keys sorted by their values.

Example

```python
marks = {
    "Alice": 90,
    "Bob": 80,
    "Charlie": 95
}

print(sorted(marks, key=marks.get))
```

Output

```python
['Bob', 'Alice', 'Charlie']
```

---

Sort key-value pairs

```python
sorted(d.items(), key=lambda x: x[1])
```

---

## Sort by Multiple Criteria ⭐⭐⭐⭐

Suppose

```python
students = [
    ("Alice", 90),
    ("Bob", 90),
    ("Charlie", 80)
]
```

Sort by

* Marks descending
* Name ascending

```python
sorted(
    students,
    key=lambda x: (-x[1], x[0])
)
```

Python compares tuples lexicographically.

---

# Lambda Patterns

Sort by first element

```python
key=lambda x: x[0]
```

Sort by second element

```python
key=lambda x: x[1]
```

Sort by third element

```python
key=lambda x: x[2]
```

Sort by string length

```python
key=len
```

Sort dictionary by values

```python
key=d.get
```

---

# Frequently Used Dictionary Methods

Check if key exists

```python
if key in d:
```

Delete

```python
del d[key]
```

Pop

```python
value = d.pop(key)
```

Keys

```python
d.keys()
```

Values

```python
d.values()
```

Items

```python
d.items()
```

Length

```python
len(d)
```

---

# Complexity

## Dictionary

| Operation               | Complexity   |
| ----------------------- | ------------ |
| Lookup                  | O(1) average |
| Insert                  | O(1) average |
| Delete                  | O(1) average |
| Membership (`key in d`) | O(1) average |
| Iterate                 | O(n)         |

---

## `sorted()`

| Operation | Complexity |
| --------- | ---------- |
| Sorting   | O(n log n) |

---

# Common Interview Patterns

| Problem Type             | Pattern                      |
| ------------------------ | ---------------------------- |
| Frequency counting       | `defaultdict(int)`           |
| Grouping                 | `defaultdict(list)`          |
| Unique elements          | `set()`                      |
| Seen before?             | `set()` or `dict`            |
| Sort dictionary by value | `sorted(d, key=d.get)`       |
| Sort tuples              | `key=lambda x: x[1]`         |
| Custom ordering          | `key=lambda ...`             |
| Top K Frequent           | `sorted()` or `heapq`        |
| Missing key handling     | `dict.get()` / `defaultdict` |
| Two Sum                  | Hash map lookup              |

---

# Interview Thinking Guide

When you see a problem, ask yourself:

### Need to count something?

→ `defaultdict(int)` or `Counter`

---

### Need to group objects?

→ `defaultdict(list)`

---

### Need fast lookup / check if seen?

→ `set()` or `dict`

---

### Need ordering based on some property?

→ `sorted(..., key=...)`

---

### Need the top/bottom elements?

→ `sorted(..., reverse=True)` or `heapq`

---

## Golden Rule

Many brute-force solutions repeatedly scan a list:

```
for each element:
    scan the list again
```

Whenever you notice this pattern, ask:

* Can I store information in a dictionary?
* Can I replace repeated scans with O(1) lookups?

This single observation is the key optimization behind a large fraction of LeetCode hash map problems.
