#!/usr/bin/env python  
# encoding: utf-8  

"""
题目：有一个整形数组nums和一个大小为k的窗口，窗口从数组的最左边每次滑动一格直到最右边，返回每次窗口中的最大值。
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 窗口为K的最大子数组和.py 
@time: 2020/5/7 17:31 
"""

from collections import deque
from queue import PriorityQueue


def sliding_window_maximum_sum(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3):
    cur_sum = sum(nums[0:k])
    max_sum = cur_sum
    for i in range(k, len(nums)):
        cur_sum = cur_sum - nums[i - k] + nums[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


if __name__ == "__main__":
    print(sliding_window_maximum_sum())
