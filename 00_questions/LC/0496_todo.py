# https://leetcode.com/problems/next-greater-element-i/

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

stack = []
stack.append(nums2[-1])
out = [-1]*len(nums2)   # [-1, -1, -1, -1]

for i in range(2, len(nums2)+1):
    if nums2[-1*i]