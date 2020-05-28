#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 合并k个排序好的数组.py 
@time: 2020/5/28 10:00 
"""

from queue import PriorityQueue


def merge(num_lists):
    heap = PriorityQueue(len(num_lists))
    for idx, nums in enumerate(num_lists):
        num = nums.pop()
        heap.put([num, idx])
    result = []
    while not heap.empty():
        num, idx = heap.get()
        result.append(num)
        if len(num_lists[idx]) != 0:
            num = num_lists[idx].pop()
            heap.put([num, idx])
    result.reverse()
    return result


if __name__ == "__main__":
    num_lists = [[21, 12, 11, 10, 1],
                 [22, 17, 16, 7, 2],
                 [23, 18, 13, 8, 3],
                 [24, 19, 14, 9, 4],
                 [25, 20, 15, 6, 5]]

    r = merge(num_lists)
    print(r)
