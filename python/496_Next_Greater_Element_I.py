#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/02/05/leetcode-next-greater-element-i/
 
题目描述：
LeetCode 496. Next Greater Element I

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

题目大意：
给定两个数组（无重复）nums1 与 nums2，其中nums1的元素是nums2的子集。在nums2中寻找大于nums1中对应位置且距离最近的元素。如果对应位置不存在这样的元素，则输出-1。

注意：
nums1与nums2中的所有元素都是唯一的。
nums1与nums2的元素个数不超过1000。

解题思路：

解法I 栈（Stack）
时间复杂度O(n + m) 其中n为nums的长度，m为findNums的长度
参考LeetCode Discuss：
https://discuss.leetcode.com/topic/77916/java-10-lines-linear-time-complexity-o-n-with-explanation
栈stack维护nums的递减子集，记nums的当前元素为n，栈顶元素为top
重复弹出栈顶，直到stack为空，或者top大于n为止
将所有被弹出元素的next greater element置为n

解法II 朴素解法
时间复杂度O(n * m) 其中n为nums的长度，m为findNums的长度
"""

class Solution(object):
    def nextGreaterElement(self, findNums, nums):  # 栈（Stack）:时间复杂度O(n + m)
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        dmap = {}
        stack = []
        for n in nums:
            while stack and stack[-1] < n:
                dmap[stack.pop()] = n
            stack.append(n)
        return [dmap.get(n, -1) for n in findNums]
    
    def nextGreaterElement_v2(self, findNums, nums):  # 朴素解法:时间复杂度O(n * m)
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """    
        ans = []
        dmap = {n: idx for idx, n in enumerate(nums)}
        for idx, n in enumerate(findNums):            
            for k in nums[dmap[n]+1:]:
                if k > n:
                    ans.append(k)
                    break
            if len(ans) <= idx:
                ans.append(-1)
        return ans
                    
        
    def nextGreaterElement_v3(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """        
        ans = []
        for idx, n in enumerate(findNums):
            pos = nums.index(n)   
            right_nums = nums[pos+1:]            
            # print n, pos, right_nums            
            ngn = -1
            if right_nums:
                for k in right_nums:
                    if k > n:
                        ngn = k
                        break
            ans.append(ngn)        
        return ans

test = Solution()
print test.nextGreaterElement([4,1,2], [1,3,4,2])
print test.nextGreaterElement([2,4], [1,2,3,4])
