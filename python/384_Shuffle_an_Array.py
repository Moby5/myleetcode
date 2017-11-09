#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/08/12/leetcode-shuffle-array/

LeetCode 384. Shuffle an Array

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();

题目大意：
对一个不包含重复元素的数组执行洗牌操作。

解题思路：
伪代码如下：

for (i = 0 to nums.length)
    swap(nums[randint(0, i)], nums[i])
"""

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = list(nums)
        self.nums = list(nums)                   

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.nums)):
            y = random.randint(0, i)
            self.nums[i], self.nums[y] = self.nums[y], self.nums[i]
        return self.nums   
        
        
# Your Solution object will be instantiated and called as such:
nums = {1,2,3};
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()
print param_1
print param_2

