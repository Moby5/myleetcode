#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def is_power_of_three(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3 ** round(math.log(n, 3)) == n

    def is_power_of_three_recurisive(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 0 or n % 3 > 0:
            return False
        return self.is_power_of_three_recurisive(n / 3)

'''
def log(x, base=None): # real signature unknown; restored from __doc__
    """
    log(x[, base])

    Return the logarithm of x to the given base.
    If the base not specified, returns the natural logarithm (base e) of x.
    """
    pass
'''
