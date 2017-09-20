#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/11/13/leetcode-assign-cookies/

455. Assign Cookies

Assume you are an awesome parent and want to give your children some cookies. 
But, you should give each child at most one cookie. 
Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with; 
and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
and the child i will be content. 
Your goal is to maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, 
you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.

题目大意：
假设你是一位很赞的家长想要给孩子一些饼干。但是，你只能至多给每个孩子一个饼干。
孩子i的贪婪因子为gi，意思是他所满意的饼干的最小尺寸；每一个饼干j的尺寸为sj。
如果sj >= gi，我们就可以把饼干j分给孩子i，然后孩子i会很满意。你的目标是最大化分到饼干的孩子的个数。

注意：
可以假设贪婪因子都是正数。
不可以为一个孩子分配多个饼干。

解题思路：
贪心算法（Greedy Algorithm）
首先对贪婪系数g、饼干尺寸s从小到大排序
令指针i指向g的末尾，指针j指向s的末尾
当g和s均≥0时，执行循环：
  若g[i] ≤ s[j] 则令计数器+1，并令j -= 1 （将j号饼干分配给i号孩子，并令j指向下一个更小的饼干）
  令i -= 1 （将i指向下一个贪婪系数更小的孩子）
"""

class Solution(object):
    def findContentChildren(self, g, s):  # my solution
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g, s = sorted(g, reverse=True), sorted(s, reverse=True)        
        ans = 0
        for gi in g:
            for sj in s[ans:]:
                if sj >= gi:
                    ans += 1   
                    break
        return ans
    
    def findContentChildren_v2(self, g, s):  # Greedy Algorithm
        cnt = 0
        i, j = len(g) - 1, len(s) - 1
        g, s = sorted(g), sorted(s)
        while min(i, j) >= 0:
            if g[i] <= s[j]:
                cnt += 1
                j -= 1
            i -= 1
        return cnt    

test = Solution()
print test.findContentChildren([1,2,3], [1,1])
print test.findContentChildren([1,2], [1,2,3])
