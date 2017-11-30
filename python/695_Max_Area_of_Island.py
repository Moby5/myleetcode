#!/usr/bin/env python
# coding=utf-8
"""
http://bookshadow.com/weblog/2017/10/08/leetcode-max-area-of-island/

695. Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.

题目大意：
给定二维格子grid，上下左右相邻的1组成岛屿，求岛屿的最大面积。

解题思路：
FloodFill（洪水填充）
"""

import numpy as np

class Solution(object):
    def maxAreaOfIsland_v0(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 深度优先搜索 + 二维数组记录元素是否已被访问
        if not grid: return 0
        h, w = len(grid), len(grid[0])
        visited = np.zeros((h, w))        
        ans = 0
        for i in range(0, h):
        	for j in range(0, w):
        		if not visited[i][j]:
        			#dfs(i, j)
        			visited[i][j] = 1
        			if grid[i][j]:
        				area = 0
        				queue = []
        				queue.append((i, j))
        				while queue:
        					p, q = queue.pop()
        					area += 1        					
        					#print "p, q, ans", p, q, area			
        					if p-1 >= 0 and grid[p-1][q] and not visited[p-1][q]: 
        						queue.append((p-1, q))
        						visited[p-1][q] = 1             						     						
        					if p+1 < h and grid[p+1][q] and not visited[p+1][q]: 
        						queue.append((p+1, q))           						  
        						visited[p+1][q] = 1
        					if q-1 >= 0 and grid[p][q-1] and not visited[p][q-1]: 
        						queue.append((p, q-1)) 						  					
        						visited[p][q-1] = 1
        					if q+1 < w and grid[p][q+1] and not visited[p][q+1]: 
        						queue.append((p, q+1))        		
        						visited[p][q+1] = 1				    						     					        					
        				#print "area:", area
        				if area > ans: ans = area
        return ans


    def maxAreaOfIsland(self, grid):  # DFS + 访问过的位置被置零
    	h, w = len(grid), len(grid[0])
        ans = 0
        for i in range(0, h):
        	for j in range(0, w):
        		if grid[i][j]:
        			area = 0
        			queue = [(i, j)]
        			grid[i][j] = 0        			
        			while queue:
        				p, q = queue.pop()
        				area += 1
        				for x, y in ((p-1, q), (p+1, q), (p, q-1), (p, q+1)):
        					if 0<=x<h and 0<=y<w and grid[x][y]:
        						queue.append((x, y))  
        						grid[x][y] = 0
        			if area > ans: ans = area
        return ans


    def maxAreaOfIsland_ref(self, grid):
        def bfs(grid, x, y):
	        dxs = [1, 0, -1, 0]
	        dys = [0, 1, 0, -1]
	        queue = [(x, y)]
	        grid[x][y] = 0
	        ans = 0
	        while queue:
	            x, y = queue.pop(0)
	            ans += 1
	            for dx, dy in zip(dxs, dys):
	                nx, ny = x + dx, y + dy
	                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
	                    if grid[nx][ny]:
	                        grid[nx][ny] = 0
	                        queue.append((nx, ny))
	        return ans

        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y]:
                    ans = max(ans, bfs(grid, x, y))
        return ans

    def maxAreaOfIsland_ref2(self, grid):  # Depth-First Search (Recursive) https://leetcode.com/problems/max-area-of-island/solution/
        seen = set()
        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                    and (r, c) not in seen and grid[r][c]):
                return 0
            seen.add((r, c))
            return (1 + area(r+1, c) + area(r-1, c) +
                    area(r, c-1) + area(r, c+1))

        return max(area(r, c)
                   for r in range(len(grid))
                   for c in range(len(grid[0])))  

    def maxAreaOfIsland_ref3(self, grid):  # Depth-First Search (Iterative) 
        seen = set()
        ans = 0
        for r0, row in enumerate(grid):
            for c0, val in enumerate(row):
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        r, c = stack.pop()
                        shape += 1
                        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                            if (0 <= nr < len(grid) and 0 <= nc < len(grid[0])
                                    and grid[nr][nc] and (nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans                         



solution = Solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,1,1,0,1,0,0,0,0,0,0,0,0],
		[0,1,0,0,1,1,0,0,1,0,1,0,0],
		[0,1,0,0,1,1,0,0,1,1,1,0,0],
		[0,0,0,0,0,0,0,0,0,0,1,0,0],
		[0,0,0,0,0,0,0,1,1,1,0,0,0],
		[0,0,0,0,0,0,0,1,1,0,0,0,0]]  # 6
print solution.maxAreaOfIsland(grid)
grid = [[0,0,0,0,0,0,0,0]] # 0
print solution.maxAreaOfIsland(grid)
grid = [[1,1,0,0,0],
		[1,1,0,0,0],
		[0,0,0,1,1],
		[0,0,0,1,1]]  # 4
print solution.maxAreaOfIsland(grid)	
grid = [[0,1],
		[1,1]]	 # 3
print solution.maxAreaOfIsland(grid)			