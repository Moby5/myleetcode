#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/07/31/leetcode-single-number/

LeetCode 136. Single Number
Given an array of integers, every element appears twice except for one. Find that single one.
Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

题目大意：
给定一个整数数组，除一个元素只出现一次外，其余各元素均出现两次。找出那个只出现一次的元素。
注意：
你的算法应该满足线性时间复杂度。可以不使用额外的空间完成此题吗？

解题思路：
对数组元素执行异或运算，最终结果即为所求。
由于异或运算的性质，两个相同数字的亦或等于0，而任意数字与0的亦或都等于它本身。另外，异或运算满足交换律。
a ^ b = (a & !b) || (!a & b)

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res

    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(operator.xor, nums)

    def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x ^ y, nums)


'''
def reduce(function, sequence, initial=None):  # real signature unknown; restored from __doc__
    """
    reduce(function, sequence[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence,
    from left to right, so as to reduce the sequence to a single value.
    For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the sequence in the calculation, and serves as a default when the
    sequence is empty.
    """
    pass
'''