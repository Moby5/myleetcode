#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/06/11/leetcode-implement-stack-using-queues/

225. Implement Stack using Queues
Implement the following operations of a stack using queues.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

题目大意：
使用队列实现栈的下列操作：

push(x) -- 将元素x压入栈.
pop() -- 移除栈顶元素.
top() -- 获得栈顶元素.
empty() -- 返回栈是否为空.

注意：

你可以假设所有的操作都是有效的（例如，不会对空栈执行pop或者top操作）
取决于你使用的语言，queue可能没有被原生支持。你可以使用list或者deque（双端队列）模拟一个队列，只要保证你仅仅使用队列的标准操作即可——亦即只有如下操作是有效的：
push to back（加入队尾），pop from front（弹出队首），size（取队列大小）以及is empty（判断是否为空）

解题思路：
# push(x) -- 使用queue的push to back操作.
# pop() -- 将queue中除队尾外的所有元素pop from front然后push to back，最后执行一次pop from front
# top() -- 将queue中所有元素pop from front然后push to back，使用辅助变量top记录每次弹出的元素，返回top
# empty() -- 使用queue的is empty操作.
"""


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        # for x in range(len(self.queue) - 1):
        #     self.queue.append(self.queue.pop(0))
        # self.queue.pop(0)
        return self.queue.pop()
        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        # top = None
        # for x in range(len(self.queue)):
        #     top = self.queue.pop(0)
        #     self.queue.append(top)
        # return top
        return self.queue[-1]
        

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue) == 0


if __name__ == '__main__':
    obj = MyStack()
    for x in range(5):
        obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()

    print param_2
    print param_3
    print param_4

"""
class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.queue = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.queue.append(x)

    # @return nothing
    def pop(self):
        for x in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
        self.queue.pop(0)

    # @return an integer
    def top(self):
        top = None
        for x in range(len(self.queue)):
            top = self.queue.pop(0)
            self.queue.append(top)
        return top

    # @return an boolean
    def empty(self):
        return self.queue == []
"""