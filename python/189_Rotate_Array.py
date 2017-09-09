#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/02/24/leetcode-rotate-array/

189. Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

题目大意：
将包含n个元素的数组向右旋转k步

例如，数组[1,2,3,4,5,6,7]包含元素个数n = 7，向右旋转k = 3步，得到[5,6,7,1,2,3,4]。

至少有3种不同的解题方法，最好使用O(1)的额外空间，“就地”完成数组旋转。

解题思路及代码：
参考LeetCode Discuss（https://oj.leetcode.com/discuss/26088/two-solution-with-extra-memory-dont-know-the-third-one-yet-idea）
"""


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if k > size: k = k % size 
        if k <= 0 or k == size: return                         
        nums[:k], nums[k:] = nums[-k:], nums[:-k]    
        
    def rotate_v1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)  
        tmp = nums[:]
        for i in range(size): nums[(i+k)%size] = tmp[i]  
            
    def rotate_v3(self, nums, k): # 全部逆序，再逆序前k个，最后逆序剩余部分, O(1)空间复杂度
        """                
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, stop):            
            for i in range((stop-start)/2):
                left, right = start + i, stop-i-1                
                nums[left], nums[right] = nums[right], nums[left]        
                
        size = len(nums)  
        if k > size: k = k % size
        reverse(nums, 0, size)
        if k > 0: reverse(nums, 0, k)        
        if k <= size-1: reverse(nums, k, size)                            

test = Solution()
num, k = [1,2,3,4,5,6,7], 3  # [5, 6, 7, 1, 2, 3, 4]
print 'num: %s, k: %d' % (num, k)
test.rotate(num, k)   
print num, '\n'

num, k = [1,2], 1
print 'num: %s, k: %d' % (num, k)  # [2, 1] 
test.rotate(num, k)
print num, '\n'

num, k = [1,2], 3
print 'num: %s, k: %d' % (num, k)  # [2, 1] 
test.rotate(num, k)
print num, '\n'

num, k = [1,2,3], 1
print 'num: %s, k: %d' % (num, k)  # [3, 1, 2]
test.rotate(num, k)
print num, '\n'

num, k = [-1], 2
print 'num: %s, k: %d' % (num, k)  # [-1] 
test.rotate(num, k)
print num, '\n'

"""
解法一 [ 时间复杂度O（n），空间复杂度O(1) ]：
以n - k为界，分别对数组的左右两边执行一次逆置；然后对整个数组执行逆置。

reverse(nums, 0, n - k - 1)
reverse(nums, n - k, n - 1)
reverse(nums, 0, n - 1)
Python代码：
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - k)
        self.reverse(nums, n - k, n)
        self.reverse(nums, 0, n)

    def reverse(self, nums, start, end):
        for x in range(start, (start + end) / 2):
            nums[x] ^= nums[start + end - x - 1]
            nums[start + end - x - 1] ^= nums[x]
            nums[x] ^= nums[start + end - x - 1]

注释：
Python中两个数交换可以用如下方法实现：

a, b = b, a
或者：

a ^= b
b ^= a
a ^= b
解法二 [ 时间复杂度O(n)，空间复杂度O(1) ]：
将数组元素依次循环向右平移k个单位

Python代码：
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        idx = 0
        distance = 0
        cur = nums[0]
        for x in range(n):
            idx = (idx + k) % n
            nums[idx], cur = cur, nums[idx]
            
            distance = (distance + k) % n
            if distance == 0:
                idx = (idx + 1) % n
                cur = nums[idx]

解法三 [ 时间复杂度O(n)，空间复杂度O(n) ]：

注：此方法需要构造新的数组，不满足提示描述中的“就地”旋转条件

class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n - k:] + nums[:n - k]
"""
