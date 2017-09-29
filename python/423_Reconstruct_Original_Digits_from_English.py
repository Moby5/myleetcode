#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/16/leetcode-reconstruct-original-digits-from-english/

423. Reconstruct Original Digits from English

Given a non-empty string containing an out-of-order English representation of digits 0-9, 
output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. 
That means invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.

Example 1:
Input: "owoztneoer"
Output: "012"

Example 2:
Input: "fviefuro"
Output: "45"

题目大意：
给定一个非空字符串，包含一组乱序的英文字母表示的数字0-9，按递增序输出这些数字。

注意：

输入只包含小写英文字母
输入确保是有效的，并且一定可以转换为其原始数字。这意味着不会出现"abc", "zerone"之类的非法输入
输入长度小于50000
解题思路：
字符统计 + 枚举

统计字符串s中各字符的个数，需要注意的是，在枚举英文字母时，需要按照特定的顺序方可得到正确答案。

例如按照顺序：6028745913，这个顺序可以类比拓扑排序的过程。

观察英文单词，six, zero, two, eight, seven, four中分别包含唯一字母x, z, w, g, v, u；因此6, 0, 2, 8, 7, 4需要排在其余数字之前。

排除这6个数字之后，剩下的4个数字中，按照字母唯一的原则顺次挑选。

由于剩下的单词中，只有five包含f，因此选为下一个单词；

以此类推，可以得到上面所述的顺序。
"""

from collections import Counter, defaultdict

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        # nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        nums = ['eight', 'four', 'two', 'six', 'zero', 'five', 'three', 'seven', 'nine', 'one']
        digs = [8, 4, 2, 6, 0, 5, 3, 7, 9, 1]
        special_chars = ['g', 'u', 'w', 'x', 'z', 'f', 'h', 's', 'i', 'o']
        #chars = 'abcdefghijklmnopqrstuvwxyz'
        #print chars, len(chars)
        #d = defaultdict(list) 
        #for n in nums:
        #    for ch in n:
        #        d[ch].append(n)
        #for ch, n in d.iteritems():
        #    print ch, n

        ans = []
        c = Counter(s)
        for idx, special_ch in enumerate(special_chars):
            while c[special_ch] > 0:
                # print special_ch, c[special_ch], digs[idx]
                ans.append(digs[idx])
                for ch in nums[idx]:
                    c[ch] -= 1
        ans = sorted(ans)
        return ''.join(str(i) for i in ans)

    def originalDigits_v1(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnts = Counter(s)
        nums = ['six', 'zero', 'two', 'eight', 'seven', 'four', 'five', 'nine', 'one', 'three']
        numc = [collections.Counter(num) for num in nums]
        digits = [6, 0, 2, 8, 7, 4, 5, 9, 1, 3]
        ans = [0] * 10
        for idx, num in enumerate(nums):
            cntn = numc[idx]
            t = min(cnts[c] / cntn[c] for c in cntn)
            ans[digits[idx]] = t
            for c in cntn:
                cnts[c] -= t * cntn[c]
        return ''.join(str(i) * n for i, n in enumerate(ans))        

        
test = Solution()       
print test.originalDigits("owoztneoer")
print test.originalDigits("fviefuro")
print test.originalDigits("zerozero")

