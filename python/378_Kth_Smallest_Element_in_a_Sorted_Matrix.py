#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-20

"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/

378. Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

"""


import heapq
import bisect

class Solution(object):
    def kthSmallest(self, matrix, k):  #  二分查找（Binary Search） 优化  56 ms
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = self.countLower(matrix, mid)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt

        
    def kthSmallest_v3(self, matrix, k):  #  二分查找（Binary Search） 32 ms
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = sum(bisect.bisect_right(m, mid) for m in matrix)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo
        
    def kthSmallest_v2(self, matrix, k):  #  优先队列 / 堆 （Priority Queue / Heap） 优化
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
        
    def kthSmallest_v1(self, matrix, k):  #  优先队列 / 堆 （Priority Queue / Heap）
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        visited[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans
        
    def kthSmallest_v0(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        return sorted([cell for row in matrix for cell in row])[k-1]

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

solution = Solution()
print(solution.kthSmallest(matrix, k))

        
"""
http://bookshadow.com/weblog/2016/08/01/leetcode-kth-smallest-element-in-a-sorted-matrix/
题目大意：
给定一个 n x n 矩阵，其中每一行每一列都按照递增序排列，寻找矩阵中的第k小元素。

注意是要寻找排好序的第k小元素，而不是第k个不重复元素。

测试用例如题目描述。

注意：

你可以假设k总是有效的， 1 ≤ k ≤ n2

解题思路：

解法I 优先队列 / 堆 （Priority Queue / Heap）

首先将矩阵的左上角（下标0,0）元素加入堆
然后执行k次循环：
弹出堆顶元素top，记其下标为i, j
将其下方元素matrix[i + 1][j]，与右方元素matrix[i][j + 1]加入堆（若它们没有加入过堆）

Python代码：
class Solution(object):
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        visited = [[False] * n for _ in range(m)]
        q = [(matrix[0][0], 0, 0)]
        ans = None
        visited[0][0] = True
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if i + 1 < m and not visited[i + 1][j]:
                visited[i + 1][j] = True
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n and not visited[i][j + 1]:
                visited[i][j + 1] = True
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans

上述解法的优化：
实际上visited数组可以省去，在队列扩展时，当且仅当j == 0时才向下扩展，否则只做横向扩展。

Python代码：
class Solution(object):
    def kthSmallest(self, matrix, k):
        m, n = len(matrix), len(matrix[0])
        q = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(q)
            if j == 0 and i + 1 < m:
                heapq.heappush(q, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return ans

解法II 二分查找（Binary Search）

将查找上下限设为矩阵的右下角与左上角元素
查找过程中对中值在矩阵每一行的位置进行累加，记该值为loc
根据loc与k的大小关系调整上下限

Python代码：
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = sum(bisect.bisect_right(m, mid) for m in matrix)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

上述解法的优化：
循环中对每行的二分查找可以替换为：从矩阵左下角到右上角的“阶梯型”遍历。

Python代码：
class Solution(object):
    def kthSmallest(self, matrix, k):
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = self.countLower(matrix, mid)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def countLower(self, matrix, num):
        i, j = len(matrix) - 1, 0
        cnt = 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] <= num:
                cnt += i + 1
                j += 1
            else:
                i -= 1
        return cnt
"""        
        
