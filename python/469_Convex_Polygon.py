#!/usr/bin/env python
# coding=utf-8
"""
LeetCode 469. Convex Polygon

Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.
Example 1:

[[0,0],[0,1],[1,1],[1,0]]

Answer: True

Explanation:
Example 2:

[[0,0],[0,10],[10,10],[10,0],[5,5]]

Answer: False

Explanation:
题目大意：
给定一组点，顺序相连可以组成一个多边形。判断多边形是否是凸包。

注意：

最少3个，最多10000个点
坐标在-10,000 到 10,000之间。
你可以假设组成的多边形总是简单多边形。换言之，我们确保每个顶点都是两条边的交点，其他边不会相互交叉。
解题思路：
遍历顶点，判断相邻三个顶点A、B、C组成的两个向量(AB, AC)的叉积是否同负同正。
"""


class Solution(object):
    def isConvex(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        def crossProduct(p0, p1, p2):
            x0, y0 = p0
            x1, y1 = p1
            x2, y2 = p2
            return (x2 - x0) * (y1 - y0) - (x1 - x0) * (y2 - y0)

        size = len(points)
        last = 0
        for x in range(size):
            p0, p1, p2 = points[x], points[(x+1) % size], points[(x+2) % size]
            p = crossProduct(p0, p1, p2)
            if p * last < 0:
                return False
            last = p
        return True

