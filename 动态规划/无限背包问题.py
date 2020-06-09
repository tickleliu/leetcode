#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 无限背包问题.py 
@time: 2020/6/6 15:42

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

不同顺序也算作不同的背包
"""

from copy import deepcopy


def combine(nums, k):
    result = []

    def dfs(temp, k):
        if k == 0:
            result.append(deepcopy(temp))
            return
        for num in nums:
            if num <= k:
                temp.append(num)
                dfs(temp, k - num)
                temp.pop()

    dfs([], k)
    return result


def combine_dp(nums, k):
    counts = (k + 1) * [0]
    counts[0] = 1
    for i in range(1, k + 1):
        for j in range(len(nums)):
            if i >= nums[j]:
                counts[i] += counts[i - nums[j]]
    return counts[-1]


if __name__ == "__main__":
    r = combine_dp([1, 2, 3], 4)
    print(r)
