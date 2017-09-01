#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/11/20/leetcode-island-perimeter/

463. Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. 
Grid cells are connected horizontally/vertically (not diagonally). 
The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). 
The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:

题目大意：
给定一个二维地图，1表示陆地，0表示水域。单元格水平或者竖直相连（不含对角线）。地图完全被水域环绕，只包含一个岛屿
（也就是说，一个或者多个相连的陆地单元格）。岛屿没有湖泊（岛屿内部环绕的水域）。单元格是边长为1的正方形。
地图是矩形，长宽不超过100。计算岛屿的周长。

解题思路：
每一个陆地单元格的周长为4，当两单元格上下或者左右相邻时，令周长减2。
"""

class Solution(object):  
    def islandPerimeter(self, grid):  # 加法
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        height = len(grid)
        width = len(grid[0]) if height else 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0: ans += 1
                    if j == 0 or grid[i][j-1] == 0: ans += 1
                    if j == width-1 or grid[i][j+1] == 0: ans += 1
                    if i == height-1 or grid[i+1][j] == 0: ans += 1   
        return ans
    
    def islandPerimeter_v2(self, grid): # 减法
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0]) if h else 0
        ans = 0
        for x in range(h):
            for y in range(w):
                if grid[x][y] == 1:
                    ans += 4
                    if x > 0 and grid[x - 1][y]:
                        ans -= 2
                    if y > 0 and grid[x][y - 1]:
                        ans -= 2
        return ans
                    

test = Solution()
grid = [[0,1,0,0], 
        [1,1,1,0], 
        [0,1,0,0],
        [1,1,0,0]]  # 16
# grid = [[1]]  # 4
print test.islandPerimeter(grid)
