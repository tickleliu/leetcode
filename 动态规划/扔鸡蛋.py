#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 扔鸡蛋.py
@time: 2020/06/10 11:31
"""


class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def dropEggs2(self, n):
        # write your code here
        # for a in range(0, n):
        #     for k in range(0, n):
        #         if ((k + 1) * a - k * (k + 1) / 2) <= n and ((k + 2) * a - (k + 1) * (k + 2) / 2) >= n:
        #             return a
        for x in range(0, n):
            if x * (x + 1) / 2 >= n:
                return x

    def dropEggs(self, n, k):
        # write your code here
        MAX_INT = 99999
        memo = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            memo[i][1] = i
        for i in range(k + 1):
            memo[0][i] = 0
            memo[1][i] = 1

        for i in range(2, n + 1):
            for j in range(2, k + 1):
                memo[i][j] = MAX_INT
                for t in range(1, i):
                    tmp = max(memo[t - 1][j - 1] + 1, memo[i - t][j] + 1)
                    memo[i][j] = min(tmp, memo[i][j])

        return memo[n][k]


if __name__ == "__main__":
    s = Solution()
    r = s.dropEggs2(100)
    print(r)

    r = s.dropEggs(10000007, 2)
    print(r)
