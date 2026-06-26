# https://leetcode.com/problems/top-k-frequent-elements/

'''
Solved via hashmap
See q 0049 before this

'''


nums = [1,2,1,2,1,2,3,1,3,2]
k = 2

from collections import defaultdict
freq = defaultdict(int)

for i in range(len(nums)):
    freq[nums[i]] += 1

sorted_ = sorted(freq, key=freq.get, reverse=True)

print(sorted_[:k])
