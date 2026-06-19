'''
https://leetcode.com/problems/set-matrix-zeroes/description/
'''


# This is the approach I came up with
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
m = len(matrix)
n = len(matrix[0])

targets = []

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            targets.append([i, j])

for target in targets:
    for i in range(m):
        matrix[i][target[1]] = 0
    for j in range(n):
        matrix[target[0]][j] = 0



# Much better:
'''
WHY IS THIS MUCH BETTER???
'''

m = len(matrix)
n = len(matrix[0])

first_row_zero = False
first_col_zero = False

# Check original first row
for ele in matrix[0]:
    if ele == 0:
        first_row_zero = True
        break

# Check original first column
for i in range(m):
    if matrix[i][0] == 0:
        first_col_zero = True
        break

# Mark rows and columns (skip first row/column)
for i in range(1, m):
    for j in range(1, n):
        if matrix[i][j] == 0:
            matrix[i][0] = 0
            matrix[0][j] = 0

# Zero rows based on markers
for i in range(1, m):
    if matrix[i][0] == 0:
        for j in range(1, n):
            matrix[i][j] = 0

# Zero columns based on markers
for j in range(1, n):
    if matrix[0][j] == 0:
        for i in range(1, m):
            matrix[i][j] = 0

# Handle first row
if first_row_zero:
    for j in range(n):
        matrix[0][j] = 0

# Handle first column
if first_col_zero:
    for i in range(m):
        matrix[i][0] = 0