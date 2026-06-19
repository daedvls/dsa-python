# https://leetcode.com/problems/maximum-subarray/description/

'''
Max Subarray sum (Kadane's Algorithm)
'''

# nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [5,4,-1,7,8]

sum = nums[0]
currSum = 0

for i in range(len(nums)):
    currSum += nums[i]
    sum = max(sum, currSum)

    if currSum < 0:
        currSum = 0
        continue


print(sum)
