#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 前K大的数.py 
@time: 2020/5/27 9:08 
"""
from heapq import heappush, heappop


def find_topk(nums=[5, 3, 7, 1, 4, 2, 6], k=5):
    heap = []
    for num in nums:
        if len(heap) < k:
            heappush(heap, num)
        else:
            if heap[0] < num:
                heappop(heap)
                heappush(heap, num)
    return heap[0]


if __name__ == "__main__":
    print(find_topk())
