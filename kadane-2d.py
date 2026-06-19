matrix = [[3, 8, 9, 1, 3],
          [-4, -1, 1, 7, -6],
          [-2, -3, 8, 1, -1]]

def kadane(arr):
    # kadane for 1d array
    currSum = maxSum = arr[0]

    for num in arr[1:]:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)

    return maxSum



def maxSubArraySumofGrid(matrix):
    if not matrix:
        return 0

    maxSum = float('-inf')

    n_cols = len(matrix[0])
    n_rows = len(matrix)

    for i in range(n_cols):
        for j in range(i, n_cols):
            arr = []
            for k in range(n_rows):
                arr.append(sum(matrix[k][i:j+1]))
            maxSum = max(maxSum, kadane(arr))
    return maxSum

print(maxSubArraySumofGrid(matrix))