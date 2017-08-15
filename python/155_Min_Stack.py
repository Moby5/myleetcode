#!/usr/bin/env python
# coding=utf-8

"""
https://leetcode.com/problems/min-stack/description/

[LeetCode]155. Min Stack 

题目描述：
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

题目大意：
设计一个栈，支持在常数时间内push，pop，top，和取最小值。

push(x) -- 元素x压入栈
pop() -- 弹出栈顶元素
top() -- 获取栈顶元素
getMin() -- 获取栈中的最小值
解题思路：
“双栈法”，栈stack存储当前的所有元素，minStack存储栈中的最小元素。

在操作元素栈stack的同时，维护最小值栈minStack。

对于push（x）操作：

stack.push( x )
minStack.push( min( minStack.top(), x ) )
1
2
注意事项（Tricks）：
leetcode OJ对于该题目的内存限制比较严苛，直接使用双栈法容易出现Memory Limit Exceeded（MLE）

可以使用下面的优化解决此问题，minStack存储元组（minVal, count），分别记录当前的最小值和出现次数。

如果新增元素x与最小值栈顶的minVal相同，则只更新count。
"""

class MinStack:
  # @param x, an integer
  # @return an integer
  def __init__(self):
    self.stack = []
    self.minStack = [] #最小值栈 （最小值，出现次数）

  def push(self, x):
    self.stack.append(x)
    #如果 新增值x == 最小值栈顶的值
    if len(self.minStack) and x == self.minStack[-1][0]:
      #最小值栈顶元素次数+1
      self.minStack[-1] = (x, self.minStack[-1][1] + 1)
    #如果 最小值栈为空，或者新增值 < 最小值栈顶的值
    elif len(self.minStack) == 0 or x < self.minStack[-1][0]:
      #x入最小值栈
      self.minStack.append((x, 1))

  def pop(self):
    #如果 栈顶值 == 最小值栈顶值
    if self.top() == self.getMin():
      #如果 最小值栈顶元素次数 > 1
      if self.minStack[-1][1] > 1:
        #最小值栈顶元素次数 - 1
        self.minStack[-1] = (self.minStack[-1][0], self.minStack[-1][1] - 1)
      else:
        #最小值栈顶元素弹出
        self.minStack.pop()
    return self.stack.pop()

  def top(self):
    return self.stack[-1]

  def getMin(self):
    return self.minStack[-1][0]


class MinStack_v2(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []   
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)      
        if not self.min_stack or x < self.min_stack[-1][0]:
            self.min_stack.append((x, 1))
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1] = (x, self.min_stack[-1][1]+1)                
        
    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return
        if self.top() == self.getMin():
            if self.min_stack[-1][1] == 1:
                self.min_stack.pop()
            else:
                self.min_stack[-1] = (self.min_stack[-1][0], self.min_stack[-1][1]-1)
        self.stack.pop()        
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1][0]
            

minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print minStack.getMin();   #--> Returns -3.
minStack.pop();
print minStack.top();      #--> Returns 0.
print minStack.getMin();   #--> Returns -2.

