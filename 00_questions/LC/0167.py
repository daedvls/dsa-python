# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

numbers = [2,7,11,15]
target = 9

'''
My soln: Almost works. Better however, is to just use two pointer method!

numSet = set(numbers)
for i in range(len(numbers)):
    if (target - numbers[i]) in numSet:
        for j in range(len(numbers)):
            if numbers[j]==(target - numbers[i]):
                print(min(j+1, i+1), max(j+1, i+1))
                break

            '''



# Two pointer method
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []