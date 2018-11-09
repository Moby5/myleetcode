#!/usr/bin/env python
# coding=utf-8
# Date: 2018-11-09
# File: 200_Number_of_Islands.py

"""
https://leetcode.com/problems/number-of-islands

200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

class Solution(object):
    def numIslands(self, grid):  # 104 ms
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not len(grid):
            return ans
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for x in range(m)]  # m * n
        for x in range(m):
            for y in range(n):
                if grid[x][y] == '1' and not visited[x][y]:
                    ans += 1
                    self.bfs(grid, visited, x, y, m, n)
        return ans

    def bfs(self, grid, visited, x, y, m, n):
        dz = zip([1, 0, -1, 0], [0, 1, 0, -1])
        queue = [(x, y)]
        visited[x][y] = True
        while queue:
            front = queue.pop(0)
            for p in dz:
                np = (front[0] + p[0], front[1] + p[1])
                if self.isValid(np, m, n) and grid[np[0]][np[1]] == '1' and not visited[np[0]][np[1]]:
                    visited[np[0]][np[1]] = True
                    queue.append(np)

    def isValid(self, np, m, n):
        return np[0] >= 0 and np[0] < m and np[1] >= 0 and np[1] < n
        

solution = Solution()

Input = [
['1', '1', '1', '1', '0'],
['1', '1', '0', '1', '0'],
['1', '1', '0', '0', '0'],
['0', '0', '0', '0', '0']]
Output = 1
pred = solution.numIslands(Input)
assert pred == Output, pred

Input = [
['1', '1', '0', '0', '0'],
['1', '1', '0', '0', '0'],
['0', '0', '1', '0', '0'],
['0', '0', '0', '1', '1']]
Output = 3
pred = solution.numIslands(Input)
assert pred == Output, pred

print("Pass.")

"""
http://bookshadow.com/weblog/2015/04/08/leetcode-number-islands/

题目大意：
给定一个由字符‘1’（陆地）和‘0’（水域）组成的二维网格地图，计算岛屿的个数。岛屿被水域环绕，由竖直或者水平方向邻接的陆地构成。你可以假设网格地图的四条边都被水域包围。

测试样例见题目描述。

解题思路：
FloodFill，BFS（广度优先搜索）或者DFS（深度优先搜索）均可。
"""

