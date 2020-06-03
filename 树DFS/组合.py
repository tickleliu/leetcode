#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 组合.py
@time: 2020/06/03 16:22
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

"""


# def combine(n, k):
#     nums = list(range(1, n + 1))
#     result = [[]]
#     for num in nums:
#         cur_set_length = len(result)
#         for sub_set_idx in range(cur_set_length):
#             if len(cur_sub_set) < k:
#                 cur_sub_set = deepcopy(result[sub_set_idx])
#                 cur_sub_set.append(num)
#                 result.append(cur_sub_set)
#     k_result = []
#     for sub_set in result:
#         if len(sub_set) == k:
#             k_result.append(sub_set)
#     return k_result


def combine(n, k):
    if k > n or k == 0:
        return []
    if k == 1:
        return [[i] for i in range(1, n + 1)]
    if k == n:
        return [[i for i in range(1, n + 1)]]
    answer = combine(n - 1, k)
    for item in combine(n - 1, k - 1):
        item.append(n)
        answer.append(item)
    return answer


from copy import deepcopy


class Solution:
    def combine(self, n, k):
        result = []

        def dfs(temp, n, k, idx):
            if len(temp) == k:
                result.append(deepcopy(temp))
            else:
                for i in range(idx, n):
                    temp.append(i)
                    dfs(temp, n, k, i + 1)
                    temp.pop()

        dfs([], n + 1, k, 1)
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.combine(4, 2)
    print(r)
