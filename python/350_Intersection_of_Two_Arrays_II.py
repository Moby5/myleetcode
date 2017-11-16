#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/05/21/leetcode-intersection-of-two-arrays-ii/

350. Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

题目大意：
给定两个数组，编写函数计算它们的交集。

测试用例如题目描述。

注意：

结果中的每个元素的出现次数应与其在两个数组中同时出现的次数一样多。
结果可以采用任意顺序。
进一步思考：

如果数组已经排好序，怎样优化你的算法？
如果nums1的长度＜nums2的长度？哪一种算法更好？
如果nums2的元素存储在磁盘上，并且内存大小有限，不足以将其一次性的加载到内存中。此时应当怎样做？

"""

from collections import Counter

class Solution(object):
    def intersect_v0(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        iset = set(nums1).intersection(set(nums2))        
        ans = []
        for v in iset:
        	ans.extend([v] * min(nums1.count(v), nums2.count(v)))
        return ans

	#　if len(nums1) < len(nums2)
    def intersect_v1(self, nums1, nums2):    	
    	ans = []
    	for v in set(nums1):
    		ans.extend([v] * min(nums1.count(v), nums2.count(v)))
    	return ans

	# 解法I 排序（Sort）+双指针（Two Pointers）
    def intersect(self, nums1, nums2):  # _ref1 　效率最高
    	nums1, nums2 = sorted(nums1), sorted(nums2)
    	p1, p2, size1, size2 = 0, 0, len(nums1), len(nums2)
    	ans = []
    	while p1 < size1 and p2 < size2:
    		if nums1[p1] == nums2[p2]:
    			ans.append(nums1[p1])
    			p1 += 1
    			p2 += 1
    		elif nums1[p1] > nums2[p2]:
    			p2 += 1
    		else:
    			p1 += 1
    	return ans

    # 解法II Counter计数 该解法不需要将nums2一次性加载到内存中
    def intersect_ref2(self, nums1, nums2):
    	if len(nums1) > len(nums2):
    		nums1, nums2 = nums2, nums1
    	c1 = Counter(nums1)    	
    	ans = []
    	for v in nums2:
    		if c1[v] > 0:
    			ans.append(v)
    			c1[v] -= 1
    	return ans   	
    

solution = Solution()
print solution.intersect([1,2,2,1], [2,2])
print solution.intersect([1,2,2,1], [2,2,1,1])
        