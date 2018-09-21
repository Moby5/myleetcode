#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-21

"""
https://leetcode.com/problems/flatten-nested-list-iterator/description/

341. Flatten Nested List Iterator

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class NestedIterator(object):  # 64ms

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [e for e in nestedList[::-1]]
        
    def next(self):
        """
        :rtype: int
        """       
        return self.stack.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            curr = self.stack.pop().getList()
            for e in curr[::-1]:
                self.stack.append(e)
        return False


"""
https://leetcode.com/problems/flatten-nested-list-iterator/discuss/80147/Simple-Java-solution-using-a-stack-with-explanation

http://bookshadow.com/weblog/2016/04/17/leetcode-flatten-nested-list-iterator/

class NestedIterator(object):  # 132ms

    def __init__(self, nestedList):
        self.list = nestedList
        self.stack = []
        
    def next(self):      
        return self.stack.pop()

    def hasNext(self):
        while self.list or self.stack:
            if not self.stack:
                self.stack.append(self.list.pop(0))
            while self.stack and not self.stack[-1].isInteger():
                top = self.stack.pop().getList()
                for e in top[::-1]:
                    self.stack.append(e)
            if self.stack and self.stack[-1].isInteger():
                return True
        return False
"""


# Your NestedIterator object will be instantiated and called as such:
nestedList = [1,[4,[6]]]
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())        
    
