#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2015/07/07/leetcode-implement-queue-using-stacks/

232. Implement Queue using Stacks
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Notes:
You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

题目大意：
使用栈实现队列的下列操作：
push(x) -- 将元素x加至队列尾部
pop() -- 从队列头部移除元素
peek() -- 获取队头元素
empty() -- 返回队列是否为空

注意：
你只可以使用栈的标准操作——这意味着只有push to top（压栈）, peek/pop from top（取栈顶/弹栈顶），以及empty（判断是否为空）是允许的
取决于你的语言，stack可能没有被内建支持。你可以使用list（列表）或者deque（双端队列）来模拟，确保只使用栈的标准操作即可
你可以假设所有的操作都是有效的（例如，不会对一个空的队列执行pop或者peek操作）

解题思路：
“双栈法”或者“单栈法”均可。
"""

"""
双栈法：
维护两个栈inStack与outStack，其中inStack接收push操作新增的元素，outStack为pop/peek操作提供服务
由于栈具有后进先出（Last In First Out）的性质，栈A中的元素依次弹出并压入空栈B之后，栈A中元素的顺序会被逆转
当执行pop或者peek操作时，如果outStack中元素为空，则将inStack中的所有元素弹出并压入outStack，然后对outStack执行相应操作
由于元素至多只会从inStack向outStack移动一次，因此peek/pop操作的平摊开销为O(1)
"""
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.inStack.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.peek()
        return self.outStack.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.inStack) + len(self.outStack) == 0


"""
单栈法：
在执行push操作时，使用辅助栈swap，将栈中元素顺序按照push顺序的逆序存储。
此时，push操作的时间复杂度为O(n)，其余操作的时间复杂度为O(1)
"""
class MyQueue2(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        swap = []
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stack) == 0


if __name__ == '__main__':
    obj = MyQueue2()
    for x in range(5):
        obj.push(x)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()

    print param_2
    print param_3
    print param_4
