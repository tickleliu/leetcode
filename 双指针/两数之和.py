#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 两数之和.py
@time: 2020/06/16 17:25
"""


class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """

    hash_dict = {}

    def add(self, number):
        # write your code here
        TwoSum.hash_dict[number] = TwoSum.hash_dict.get(number, 0) + 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """

    def find(self, value):
        # write your code here
        for num in TwoSum.hash_dict:
            if num == value - num:
                if TwoSum.hash_dict[num] >= 2:
                    return True
            elif value - num in TwoSum.hash_dict:
                return True

        return False


if __name__ == "__main__":
    s = TwoSum()
    s.add(2)
    s.add(3)
    print(s.find(4))
    s.add(5)
    print(s.find(7))
