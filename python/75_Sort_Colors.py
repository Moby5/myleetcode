#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-28

"""
https://leetcode.com/problems/sort-colors/description/

75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

class Solution(object):
    def sortColors(self, nums):  # 20 ms
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero, second = 0, len(nums) - 1
        i = 0
        while i <= second:
            while nums[i] == 2 and i < second:
                nums[i], nums[second] = nums[second], nums[i]
                second -= 1
            while nums[i] == 0 and i > zero:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
            i += 1


solution = Solution()

nums = [2,0,2,1,1,0]
expected_output = [0,0,1,1,2,2]
solution.sortColors(nums)
print(nums)

if nums == expected_output:
    print("测试通过")
else:
    print("测试不通过")
        
"""
https://leetcode.com/problems/sort-colors/discuss/26472/Share-my-at-most-two-pass-constant-space-10-line-solution

The idea is to sweep all 0s to the left and all 2s to the right, then all 1s are left in the middle.

It is hard to define what is a "one-pass" solution but this algorithm is bounded by O(2n), meaning that at most each element will be seen and operated twice (in the case of all 0s). You may be able to write an algorithm which goes through the list only once, but each step requires multiple operations, leading the total operations larger than O(2n).

    class Solution {
    public:
        void sortColors(int A[], int n) {
            int second=n-1, zero=0;
            for (int i=0; i<=second; i++) {
                while (A[i]==2 && i<second) swap(A[i], A[second--]);
                while (A[i]==0 && i>zero) swap(A[i], A[zero++]);
            }
        }
    };
"""        
