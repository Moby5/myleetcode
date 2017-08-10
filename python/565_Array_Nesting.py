#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2017/05/28/leetcode-array-nesting/

题目描述：
LeetCode 565. Array Nesting

A zero-indexed array A consisting of N different integers is given. The array contains all integers in the range [0, N - 1].

Sets S[K] for 0 <= K < N are defined as follows:

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.

Sets S[K] are finite for each K and should NOT contain duplicates.

Write a function that given an array A consisting of N integers, return the size of the largest set S[K] for this array.

Example 1:

Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:

N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of array A is an integer within the range [0, N-1].
题目大意：
索引从0开始的数组A包含N个不同的数字。每个数字范围[0, N - 1]

定义集合S[K] 对于 0 <= K < N：

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }

对于每一个K，S[K]是有限的，不包含重复。

编写函数返回最大的S[K]的大小。

注意：

N是整数，范围[1, 20000]
A中的元素各不相同
A是整数，范围[0, N - 1]
解题思路：
DFS / 并查集

由于A是[0 .. N - 1]的排列，因此输入可以看做顶点集合V = [0 .. N - 1]，边集合E = [[i, A[i]] (i ∈   [0 .. N - 1])的有向图

图的形态是一个或者多个O型的环（可以是自环），而不会出现ρ型的环
"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int        
        """        
        def search(k):
            cnt = 0
            while nums[k] >= 0:
                cnt += 1
                next = nums[k]
                nums[k] = -1
                k = next
            return cnt

        ans = 0
        for k in range(len(nums)):
            ans = max(ans, search(k)) 
        return ans

"""
# Time Limit Exceeded
    ans = 0       
    for k in range(len(nums)):
        sk = set() 
        value = nums[k]
        while value not in sk:
            sk.add(value)
            value = nums[value]
        # print k, sk
        ans = max(ans, len(sk))
    return ans
"""   


A = [5,4,0,3,1,6,2]
test = Solution()
print test.arrayNesting(A)

