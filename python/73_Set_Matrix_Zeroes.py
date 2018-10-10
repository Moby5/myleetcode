#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-10

"""
https://leetcode.com/problems/set-matrix-zeroes/description/

73. Set Matrix Zeroes

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

class Solution(object):
    def setZeroes(self, matrix):  # 120 ms
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(h):
            for j in range(w):
                if i in rows or j in cols:
                    matrix[i][j] = 0
                    
    def setZeroes_v0(self, matrix):  # 136 ms
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        h, w = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        zeros_row = [0] * w
        for i in rows:            
            matrix[i] = zeros_row
        for j in cols:
            for i in range(h):
                matrix[i][j] = 0

solution = Solution()

matrix = [
      [1,1,1],
      [1,0,1],
      [1,1,1]
]
expected_output = [
      [1,0,1],
      [0,0,0],
      [1,0,1]
]
solution.setZeroes(matrix)
assert matrix == expected_output, matrix

matrix = [
      [0,1,2,0],
      [3,4,5,2],
      [1,3,1,5]
] 
expected_output = [
      [0,0,0,0],
      [0,4,5,0],
      [0,3,1,0]
]
solution.setZeroes(matrix)
assert matrix == expected_output, matrix

print("ok")
        
"""
https://leetcode.com/problems/set-matrix-zeroes/solution/
"""        
        
