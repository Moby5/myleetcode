#!/usr/bin/env python
# coding=utf-8
# Date: 2018-10-17

"""
https://leetcode.com/problems/course-schedule/

There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""

class Solution(object):
    def canFinish(self, numCourses, prerequisites):  # 64 ms
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        degrees = [0] * numCourses
        childs = [[] for x in range(numCourses)]
        for pair in prerequisites:
            degrees[pair[0]] += 1
            childs[pair[1]].append(pair[0])
        courses = set(range(numCourses))
        flag = True
        while flag and len(courses):
            flag = False
            removeList = []
            for x in courses:
                if degrees[x] == 0:
                    for child in childs[x]:
                        degrees[child] -= 1
                    removeList.append(x)
                    flag = True
            for x in removeList:
                courses.remove(x)
        return len(courses) == 0
       
solution = Solution()
numCourses, prerequisites = 2, [[1,0]]
expected_output = True
output = solution.canFinish(numCourses, prerequisites)
assert expected_output == output, output

numCourses, prerequisites = 2, [[1,0], [0,1]]
expected_output = False
output = solution.canFinish(numCourses, prerequisites)
assert expected_output == output, output

print("Pass")

"""
http://bookshadow.com/weblog/2015/05/07/leetcode-course-schedule/

提示：

此问题等价于判断有向图中是否有环。如果存在环路，无法完成拓扑排序，也就不可能修完所有的课程。

表示图的方法有几种。例如，输入中的先修课程就是用一组边的方式表示图。这种图的表示方法合适吗？

通过DFS实现的拓扑排序—Cousera的一段21分钟的视频教程很好的解释了拓扑排序的基本概念。拓扑排序也可以通过BFS完成。

解题思路：
拓扑排序，如果可以完成拓扑排序，返回True，否则返回False
"""

