#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-08

"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""

class Solution(object):
    def lengthOfLIS(self, nums):  # Dynamic Programming with Binary Search   40 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        length = 0
        for n in nums:
            l, r = 0, length
            while l != r:
                m = (l + r) / 2
                if dp[m] < n:
                    l = m + 1
                else:
                    r = m
            dp[l] = n
            length = max(l + 1, length)
        return length
        
    def lengthOfLIS_v1(self, nums):  # Dynamic Programming  1276 ms
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dp = [0] * len(nums)
        dp[0] = 1
        maxans = 1
        for i in range(1, len(dp)):
            maxval = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    maxval = max(maxval, dp[j])
            dp[i] = maxval + 1
            maxans = max(maxans, dp[i])
        return maxans

        
    def lengthOfLIS_v0(self, nums):  #   Time Limit Exceeded
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, float('-inf'), 0)

    def helper(self, nums, prev, curpos):
        if curpos == len(nums):
            return 0
        taken = 0
        if nums[curpos] > prev:
            taken = 1 + self.helper(nums, nums[curpos], curpos + 1)
        nottaken = self.helper(nums, prev, curpos + 1)
        return max(taken, nottaken)


solution = Solution()
nums = [10,9,2,5,3,7,101,18]
expected_output = 4
output = solution.lengthOfLIS(nums)
assert output == expected_output, output
print("ok")

"""
https://leetcode.com/problems/longest-increasing-subsequence/solution/

Approach #1 Brute Force [Time Limit Exceeded]
Algorithm

The simplest approach is to try to find all increasing subsequences and then returning the maximum length of longest increasing subsequence. In order to do this, we make use of a recursive function lengthofLISlengthofLIS which returns the length of the LIS possible from the current element(corresponding to curposcurpos) onwards(including the current element). Inside each function call, we consider two cases:

The current element is larger than the previous element included in the LIS. In this case, we can include the current element in the LIS. Thus, we find out the length of the LIS obtained by including it. Further, we also find out the length of LIS possible by not including the current element in the LIS. The value returned by the current function call is, thus, the maximum out of the two lengths.

The current element is smaller than the previous element included in the LIS. In this case, we can't include the current element in the LIS. Thus, we find out only the length of the LIS possible by not including the current element in the LIS, which is returned by the current function call.


Complexity Analysis

Time complexity : O(2^n)O(2
n
). Size of recursion tree will be 2^n2
n
.

Space complexity : O(n^2)O(n
2
). memomemo array of size n * nn∗n is used.

Approach #2 Recursion with memorization [Memory Limit Exceeded]
Algorithm

In the previous approach, many recursive calls had to made again and again with the same parameters. This redundancy can be eliminated by storing the results obtained for a particular call in a 2-d memorization array memomemo. memo[i][j]memo[i][j] represents the length of the LIS possible using nums[i]nums[i] as the previous element considered to be included/not included in the LIS, with nums[j]nums[j] as the current element considered to be included/not included in the LIS. Here, numsnums represents the given array.


Complexity Analysis

Time complexity : O(n^2)O(n
2
). Size of recursion tree can go upto n^2n
2
.

Space complexity : O(n^2)O(n
2
). memomemo array of n*nn∗n is used.

Approach #3 Dynamic Programming [Accepted]
Algorithm

This method relies on the fact that the longest increasing subsequence possible upto the i^{th}i
th
 index in a given array is independent of the elements coming later on in the array. Thus, if we know the length of the LIS upto i^{th}i
th
index, we can figure out the length of the LIS possible by including the (i+1)^{th}(i+1)
th
 element based on the elements with indices jj such that 0 \leq j \leq (i + 1)0≤j≤(i+1).

We make use of a dpdp array to store the required data. dp[i]dp[i] represents the length of the longest increasing subsequence possible considering the array elements upto the i^{th}i
th
 index only ,by necessarily including the i^{th}i
th
element. In order to find out dp[i]dp[i], we need to try to append the current element(nums[i]nums[i]) in every possible increasing subsequences upto the (i-1)^{th}(i−1)
th
 index(including the (i-1)^{th}(i−1)
th
 index), such that the new sequence formed by adding the current element is also an increasing subsequence. Thus, we can easily determine dp[i]dp[i] using:

dp[i] = \text{max}(dp[j]) + 1, \forall 0\leq j &lt; idp[i]=max(dp[j])+1,∀0≤j<i

At the end, the maximum out of all the dp[i]dp[i]'s to determine the final result.

LIS_{length}= \text{max}(dp[i]), \forall 0\leq i &lt; nLIS
length
​
=max(dp[i]),∀0≤i<n

The following animation illustrates the method:

1 / 23

Complexity Analysis

Time complexity : O(n^2)O(n
2
). Two loops of nn are there.

Space complexity : O(n)O(n). dpdp array of size nn is used.

Approach #4 Dynamic Programming with Binary Search[Accepted]:
Algorithm

In this approach, we scan the array from left to right. We also make use of a dpdp array initialized with all 0's. This dpdp array is meant to store the increasing subsequence formed by including the currently encountered element. While traversing the numsnums array, we keep on filling the dpdp array with the elements encountered so far. For the element corresponding to the j^{th}j
th
 index (nums[j]nums[j]), we determine its correct position in the dpdp array(say i^{th}i
th
index) by making use of Binary Search(which can be used since the dpdp array is storing increasing subsequence) and also insert it at the correct position. An important point to be noted is that for Binary Search, we consider only that portion of the dpdp array in which we have made the updates by inserting some elements at their correct positions(which remains always sorted). Thus, only the elements upto the i^{th}i
th
 index in the dpdp array can determine the position of the current element in it. Since, the element enters its correct position(ii) in an ascending order in the dpdp array, the subsequence formed so far in it is surely an increasing subsequence. Whenever this position index ii becomes equal to the length of the LIS formed so far(lenlen), it means, we need to update the lenlen as len = len + 1len=len+1.

Note: dpdp array does not result in longest increasing subsequence, but length of dpdp array will give you length of LIS.

Consider the example:

input: [0, 8, 4, 12, 2]

dp: [0]

dp: [0, 8]

dp: [0, 4]

dp: [0, 4, 12]

dp: [0 , 2, 12] which is not the longest increasing subsequence, but length of dpdp array results in length of Longest Increasing Subsequence.


Note: Arrays.binarySearch() method returns index of the search key, if it is contained in the array, else it returns (-(insertion point) - 1). The insertion point is the point at which the key would be inserted into the array: the index of the first element greater than the key, or a.length if all elements in the array are less than the specified key.

Complexity Analysis

Time complexity : O(nlog(n))O(nlog(n)). Binary search takes log(n)log(n) time and it is called nn times.

Space complexity : O(n)O(n). dpdp array of size nn is used.
"""

