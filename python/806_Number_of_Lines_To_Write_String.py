#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-07

"""
https://leetcode.com/problems/number-of-lines-to-write-string/description/

806. Number of Lines To Write String

We are to write the letters of a given string S, from left to right into lines. Each line has maximum width 100 units, and if writing a letter would cause the width of the line to exceed 100 units, it is written on the next line. We are given an array widths, an array where widths[0] is the width of 'a', widths[1] is the width of 'b', ..., and widths[25] is the width of 'z'.

Now answer two questions: how many lines have at least one character from S, and what is the width used by the last such line? Return your answer as an integer list of length 2.

 

Example :
Input: 
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
Output: [3, 60]
Explanation: 
All letters have the same length of 10. To write all 26 letters,
we need two full lines and one line with 60 units.
Example :
Input: 
widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
Output: [2, 4]
Explanation: 
All letters except 'a' have the same length of 10, and 
"bbbcccdddaa" will cover 9 * 10 + 2 * 4 = 98 units.
For the last 'a', it is written on the second line because
there is only 2 units left in the first line.
So the answer is 2 lines, plus 4 units in the second line.
 

Note:

The length of S will be in the range [1, 1000].
S will only contain lowercase letters.
widths is an array of length 26.
widths[i] will be in the range of [2, 10].
"""

import string

class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        if not S:
            return 0, 0
        dmap = {le: widths[idx] for idx, le in enumerate(string.ascii_lowercase)}
        num_line, num_last = 0, 0
        for s in S:
            if num_last + dmap[s] > 100:
                num_line += 1
                num_last = dmap[s]
            else:
                num_last += dmap[s]
        return num_line + 1, num_last


solution = Solution()    
widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "abcdefghijklmnopqrstuvwxyz"
print solution.numberOfLines(widths, S)  # [3, 60]

widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaa"
print solution.numberOfLines(widths, S)  # [2, 4]

"""
https://leetcode.com/problems/number-of-lines-to-write-string/solution/
class Solution(object):
    def numberOfLines(self, widths, S):
        lines, width = 1, 0
        for c in S:
            w = widths[ord(c) - ord('a')]
            width += w
            if width > 100:
                lines += 1
                width = w

        return lines, width
        
http://bookshadow.com/weblog/2018/03/26/leetcode-number-of-lines-to-write-string/                
class Solution(object):
    def numberOfLines(self, widths, S):
        lines = cnt = 0
        for c in S:
            lc = widths[ord(c) - ord('a')]
            if cnt + lc > 100:
                lines += 1
                cnt = lc
            else:
                cnt += lc
        return [lines + (cnt > 0), cnt]        
"""        

