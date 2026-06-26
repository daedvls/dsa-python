# first: brute force approach (?), compare every element with every other

'''
def isAnagram(str1, str2):
    a = set(list(str1))
    b = set(list(str2))
    return a==b


strs = [""]


visited = [False]*len(strs)
ans = []

for i in range(len(strs)):
    if visited[i]:
        continue

    group = [strs[i]]  # group of strs, will be later added to ans
    visited[i] = True

    for j in range(i+1, len(strs)):
        if visited[j]:
            continue

        if isAnagram(strs[i], strs[j]):
            group.append(strs[j])
            visited[j] = True

    ans.append(group)


print(ans)

'''

# much better approach (Using a hashmap, ie, dictionary)

strs = ["eat","tea","tan","ate","nat","bat"]

from collections import defaultdict
groups = defaultdict(list)

'''
Note: If we were to use just a normal dict (ie, groups = {})
The issue here is that now when we want to do sth like:
groups['aet'].append(sth)

Here, python dict doesn't have anything in it. So it returns an error when it can't find groups['aet']
So instead, we use defaultdict -> This basically assigns a default value to a key if it can't find a key when we try to
access it.

We can also do defaultdict(some_function)
Such that whenever python encounters a key that is called when it does not exist yet, then it calls that `some_function`

'''

for i in range(len(strs)):
    word = strs[i]
    key = "".join(sorted(word))      # returns str w alphabetically sorted letters
    # Note, sorted(word) returns a list by default. So we need to convert it back into a str
    # Since lists are unhashable (Can't use lists directly as dict keys)

    groups[key].append(word)

print(list(groups.values()))