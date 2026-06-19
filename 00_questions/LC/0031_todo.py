# https://leetcode.com/problems/next-permutation/description/

nums = [1, 2, 3]


def isDescending(*args):
    e = args[0]
    for ele in args:
        if ele>e:
            return False
        e = ele
    return True



def optimise(nums):
    if nums[-1] > nums[-2]:
        nums[-1], nums[-2] = nums[-2], nums[-1]
        return nums

    for i in range(len(nums)): # 0, 1, 2
        if not isDescending(nums[len(nums)-1-i:]):
            temp = nums[len(nums)-1-i]
            nums[len(nums)-1-i] = min(nums[len(nums)-i:])
            # sort [temp, (nums[len(nums)-i] excluding min(nums[len(nums)-i]))]



