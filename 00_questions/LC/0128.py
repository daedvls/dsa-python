# https://leetcode.com/problems/longest-consecutive-sequence/description/


'''
Very elegant solution

Hint: Note that sorting would give at best O(nlogn)

Hint: Try identifying where the sequences start. Also remember that we can use sets for O(1) lookup

'''

nums = [100,4,200,1,3,2]


numSet = set(nums)
longest = 0
for num in nums:
    if (num-1) not in numSet:
        length=1
        while (num+length) in numSet:
            length += 1
        longest = max(longest, length)

print(longest)