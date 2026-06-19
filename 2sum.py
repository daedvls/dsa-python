arr = [10, 5, 2, 7, 1]
target = 9


# using 2 pointer method
def twoSum(arr, target):
    arr_new = sorted(arr)
    left, right = 0, len(arr_new) - 1

    while left < right:
        currSum = arr_new[left] + arr_new[right]
        if currSum == target:
            return [arr_new.index(arr[left]), arr_new.index(arr[right])]
        elif currSum < target:
            left += 1
        else: right -= 1

    return [-1, -1]

print(twoSum(arr, target))
