#!/usr/bin/env python
# coding=utf-8

import sys

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype : str
        """
        return ' '.join(w[::-1] for w in s.split())


if __name__ == '__main__':

    test = Solution()
    print test.reverseWords(sys.argv[1])
