#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/09/leetcode-arithmetic-slices/

413. Arithmetic Slices

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

题目大意：
如果一组数包含至少3个元素，并且任意两个连续元素之差都相等，则称该序列为等差序列。

给定一个以0为起始下标的数组A，包含N个数字。数组的切片是指任意满足0 <= P < Q < N的整数对 (P, Q)。

数组A的切片 (P, Q) 是等差数列，如果满足下列条件：

A[P], A[p + 1], ..., A[Q - 1], A[Q]是等差数列。特别的，P + 1 < Q。

函数应当返回数组A的等差数列切片的个数。

解题思路：
若序列S为等差数列，其长度为N，则其等差数列切片的个数SUM = 1 + 2 + ... + (N - 2)

例如，等差数列[1, 2, 3, 4, 5, 6]的切片个数为1+2+3+4 = 10

这10个切片分别是：

[1,2,3], [1,2,3,4], [1,2,3,4,5], [1,2,3,4,5,6]
[2,3,4], [2,3,4,5], [2,3,4,5,6]
[3,4,5], [3,4,5,6]
[4,5,6]

其它解法
https://leetcode.com/articles/arithmetic-slices/

"""

class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3: return 0
        arr = []
        cur_slice = [A[0], A[1]]
        cur_diff = A[0] - A[1]
        # print cur_slice, cur_diff
        for i in range(2, len(A)):
            if A[i-1] - A[i] == cur_diff:
                cur_slice.append(A[i])
                # print cur_slice, cur_diff, A[i-1], A[i]
            else:
                if len(cur_slice) >= 3:
                    arr.append(cur_slice)
                cur_slice = [A[i-1], A[i]]
                cur_diff = A[i-1] - A[i]
                # print cur_slice, cur_diff, A[i-1], A[i]
        if len(cur_slice) >= 3:
            arr.append(cur_slice)
        # print arr
        ans = 0
        for li in arr:            
            size = len(li)
            ans += (1 + (size - 2)) * (size - 2) / 2 # 等差数列的切片个数公式
            # 枚举法
            # for n in range(3, size):
            #     ans += size - n + 1
            # ans += 1 # all numbers  
        return ans
        
    def numberOfArithmeticSlices_ref(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        size = len(A)
        if size < 3: return 0
        ans = cnt = 0
        delta = A[1] - A[0]
        for x in range(2, size):
            if A[x] - A[x - 1] == delta:
                cnt += 1
                ans += cnt
            else:
                delta = A[x] - A[x - 1]
                cnt = 0
        return ans        

test = Solution()        
print test.numberOfArithmeticSlices([1,2,3]) # 1
print test.numberOfArithmeticSlices([1,2,3,4]) # 3
print test.numberOfArithmeticSlices([1,2,3,4,5]) # 6
print test.numberOfArithmeticSlices([1,2,3,4,5,6]) # 10
print test.numberOfArithmeticSlices([1,2,3,8,9,10]) # 2
        
