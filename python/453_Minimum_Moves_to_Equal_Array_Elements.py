#!/usr/bin/env python
# coding=utf-8
"""
http://bookshadow.com/weblog/2016/11/06/leetcode-minimum-moves-to-equal-array-elements/

453. Minimum Moves to Equal Array Elements

Given a non-empty integer array of size n, 
find the minimum number of moves required to make all array elements equal, 
where a move is incrementing n - 1 elements by 1.

Example:

Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):

[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

题目大意：
给定一个长度为n的非空整数数组，计算最少需要多少次移动可以使所有元素相等，一次移动是指将n - 1个元素加1。

解题思路：
一次移动将n - 1个元素加1，等价于将剩下的1个元素减1。

因此累加数组中各元素与最小值之差即可。
"""

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_num = min(nums)
        return sum([n-min_num for n in nums])  
        # return sum(nums) - min(nums) * len(nums) 
        
test = Solution()
print test.minMoves([1,2,3])
