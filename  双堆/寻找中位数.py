#!/usr/bin/env python  
# encoding: utf-8  

"""
数据流中的中位数
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 寻找中位数.py 
@time: 2020/5/24 10:18 
"""

from heapq import heappush, heappop


def find_median(nums=[5, 2, 4, 3, 1, 0, 6]):
    big = []  # 小顶堆，存放较大的元素
    little = []  # 大顶堆，存放较小的元素
    for num in nums:
        if len(big) < len(nums) // 2:
            heappush(big, num)
        else:
            if big[0] < num:
                temp_num = heappop(big)
                heappush(big, num)
                heappush(little, -temp_num)
            else:
                heappush(little, -num)

    if len(nums) % 2 == 0:
        median = (big[0] - little[0]) / 2
    else:
        median = -little[0]

    return median


if __name__ == "__main__":
    median = find_median()
    print(median)
