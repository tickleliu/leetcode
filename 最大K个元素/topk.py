#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: topk.py
@time: 2020/06/02 18:11
"""

import random


def find_topk(nums=[5, 1, 4, 3, 2], k=3):
    def _help(nums, s, e, k):
        use_idx = random.randint(s, e)

        temp = nums[s]
        nums[s] = nums[use_idx]
        nums[use_idx] = temp

        use_idx = partitions(nums, s, e)

        if use_idx == k:
            return
        elif use_idx < k:
            _help(nums, use_idx, e, k)
        else:
            _help(nums, s, use_idx, k)

    _help(nums, 0, len(nums) - 1, k)
    return nums


def partion(array, low, high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low


if __name__ == "__main__":
    # r = find_topk()
    # print(r)
    nums = [3, 1, 2, 4, 5]
    partion(nums, 0, len(nums) - 1)
