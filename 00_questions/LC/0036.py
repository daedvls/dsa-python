# https://leetcode.com/problems/valid-sudoku/description/

'''
My brute force approach
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        def checkRow(i, j):   # returns true if there is clash
            target = board[i][j]
            count = 0
            for ele in board[i]:
                if ele == target:
                    count += 1
            return count!=1

        def checkCol(i, j):
            target = board[i][j]
            count = 0
            for row in board:
                if row[j] == target:
                    count += 1
            return count!=1

        def checkGrid(i, j):
            target = board[i][j]
            # (i/3)*3, (j/3)*3
            count = 0

            for row in board[((i//3)*3):((i//3)*3)+3]:
                for ele in row[((j//3)*3):((j//3)*3)+3]:
                    if ele == target:
                        count += 1
            return count!=1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in nums:
                    if checkCol(i, j): return False
                    if checkRow(i, j): return False
                    if checkGrid(i, j): return False
        return True



'''
Much more elegant solution using a 3 hash sets (one for row, col, and grid)
Basically we maintain 3 defaultdict(set) called and each dict corresponds to row, col and grid for a cell [i, j]

Thus, we now only make on pass through the entire board, and if board[i][j] is already seen in
row[i] or col[j] or grid[(i//3, r//3)]
then return false

Note: Notice how we have put a tuple as the key for the dict grid. Remember that here, the tuple only acts as a key, and
tuple is chosen because it is hashable

'''

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
