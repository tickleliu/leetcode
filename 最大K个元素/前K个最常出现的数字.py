#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 前K个最常出现的数字.py 
@time: 2020/5/27 9:22 
"""

from queue import PriorityQueue


def find_topk_freq(nums=[5, 3, 3, 1, 2, 2, 6], k=2):
    freq = {}
    for num in nums:
        count = freq.get(num, 0)
        freq[num] = count + 1
    heap = PriorityQueue(maxsize=k)
    for num, count in freq.items():
        if not heap.full():
            heap.put([count, num])
        else:
            head_count, head_num = heap.get()
            if head_count < count:
                heap.put([count, num])
            else:
                heap.put([head_count, head_num])
    return heap

if __name__ == "__main__":
    print(find_topk_freq())
