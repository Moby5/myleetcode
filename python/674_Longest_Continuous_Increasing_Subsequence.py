#!/usr/bin/env python
# coding=utf-8
# Date: 2018-01-24

"""
674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 

Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
"""

class Solution(object):    
    def findLengthOfLCIS_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        ans, cnt, last = 1, 1, nums[0]
        for n in nums[1:]:
            if n > last:
                cnt += 1                
            else:                
                ans = max(ans, cnt)
                cnt = 1
            last = n
        ans = max(ans, cnt)
        return ans

    def findLengthOfLCIS_v1(self, nums):
        if len(nums) == 0: return 0
        res, cnt, last = [], 1, nums[0]
        for n in nums[1:]:
            if n > last:
                cnt += 1
                last = n
            else:
                res.append(cnt)
                cnt, last = 1, n
        res.append(cnt)
        return max(res)
    
    def findLengthOfLCIS(self, nums):
        ans, cnt = 0, 1 if len(nums) > 0 else 0
        for i in range(len(nums))[1:]:
            if nums[i] > nums[i-1]:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
        ans = max(ans, cnt)
        return ans      
    
    def findLengthOfLCIS_ref(self, nums):  # https://leetcode.com/problems/longest-continuous-increasing-subsequence/solution/
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans        
    
    def findLengthOfLCIS_ref2(self, nums): # http://bookshadow.com/weblog/2017/09/10/leetcode-longest-continuous-increasing-subsequence/
        ans = cnt = 0
        last = None
        for n in nums:
            if n > last:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 1
            last = n
        return max(ans, cnt)    
        
    
solution = Solution()
print solution.findLengthOfLCIS([1,3,5,4,7]) # 3
print solution.findLengthOfLCIS([2,2,2,2,2]) # 1
print solution.findLengthOfLCIS([1]) # 1
print solution.findLengthOfLCIS([]) # 0
