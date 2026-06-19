# https://leetcode.com/problems/contains-duplicate/submissions/2032934907/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums))!=len(nums)


'''
Note: Also check hash maps
'''