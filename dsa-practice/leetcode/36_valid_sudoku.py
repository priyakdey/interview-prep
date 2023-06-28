# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
# to be validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
#
#
# Example 1:
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
# Example 2:
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
# Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9 or len(board[0]) != 9:
            # this assumes that its a proper matrix, meaning all board[row] are of eq len
            return False

        def check_in_range(
            rstart: int, rend: int, cstart: int, cend: int, kind: str
        ) -> bool:
            if kind == "ROW":
                for x in range(rstart, rend):
                    seen = set()
                    for y in range(cstart, cend):
                        element = board[x][y]
                        if element != ".":
                            if int(element) < 1 or int(element) > 9:
                                return False
                            if element in seen:
                                return False
                            seen.add(element)
                return True
            elif kind == "GRID":
                seen = set()
                for x in range(rstart, rend):
                    for y in range(cstart, cend):
                        element = board[x][y]
                        if element != ".":
                            if int(element) < 1 or int(element) > 9:
                                return False
                            if element in seen:
                                return False
                            seen.add(element)
                return True
            else:
                for x in range(rstart, rend):
                    seen = set()
                    for y in range(cstart, cend):
                        element = board[y][x]
                        if element != ".":
                            if int(element) < 1 or int(element) > 9:
                                return False
                            if element in seen:
                                return False
                            seen.add(element)
                return True

        # check for rows
        if check_in_range(0, 9, 0, 9, "ROW") is False:
            return False

        # check for cols
        if check_in_range(0, 9, 0, 9, "COL") is False:
            return False

        # # check for grids
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if check_in_range(row, row + 3, col, col + 3, "GRID") is False:
                    return False

        return True
