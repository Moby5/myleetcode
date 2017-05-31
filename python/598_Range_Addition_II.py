#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/05/28/leetcode-range-addition-ii/

LeetCode 598. Range Addition II
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b,
which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.
You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
Input:
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4

Explanation:
Initially, M =
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M =
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M =
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.

题目大意：
给定m * n矩阵M，初始为0，然后执行一些更新操作。
数组ops表示一组更新操作，每一个操作(a, b)，表示将矩阵0 <= i < a 并且 0 <= j < b的区域值+1。
进行若干操作后，求矩阵的最大值。

注意：
m和n的范围[1, 40000]
a的范围[1, m]，b的范围[1, n]
操作不超过10000个

解题思路：
求ops[0 .. len][0]和ops[0 .. len][1]的最小值
"""


class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)


if __name__ == '__main__':
    solution = Solution()
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    print solution.maxCount(m, n, ops)
