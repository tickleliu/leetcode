#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最长回文子串.py 
@time: 2020/6/14 20:15 
"""


class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ""
        tmp = s[0]
        for idx in range(len(s) - 1):
            left, right = self.isPalindrome(s, idx, idx)  # even
            if right - left + 1 > len(tmp):
                tmp = s[left:right + 1]

            if s[idx] == s[idx + 1]:
                left, right = self.isPalindrome(s, idx, idx + 1)  # odd
                if right - left + 1 > len(tmp):
                    tmp = s[left:right + 1]
        return tmp

    def isPalindrome(self, s, left, right):
        l, r = left, right
        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                l = left
                r = right
                left = left - 1
                right = right + 1
            else:
                break
        return l, r


if __name__ == "__main__":
    s = Solution()
    r = s.longestPalindrome("aba")
    print(r)
