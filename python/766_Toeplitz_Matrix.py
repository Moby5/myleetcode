#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-13

"""
https://leetcode.com/problems/toeplitz-matrix/description/

766. Toeplitz Matrix

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""

import collections

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        vmap = collections.defaultdict(set)
        M, N = len(matrix), len(matrix[0])
        for ridx in range(M):
            for cidx in range(N):
                vmap[cidx - ridx].add(matrix[ridx][cidx])
                if len(vmap[cidx - ridx]) > 1:
                    return False
        return True
        

solution = Solution()

matrix = [
    [1, 2, 3, 4],
    [5, 1, 2, 3],
    [9, 5, 1, 2]
]
print(solution.isToeplitzMatrix(matrix))

matrix = [
    [1, 2],
    [2, 2]
]
print(solution.isToeplitzMatrix(matrix))
        
"""
http://bookshadow.com/weblog/2018/01/21/leetcode-toeplitz-matrix/

题目大意：
Toeplitz（托普利茨）矩阵是指各条从左上到右下对角线元素均相等的矩阵。

给定M x N矩阵，判断是否为Toeplitz矩阵。

解题思路：
Map + Set

将矩阵各元素按照其所在位置行与列的差值分组。

遍历矩阵，记行为i，列为j，将元素matrix[i][j]加入i - j对应的集合。

判断各集合元素是否为1

class Solution(object):
    def isToeplitzMatrix(self, matrix):
        vmap = collections.defaultdict(set)
        M, N = len(matrix), len(matrix[0])
        for x in range(M):
            for y in range(N):
                vmap[y - x].add(matrix[x][y])
                if len(vmap[y - x]) > 1: return False
        return True
"""        
