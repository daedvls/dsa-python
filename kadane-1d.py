arr = [int(ele) for ele in input().split()]



def maxSubArraySum(arr):
    currSum = maxSum = arr[0]

    for num in arr[1:]:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)

    return maxSum


print(maxSubArraySum(arr))