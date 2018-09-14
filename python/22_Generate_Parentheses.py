#!/usr/bin/env python
# coding=utf-8
# Date: 2018-09-14

"""
https://leetcode.com/problems/generate-parentheses/description/

22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

伪代码(递归法)
if len(s) == 2*n:
    将s加入到输出列表
if 左括号数目 < n:
    加入左括号
if 右括号数目 < 左括号数目:
    加入右括号
    
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.output_list = list()
        self.n = n
        
        def backtrack(s, left, right):
            if len(s) == n * 2:
                self.output_list.append(s)
                return
            if left < self.n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)
        
        backtrack("", 0, 0)
        return self.output_list

       
solution = Solution()
print(solution.generateParenthesis(3))


"""
https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution

The idea here is to only add '(' and ')' that we know will guarantee us a solution (instead of adding 1 too many close). Once we add a '(' we will then discard it and try a ')' which can only close a valid '('. Each of these steps are recursively called.

 public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<String>();
        backtrack(list, "", 0, 0, n);
        return list;
    }
    
    public void backtrack(List<String> list, String str, int open, int close, int max){
        
        if(str.length() == max*2){
            list.add(str);
            return;
        }
        
        if(open < max)
            backtrack(list, str+"(", open+1, close, max);
        if(close < open)
            backtrack(list, str+")", open, close+1, max);
    }

"""

