#!/usr/bin/env python  
# encoding: utf-8  

"""
比较含退格的字符串,#代表退格字符
输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。

@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 含退格字符串比较.py 
@time: 2020/5/9 17:50 
"""


def backspace_str_compare(str1, str2):
    new_str1 = compute(str1)
    new_str2 = compute(str2)
    return new_str1 == new_str2


def compute(str):
    new_str = ""
    for c in str:
        if c == "#":
            new_str = new_str[0:-1] if len(new_str) >= 1 else new_str
        else:
            new_str += c
    return new_str


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    print(backspace_str_compare("ab#c", "ad#c"))
    print(backspace_str_compare("ab##", "c#d#"))
    print(backspace_str_compare("a##c", "#a#c"))
