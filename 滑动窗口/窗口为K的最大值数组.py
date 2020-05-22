#!/usr/bin/env python  
# encoding: utf-8  

"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内的数字。滑动窗口每次只向右移动一位。
返回滑动窗口最大值
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 窗口为K的最大值数组.py 
@time: 2020/5/7 18:08 
"""

from queue import PriorityQueue


class Num(object):
    def __init__(self, priority, id):
        self.priority = priority
        self.id = id

    def __lt__(self, other):
        return self.priority < other.priority


def sliding_window_maximum(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3):
    """
    队列头部元素是最大的，剩余元素全部位于最大元素的右侧
    例如：合法的，【3， -3， -1】，不合法的【3，1（1位于3左边），-1】
    """
    res = []
    heap = PriorityQueue(maxsize=k)
    res.append(nums[0])
    nums = [-1 * n for n in nums]
    heap.put(nums[0])
    for i in range(1, len(nums)):
        cur_min = heap.get()
        cur_num = nums[i]
        if cur_num < cur_min:
            heap = PriorityQueue(maxsize=k)
            heap.put(cur_num)
        else:
            heap.put(cur_num)
            if not heap.full():
                heap.put(cur_min)

        # save result
        cur_res = heap.get()
        res.append(-cur_res)
        heap.put(cur_res)

    return res


if __name__ == "__main__":
    print(sliding_window_maximum())
