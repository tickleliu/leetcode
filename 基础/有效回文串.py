#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 有效回文串.py 
@time: 2020/6/14 20:01 
"""


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s: str):
        # write your code here
        if not s or len(s) == 0:
            return True
        left, right = 0, len(s) - 1

        while left < right:
            while left < right:
                if s[left].isalnum():
                    break
                left += 1

            while left < right:
                if s[right].isalnum():
                    break
                right -= 1

            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            return False

        return True


if __name__ == "__main__":
    s = Solution()
    r = s.isPalindrome(" ")
    print(r)
