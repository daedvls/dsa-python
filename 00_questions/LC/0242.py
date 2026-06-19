# https://leetcode.com/problems/valid-anagram/description/

s = "anagram"
t = "nagaram"

'''
Note: A brute force solution would be to sort the given strings and check for their equality.
This would be an O(nlogn + mlogm) solution.

Much better way:
Maintain two separate hashmaps for each string, check frequencies of both
Here, complexity is O(n+m) time and O(1) space, where n and m are string lengths
'''

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    countS, countT = {}, {}
    for i in range(len(s)):
        # countS[s[i]] += 1
        # This above line is what we would want. But what if we are encountering the key s[i]
        # for the first time in the string, and thus there is already no such key in our hashmap?
        # python would then throw error. To get around that we need to use the following syntax:
        countS[s[i]] = 1 + countS.get(s[i], 0) # default value of freq is 0 in case it doesn't exist yet
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c]!=countT.get(c, 0):
            return False

    return True



# NOTE: Python has an easier way (kinda cheating tho)
# an inbuilt DS called 'Counter()' that keeps track of frequencies for us
'''
def check(s, t):
    return Counter(s)==Counter(t)
'''