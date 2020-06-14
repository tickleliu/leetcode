#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 字符串查找.py 
@time: 2020/6/14 19:59 
"""


class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if target in source:
            return source.index(target)
        else:
            return -1


if __name__ == "__main__":
    pass  