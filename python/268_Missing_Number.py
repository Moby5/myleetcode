#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-31

"""
https://leetcode.com/problems/missing-number/description/

268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        length = len(nums)
        return int(length * (length + 1) / 2 - sum(nums)) 

        # return int((0 + len(nums)) * (len(nums) + 1) / 2 - sum(nums))    # 利用等差数列求和公式

        # return sum(range(len(nums) + 1)) - sum(nums)
        
        #num_set = set(nums)
        #for x in range(len(nums) + 1):
        #    if x not in num_set:
        #        return x
                
        # return set(range(len(nums))).difference(nums)    # Runtime Error Message: Line 22: Exception: Type <type 'set'>: Not implemented
        
        # return list(filter(lambda x: x not in set(nums), range(len(nums) + 1)))[0]  #   Time Limit Exceeded                
     
solution = Solution()
print(solution.missingNumber([3, 0, 1]))
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))


"""
https://leetcode.com/problems/missing-number/solution/

Approach #1 Sorting

    def missingNumber(self, nums):
        nums.sort()

        # Ensure that n is at the last index
        if nums[-1] != len(nums):
            return len(nums)
        # Ensure that 0 is at the first index
        elif nums[0] != 0:
            return 0

        # If we get here, then the missing number is on the range (0, n)
        for i in range(1, len(nums)):
            expected_num = nums[i-1] + 1
            if nums[i] != expected_num:
                return expected_num
            
Approach #2 HashSet
                
    def missingNumber(self, nums):
        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number                

Approach #3 Bit Manipulation

    def missingNumber(self, nums):
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
        
Approach #4 Gauss' Formula        
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum        
        
"""
