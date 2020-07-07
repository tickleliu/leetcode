#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最大公约数.py 
@time: 2020/6/28 10:36 
"""


class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """

    def gcd(self, a, b):
        # write your code here
        if a < b:
            a, b = b, a
        if b == 0:
            return a
        return self.gcd(b, a % b)


if __name__ == "__main__":
    s = Solution()
    print(s.gcd(12, 16))
