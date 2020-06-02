#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 相等子集和.py 
@time: 2020/6/1 21:48 
"""


def zero_one_package_dp(capacity=5, weights=[2, 1, 3, 2], values=[12, 10, 20, 15]):
    value_matrix = []
    for i in range(capacity + 1):
        value_matrix.append([])
        for j in range(len(weights)):
            value_matrix[i].append(0)
        if i >= weights[0]:
            value_matrix[i][0] = values[0]

    for i in range(1, capacity + 1):
        for j in range(1, len(weights)):
            v1 = value_matrix[i][j - 1]
            idx = i - weights[j]
            if idx < 0:
                v2 = 0
            else:
                v2 = value_matrix[idx][j - 1] + values[j]
            value_matrix[i][j] = max(v2, v1)

    return value_matrix[-1][-1]


def split_sub_equal_set(nums=[1, 5, 11, 5]):
    sum_nums = sum(nums)
    if sum_nums % 2 != 0:
        return False

    result = zero_one_package_dp(sum_nums // 2, nums, nums)

    if result == sum_nums // 2:
        return True
    else:
        return False


if __name__ == "__main__":
    r = split_sub_equal_set()
    print(r)
