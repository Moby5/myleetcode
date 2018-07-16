#!/usr/bin/env python
# coding=utf-8
# Date: 2018-07-16

"""
https://leetcode.com/problems/goat-latin/description/

824. Goat Latin

A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.
 
If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".
 
Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:

Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
Example 2:

Input: "The quick brown fox jumped over the lazy dog"
Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
 

Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""

class Solution(object):        
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        ans = []
        for widx, wd in enumerate(S.split(" ")):
            if wd[0].lower() not in "aeiou":
                wd = wd[1:] + wd[0]
            ans.append(wd + "ma" + "a" * (widx + 1))
        return " ".join(ans)
        
    def toGoatLatin_v1(self, S):
        """
        :type S: str
        :rtype: str
        """
        def convert(word):
            if word[0].lower() not in "aeiou":
                word = word[1:] + word[0]
            return word
        return " ".join([convert(wd) + "ma" + "a" * (widx + 1) for widx, wd in enumerate(S.split(" "))])                
        
    def toGoatLatin_v0(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = {'a', 'e', 'i', 'o', 'u'}
        swords = S.split(" ")
        ans = []
        for sidx, wd in enumerate(swords):
            if wd[0].lower() in vowel:
                ans.append(wd)
            else:
                ans.append(wd[1:] + wd[0])
            ans[-1] = ans[-1] + "ma" + "a" * (sidx + 1)
        return " ".join(ans)

solution = Solution()    
S = "I speak Goat Latin"
print solution.toGoatLatin(S)
S = "The quick brown fox jumped over the lazy dog"
print solution.toGoatLatin(S)


"""
https://leetcode.com/problems/goat-latin/solution/

class Solution(object):
    def toGoatLatin(self, S):

        def convert(word):
            if word[0] not in 'aeiouAEIOU':
                word = word[1:] + word[:1]
            return word + 'ma'

        return " ".join(convert(word) + 'a' * i
                        for i, word in enumerate(S.split(), 1))
                                                
"""                     

"""
http://bookshadow.com/weblog/2018/04/29/leetcode-goat-latin/

题目大意：
将句子S中的单词按照如下规则进行转换：

如果单词首字母是元音，在单词末尾添加ma

否则，将单词首字母移动至末尾，并添加ma

对于第i个单词，在其末尾添加i个a
解题思路：
字符串模拟

class Solution(object):
    def toGoatLatin(self, S):
        ans = []
        for idx, word in enumerate(S.split()):
            latin = word
            if word[0].lower() not in 'aeiou':
                latin = word[1:] + word[0]
            latin += 'ma' + 'a' * (idx + 1)
            ans.append(latin)
        return ' '.join(ans)
"""   

