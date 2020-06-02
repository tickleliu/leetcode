#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 1背包问题.py 
@time: 2020/6/1 20:57 
"""


def zero_one_package(capacity=5, weights=[2, 1, 3, 2], values=[12, 10, 20, 15]):
    if len(weights) == 0:
        return 0

    max_value = 0
    for idx in range(len(weights)):
        v1 = 0
        weights1 = weights[0:idx] + weights[idx + 1:]
        values1 = values[0:idx] + values[idx + 1:]
        if capacity - weights[idx] >= 0:
            v1 = zero_one_package(capacity - weights[idx], weights1, values1) + values[idx]
        v2 = zero_one_package(capacity, weights1, values1)

        v = max(v2, v1)
        if v > max_value:
            max_value = v

    return max_value


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


if __name__ == "__main__":
    r = zero_one_package_dp()
    print(r)
