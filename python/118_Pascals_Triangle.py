#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-30

"""
https://leetcode.com/problems/pascals-triangle/description/

118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

[
     [1,0],
    [1,1,0],
   [1,2,1,0],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for ridx in range(numRows):
            line = [None] * (ridx + 1)
            line[0],  line[-1] = 1, 1
            for cidx in range(1, ridx):
                line[cidx] = ans[ridx - 1][cidx - 1] + ans[ridx - 1][cidx]
            ans.append(line)
        return ans

    def generate_v0(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        ans = [[1]]
        for ridx in range(1, numRows):
            last = ans[ridx - 1] + [0]
            ans.append([1] + [last[cidx] + last[cidx + 1] for cidx in range(ridx)])
        return ans


solution = Solution()
print(solution.generate(-1))
print(solution.generate(0))
print(solution.generate(1))
print(solution.generate(5))


"""
https://leetcode.com/problems/pascals-triangle/solution/

Dynamic Programming

class Solution:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num+1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row)-1):
                row[j] = triangle[row_num-1][j-1] + triangle[row_num-1][j]

            triangle.append(row)

        return triangle
"""
