#!/usr/bin/env python
# coding=utf-8
"""
http://bookshadow.com/weblog/2017/09/30/leetcode-employee-importance/

LeetCode 690. Employee Importance

You are given a data structure of employee information, 
which includes the employee's unique id, his importance value and his direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. 
They have importance value 15, 10 and 5, respectively. 
Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], 
and employee 3 has [3, 5, []]. 
Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, 
you need to return the total importance value of this employee and all his subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. 
They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.
Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

题目大意：
给定一组雇员信息，包含ID，影响力，直接下属的ID列表。

求某雇员及其所有下属的影响力之和。

解题思路：
递归（Recurion）
"""

# # Employee info
# class Employee(object):
#     def __init__(self, id, importance, subordinates):
#         # It's the unique id of each node.
#         # unique id of this employee
#         self.id = id
#         # the importance value of this employee
#         self.importance = importance
#         # the id of direct subordinates
#         self.subordinates = subordinates
        
class Solution(object):   
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """        
        id2employee = {em.id : em for em in employees}                           
        def dfs(key_id):
            em = id2employee[key_id]
            return em.importance + sum([dfs(_id) for _id in em.subordinates])
        return dfs(id)   
    
    def getImportance_ref(self, employees, id):
        dmap = {emp.id : emp for emp in employees}
        def solve(id):
            emp = dmap[id]
            return emp.importance+ sum(solve(id) for id in emp.subordinates)
        return solve(id)    
            
