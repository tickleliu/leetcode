#!/usr/bin/env python  
# encoding: utf-8  

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 无重复字符的最长子串.py 
@time: 2020/5/7 21:18 
"""


def length_of_longest_str(str="abcabdcbefb"):
    bit_map = [0] * 256
    right = 0
    max_len = 0
    for left in range(len(str)):
        while right < len(str):
            index = ord(str[right])
            if bit_map[index] == 0:
                bit_map[index] = 1
                right += 1
                if right - left > max_len:
                    max_len = right - left
            else:
                break
        index = ord(str[left])
        bit_map[index] = 0
    return max_len


if __name__ == "__main__":
    res = length_of_longest_str()
    print(res)