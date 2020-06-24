#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 字符串去重_最小字典序.py
@time: 2020/06/24 16:27
给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

示例 1:
输入: “bcabc”
输出: “abc”
示例 2:
输入: “cbacdcbc”
输出: “acdb”
"""


class Solution:
    def removeDuplicateLetters(self, s):

        char_map = {}
        visit_char = {}
        for char in s:
            count = char_map.get(char, 0)
            char_map[char] = count + 1
            visit_char[char] = False

        result = []
        for idx in range(len(s)):
            char = s[idx]
            char_map[char] -= 1
            if visit_char[char]:
                continue

            while len(result) > 0 and result[-1] > char and char_map[result[-1]] > 0:
                remove_char = result.pop()
                visit_char[remove_char] = False
            result.append(char)
            visit_char[char] = True

        return "".join(result)


if __name__ == "__main__":
    s = Solution()
    r = s.removeDuplicateLetters("bcabc")
    print(r)
    r = s.removeDuplicateLetters("dbcacbca")
    print(r)
