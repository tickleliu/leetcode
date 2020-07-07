#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 快速幂.py 
@time: 2020/6/28 10:27 
"""


class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """

    def fastPower(self, a, b, n):
        # write your code here
        if n == 0:
            return 1 % b

        product = self.fastPower(a, b, n // 2)
        product = product * product
        if n % 2 != 0:
            product = (product * a) % b

        return product


if __name__ == "__main__":
    import math

    s = Solution()
    a = 10
    b = 3
    n = 3
    r = s.fastPower(a, b, n)
    print(r)
    print(math.pow(a, n) % b)
