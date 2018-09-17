#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-17

"""
https://leetcode.com/problems/4sum-ii/description/

454. 4Sum II

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""

from collections import Counter

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counter = Counter(a + b for a in A for b in B)
        return sum(counter[-c-d] for c in C for d in D)
        

solution = Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(solution.fourSumCount(A, B, C, D))

"""
https://leetcode.com/problems/4sum-ii/discuss/93917/Easy-2-lines-O(N2)-Python


http://bookshadow.com/weblog/2016/11/13/leetcode-4sum-ii/

解题思路：
利用字典cnt，将A，B中各元素（笛卡尔积）的和进行分类计数。

将C，D中各元素（笛卡尔积）和的相反数在cnt中的值进行累加，即为答案。

Python代码：
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        ans = 0
        cnt = collections.defaultdict(int)
        for a in A:
            for b in B:
                cnt[a + b] += 1
        for c in C:
            for d in D:
                ans += cnt[-(c + d)]
        return ans
"""

