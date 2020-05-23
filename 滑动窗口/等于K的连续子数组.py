#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 等于K的连续子数组.py 
@time: 2020/5/23 18:27

给定数组A = [1,-1,3,2,1,0,2]，找出满足和等于5的连续子数组, 数组中允许出现负数。
"""


def sliding_window_sum_k(nums=[1, -1, 3, 2, 1, 0, 2], k=3):
    prefix_sum = {0: [0]}
    prefix_sum_list = [0]
    cur_sum = 0
    result = []

    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum not in prefix_sum:
            prefix_sum[cur_sum] = []
        prefix_sum[cur_sum].append(i + 1)
        prefix_sum_list.append(cur_sum)

    for j in range(0, len(nums)):
        if prefix_sum_list[j + 1] - k in prefix_sum:
            for v in prefix_sum[prefix_sum_list[j + 1] - k]:
                if v <= j:
                    result.append([v, j])
                else:
                    break

    return result


if __name__ == "__main__":
    r = sliding_window_sum_k()
    print(r)
