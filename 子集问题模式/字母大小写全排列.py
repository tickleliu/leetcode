#!/usr/bin/env python  
# encoding: utf-8  

"""
示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]

@version: v1.0
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 字母大小写全排列.py 
@time: 2020/5/25 17:09 
"""

from copy import deepcopy


def letter_case_permutation(s="a1b2"):
    result = [s]
    s = list(s)

    def _letter_case_permutation(s: str, i):

        if i >= len(s):
            return

        if s[i].isalpha():
            s1 = deepcopy(s)
            if s[i].islower():
                s1[i] = s[i].upper()
            else:
                s1[i] = s[i].lower()
            result.append("".join(s1))
            _letter_case_permutation(s1, i + 1)
        _letter_case_permutation(s, i + 1)

    _letter_case_permutation(s, 0)

    return result


if __name__ == "__main__":
    result = letter_case_permutation()
    print(result)

    result = letter_case_permutation(s="12345")
    print(result)

    result = letter_case_permutation(s="12z45")
    print(result)
