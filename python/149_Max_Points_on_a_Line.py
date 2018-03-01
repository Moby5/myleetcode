#!/usr/bin/env python
# coding=utf-8

"""    
    @File: 149_Max_Points_on_a_Line.py
    @Desc: 
    @Author: Abby Mo
    @Date Created: 2018-3-1
"""
# TODO 超时，未通过
"""
149. Max Points on a Line
http://bookshadow.com/weblog/2014/10/16/leetcode-max-points-line/

Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

题目大意
平面上有n个点，找出共线的点的最大个数

解题思路
很容易想到O(n^3)的解法，通过起点i，终点j枚举直线，然后枚举中间点k，依次判断k与i,j是否共线，统计最大值。

实际上，采用此题可以采用O(n^2 * log(n))的复杂度解答，思路为：枚举起点i，与终点j，依次计算i，j的斜率，
统计斜率相同的点的个数的最大值（另外需要考虑起点终点重合的情况）。
此法实际上采用了起点分组统计的思想，因此减少了一重循环。
"""


# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


from collections import defaultdict
from decimal import Decimal


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ans = 0
        size = len(points)
        for x in range(size):
            k_dict = defaultdict(int)
            same = 0
            for y in range(x + 1, size):
                if self.isEqual(points[x], points[y]):
                    same += 1
                else:
                    k = self.getK(points[x], points[y])
                    k_dict[k] += 1
            val = max(k_dict.values()) if len(k_dict) else 0
            ans = max(ans, val + same + 1)
        return ans

    def maxPoints_ref(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ans = 0
        size = len(points)
        for x in range(size):
            k_dict = {}
            same = 0
            for y in range(x + 1, size):
                if self.isEqual(points[x], points[y]):
                    same += 1
                else:
                    k = self.getK(points[x], points[y])
                    print "k", k
                    if k_dict.get(k) is None:
                        k_dict[k] = 1
                    else:
                        k_dict[k] += 1
            print "ans, same, k_dict, k_dict.values()", ans, same, k_dict, k_dict.values()
            val = 0
            if len(k_dict):
                val = max(k_dict.values())
            ans = max(ans, val + same + 1)
        return ans

    def getK(self, pa, pb):
        if pa.x == pb.x:
            return None
        return Decimal(pa.y - pb.y) / Decimal(pa.x - pb.x)  # 高精度
        # return 1.0 * (pb.y - pa.y) / (pb.x - pa.x)

    def isEqual(self, pa, pb):
        return pa.x == pb.x and pa.y == pb.y


if __name__ == '__main__':
    # locs = [[0, 0], [1, 1], [2, 2]]
    locs = [[0, 0], [94911151, 94911150], [94911152, 94911151]]   # 2
    # locs = []   # 0
    # locs = [[0,0]]  # 1
    # locs = [[0,0],[0,0]]  # 2
    # locs = [[0,0],[1,0]]  # 2
    points = []
    for loc in locs:
        points.append(Point(loc[0], loc[1]))
    solution = Solution()
    print solution.maxPoints(points)
    print solution.maxPoints_ref(points)


