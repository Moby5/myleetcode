#!/usr/bin/env python
# coding=utf-8

"""
http://bookshadow.com/weblog/2016/10/02/leetcode-longest-palindrome/

409. Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

题目大意：
给定一个只包含小写或者大写字母的字符串，寻找用这些字母可以组成的最长回文串的长度。

大小写敏感，例如"Aa"在这里不认为是一个回文。

注意：

假设给定字符串的长度不超过1000。

解题思路：
统计每个字母的出现次数：

  若字母出现偶数次，则直接累加至最终结果

  若字母出现奇数次，则将其值-1之后累加至最终结果

若存在出现奇数次的字母，将最终结果+1
"""

from collections import Counter

class Solution(object):
    def longestPalindrome_v0(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter(s)
        # print c,
        ans = 0
        single_added = False
        for k, v in c.most_common():
            # print k, v, ans, single_added
            if v % 2 == 0:
                ans += v
            elif v % 2 != 0:
                if single_added: 
                    if v >= 3: ans += v - 1
                    else: continue
                else:
                    ans += v
                    single_added = True
        return ans

    def longestPalindrome(self, s):
        counter = Counter(s)
        ans = 0
        odd = False
        for c in counter:
            val = counter[c]
            ans += val
            if val % 2 == 1:
                ans -= 1
                odd = True
        if odd: ans += 1
        return ans

    def longestPalindrome_ref(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = odd = 0
        cnt = collections.Counter(s)
        for c in cnt:
            ans += cnt[c]
            if cnt[c] % 2 == 1:
                ans -= 1
                odd += 1
        return ans + (odd > 0)        
       
test = Solution()
strs = ['abccccdd', 'bananas', 'ccc', 'bb', "tattarrattat", "civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"] # 7, 5, 3, 2, 12, 983
for str in strs:
    print str, test.longestPalindrome(str)
        
