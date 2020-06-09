#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 回文串.py 
@time: 2020/6/7 21:44 
"""


class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """

    def validPalindrome(self, s):
        # Write your code here
        if s is None:
            return False

        def diff(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return left, right
                left += 1
                right -= 1

            return left, right

        left, right = 0, len(s) - 1
        left, right = diff(s, left, right)
        if left < right:
            l, r = diff(s, left + 1, right)
            if l >= r:
                return True

            l, r = diff(s, left, right - 1)
            if l >= r:
                return True
            return False
        else:
            return True


if __name__ == "__main__":
    s = Solution()
    s.validPalindrome("abc")
