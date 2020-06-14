#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最长回文串.py 
@time: 2020/6/14 19:48 
"""


class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """

    def longestPalindrome(self, s):
        # write your code here
        alpha_dict = {}
        for c in s:
            count = alpha_dict.get(c, 0)
            count += 1
            alpha_dict[c] = count
        max_length = 0
        even = 0
        for alpha, count in alpha_dict.items():
            if count % 2 == 1:
                even = 1
                max_length += count - 1
            if count % 2 == 0:
                max_length += count
        return max_length + even


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("NTrQdQGgwtxqRTSBOitAXUkwGLgUHtQOmYMwZlUxqZysKpZxRoehgirdMUgy"))
