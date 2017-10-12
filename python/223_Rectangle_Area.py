#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/06/08/leetcode-rectangle-area/

223. Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.

题目大意：
计算二维平面上两个直线矩形的覆盖面积。

矩形通过其左下角和右上角的坐标进行定义。

假设总面积不会超过int的最大值。

解题思路：
简单计算几何。根据容斥原理：S(M ∪ N) = S(M) + S(N) - S(M ∩ N)

题目可以转化为计算矩形相交部分的面积

S(M) = (C - A) * (D - B)

S(N) = (G - E) * (H - F)

S(M ∩ N) = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
"""

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a, c = max(A, E), min(C, G)
        b, d = max(B, F), min(D, H)
        sums = (C - A) * (D - B) + (G - E) * (H - F)
        return sums - max(c - a, 0) * max(d - b, 0)

    def computeArea_ref(self, A, B, C, D, E, F, G, H):
        sums = (C - A) * (D - B) + (G - E) * (H - F)
        return sums - max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)

test = Solution()
print test.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) # 45
print test.computeArea(0, 0, 0, 0, -1, -1, 1, 1) # 4
print test.computeArea(-2, -2, 2, 2, 3, 3, 4, 4) # 17

