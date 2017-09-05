#!/usr/bin/env python
# coding=utf-8

"""
283. Move Zeroes

Given an array nums, write a function to move all 0's to the end of it 
while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

题目大意：
给定一个数组nums，编写函数将数组内所有0元素移至数组末尾，并保持非0元素相对顺序不变。

例如，给定nums = [0, 1, 0, 3, 12]，调用函数完毕后， nums应该是 [1, 3, 12, 0, 0]。

注意：

你应该“就地”完成此操作，不要复制数组。
最小化操作总数。
解题思路：
题目可以在O(n)时间复杂度内求解

算法步骤：  # moveZeroes_v2

使用两个"指针"x和y，初始令y = 0

利用x遍历数组nums：

若nums[x]非0，则交换nums[x]与nums[y]，并令y+1

算法简析：

y指针指向首个0元素可能存在的位置

遍历过程中，算法确保[y, x)范围内的元素均为0
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums.count(0): return    
        pos_last_zero = nums.index(0)
        for i in range(pos_last_zero, len(nums)):
            if nums[i]:
                nums[pos_last_zero], nums[i] = nums[i], 0
                pos_last_zero += 1                
                
    def moveZeroes_v2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        y = 0
        for x in range(len(nums)):
            if nums[x]:
                nums[x], nums[y] = nums[y], nums[x]
                y += 1

test = Solution()
nums = [0, 1, 0, 3, 12]
test.moveZeroes(nums)
print nums

nums = [2, 1]
test.moveZeroes(nums)
print nums

nums = [4,2,4,0,0,3,0,5,1,0]
test.moveZeroes(nums)
print nums
