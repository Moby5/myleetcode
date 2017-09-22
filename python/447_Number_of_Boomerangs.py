#!/usr/bin/env python
# coding=utf-8
"""
447. Number of Boomerangs

Given n points in the plane that are all pairwise distinct, 
a "boomerang" is a tuple of points (i, j, k) 
such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs.
 You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

题目大意：
给定平面上的n个两两不同的点，一个“回飞镖”是指一组点(i, j, k)满足i到j的距离=i到k的距离（考虑顺序）

计算回飞镖的个数。你可以假设n最多是500，并且点坐标范围在 [-10000, 10000] 之内。

解题思路：
枚举点i(x1, y1)，计算点i到各点j(x2, y2)的距离，并分类计数

利用排列组合知识，从每一类距离中挑选2个点的排列数 A(n, 2) = n * (n - 1)

将上述结果累加即为最终答案
"""

from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):        
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def dis(p1, p2):
            return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

        ans = 0
        size = len(points)
        for i in range(size):
            distances = defaultdict(int)
            for j in range(size):
                distances[dis(points[i], points[j])] += 1
            for distance, count in distances.iteritems():
                ans += count * (count - 1)
        return ans

    
    def numberOfBoomerangs_v1(self, points):
        ans = 0
        for x1, y1 in points:
            dmap = collections.defaultdict(int)
            for x2, y2 in points:
                dmap[(x1 - x2) ** 2 + (y1 - y2) ** 2] += 1
            for d in dmap:
                ans += dmap[d] * (dmap[d] - 1)
        return ans    

        
test = Solution()
print test.numberOfBoomerangs([[0,0], [1,0], [2,0]])
        