"""
https://leetcode.com/problems/longest-increasing-subsequence/discuss/74824/JavaPython-Binary-search-O(nlogn)-time-with-explanation

Java/Python Binary search O(nlogn) time with explanation
56.0K
VIEWS
343
Last Edit: 34 minutes ago

dietpepsi
dietpepsi
 6293
tails is an array storing the smallest tail of all increasing subsequences with length i+1 in tails[i].
For example, say we have nums = [4,5,6,3], then all the available increasing subsequences are:

len = 1   :      [4], [5], [6], [3]   => tails[0] = 3
len = 2   :      [4, 5], [5, 6]       => tails[1] = 5
len = 3   :      [4, 5, 6]            => tails[2] = 6
We can easily prove that tails is a increasing array. Therefore it is possible to do a binary search in tails array to find the one needs update.

Each time we only do one of the two:

(1) if x is larger than all tails, append it, increase the size by 1
(2) if tails[i-1] < x <= tails[i], update tails[i]
Doing so will maintain the tails invariant. The the final answer is just the size.

Java

public int lengthOfLIS(int[] nums) {
    int[] tails = new int[nums.length];
    int size = 0;
    for (int x : nums) {
        int i = 0, j = size;
        while (i != j) {
            int m = (i + j) / 2;
            if (tails[m] < x)
                i = m + 1;
            else
                j = m;
        }
        tails[i] = x;
        if (i == size) ++size;
    }
    return size;
}
// Runtime: 2 ms
Python

def lengthOfLIS(self, nums):
    tails = [0] * len(nums)
    size = 0
    for x in nums:
        i, j = 0, size
        while i != j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
    return size

# Runtime: 48 ms
"""

