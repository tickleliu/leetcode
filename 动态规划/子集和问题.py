#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 子集和问题.py 
@time: 2020/6/1 21:58 
"""

from copy import deepcopy


def zero_one_package_dp(capacity=5, weights=[2, 1, 3, 2], values=[12, 10, 20, 15]):
    value_matrix = []
    path_matrix = []
    for i in range(capacity + 1):
        value_matrix.append([])
        path_matrix.append([])
        for j in range(len(weights)):
            value_matrix[i].append(0)
            path_matrix[i].append([])
        if i >= weights[0]:
            value_matrix[i][0] = values[0]
            path_matrix[i][0].append(0)

    for i in range(1, capacity + 1):
        for j in range(1, len(weights)):
            v1 = value_matrix[i][j - 1]
            idx = i - weights[j]
            if idx < 0:
                v2 = 0
            else:
                v2 = value_matrix[idx][j - 1] + values[j]
            value_matrix[i][j] = max(v2, v1)
            if v2 == 0:
                pass
            elif value_matrix[i][j] == v1:
                path_matrix[i][j] = deepcopy(path_matrix[i][j - 1])
            else:
                path_matrix[i][j] = deepcopy(path_matrix[idx][j - 1])
                path_matrix[i][j].append(j)

    return path_matrix[-1][-1]


def sub_sum(nums=[1, 2, 3, 4, 5], sum_result=10):
    return zero_one_package_dp(sum_result, nums, nums)


if __name__ == "__main__":
    print(sub_sum())
