#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-06

"""
https://leetcode.com/problems/product-of-array-except-self/description/

238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


http://bookshadow.com/weblog/2015/07/16/leetcode-product-array-except-self/
题目大意：
给定长度为n的整数数组nums，其中n > 1，返回输出数组output，满足output[i]等于除nums[i]之外其余各数的乘积。

不使用除法，在O(n)时间复杂度内完成此题目。

例如，给定 [1,2,3,4]，返回 [24,12,8,6]。

进一步思考：

你可以在常数空间复杂度内完成题目吗？（注意：输出数组不算在空间复杂度分析中）

解题思路：
首先想到的思路是计算全部数字的乘积，然后分别除以num数组中的每一个数（需要排除数字0）。然而，题目要求不能使用除法。

下面的解法非常巧妙，参考LeetCode Dicuss

链接地址：https://leetcode.com/discuss/46104/simple-java-solution-in-o-n-without-extra-space

由于output[i] = (x0 * x1 * ... * xi-1) * (xi+1 * .... * xn-1)

因此执行两趟循环：

第一趟正向遍历数组，计算x0 ~ xi-1的乘积

第二趟反向遍历数组，计算xi+1 ~ xn-1的乘积
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [1] * size
        left = 1
        for i in range(size):  # forword
            res[i] *= left
            left *= nums[i]
        right = 1
        for i in range(size-1, -1, -1):  # backword
            res[i] *= right
            right *= nums[i]
        return res
        
    def productExceptSelf_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        p = 1
        res = []
        # forword
        for i in range(n):
            res.append(p)
            p *= nums[i]
        # backword
        p = 1
        for i in range(n-1, -1, -1):
            res[i] *= p
            p *= nums[i]
        return res

solution = Solution()
for nums in [[1,2,3,4]]:
    print(nums, solution.productExceptSelf(nums))
        
        

"""
class Solution(object):
    def productExceptSelf(self, nums):  #  Time Limit Exceeded
        return [self.product(nums[:i] + nums[i+1:]) for i in range(len(nums))]

    def product(self, arr):
        res = 1
        for n in arr:
            res *= n
        return res
        

https://leetcode.com/problems/product-of-array-except-self/discuss/65625/Python-solution-(Accepted)-O(n)-time-O(1)-space
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output      
        
http://bookshadow.com/weblog/2015/07/16/leetcode-product-array-except-self/        
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        size = len(nums)
        output = [1] * size
        left = 1
        for x in range(size - 1):
            left *= nums[x]
            output[x + 1] *= left
        right = 1
        for x in range(size - 1, 0, -1):
            right *= nums[x]
            output[x - 1] *= right
        return output          
"""        
