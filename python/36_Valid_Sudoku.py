#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-31
# File: 36_Valid_Sudoku.py

"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

"""

from collections import Counter


class Solution_v2(object):
    def isValidSudoku(self, board):  # 60 ms
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = sum(([(col, i), (j, col), (i/3, j/3, col)] for i, row in enumerate(board) for j, col in enumerate(row) if col != '.'), [])
        return len(seen) == len(set(seen))
        
    def isValidSudoku_v3(self, board):  # 52ms
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return 1 == max(Counter(x 
                                for i, row in enumerate(board) 
                                for j, col in enumerate(row) 
                                if col != '.' 
                                for x in ((col, i), (j, col), (i/3, j/3, col))
                               ).values() + [1])
        

class Solution(object):  # 48 ms
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board))

    def is_row_valid(self, board):
        return all([self.is_unit_valid(row) for row in board])

    def is_col_valid(self, board):
        return all([self.is_unit_valid(col) for col in zip(*board)])

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
        

class Solution_v0(object):  # 56 ms
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return (self.is_row_valid(board) and self.is_col_valid(board) and self.is_square_valid(board))

    def is_row_valid(self, board):
        for row in board:
            if not self.is_unit_valid(row):
                return False
        return True

    def is_col_valid(self, board):
        for col in zip(*board):
            if not self.is_unit_valid(col):
                return False
        return True

    def is_square_valid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self.is_unit_valid(square):
                    return False
        return True

    def is_unit_valid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)
        

solution = Solution()

Input = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output = True
pred = solution.isValidSudoku(Input)
assert pred == Output, pred


Input = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output = False        
pred = solution.isValidSudoku(Input)
assert pred == Output, pred

print("Pass.")

"""
https://leetcode.com/problems/valid-sudoku/discuss/15451/A-readable-Python-solution

https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions

Idea

Just go through all you see (like "7 in row 3") and check for duplicates.

Solution 1

Using Counter. One logical line, seven physical lines.

def isValidSudoku(self, board):
    return 1 == max(collections.Counter(
        x
        for i, row in enumerate(board)
        for j, c in enumerate(row)
        if c != '.'
        for x in ((c, i), (j, c), (i/3, j/3, c))
    ).values() + [1])
The + [1] is only for the empty board, where max would get an empty list and complain. It's not necessary to get it accepted here, as the empty board isn't among the test cases, but it's good to have.

Solution 2

Using len(set).

def isValidSudoku(self, board):
    seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                for i, row in enumerate(board)
                for j, c in enumerate(row)
                if c != '.'), [])
    return len(seen) == len(set(seen))
Solution 3

Using any.

def isValidSudoku(self, board):
    seen = set()
    return not any(x in seen or seen.add(x)
                   for i, row in enumerate(board)
                   for j, c in enumerate(row)
                   if c != '.'
                   for x in ((c, i), (j, c), (i/3, j/3, c)))
Solution 4

Iterating a different way.

def isValidSudoku(self, board):
    seen = sum(([(c, i), (j, c), (i/3, j/3, c)]
                for i in range(9) for j in range(9)
                for c in [board[i][j]] if c != '.'), [])
    return len(seen) == len(set(seen))
"""

