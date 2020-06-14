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


class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here
        def _help(nums, s, e, k):
            if s >= e:
                return nums[s]
            use_idx = random.randint(s, e)

            temp = nums[s]
            nums[s] = nums[use_idx]
            nums[use_idx] = temp

            use_idx = self.partitions(nums, s, e)

            if use_idx == k - 1:
                return nums[use_idx]
            elif use_idx > k:
                _help(nums, use_idx + 1, e, k)
            else:
                _help(nums, s, use_idx - 1, k)

        result = _help(nums, 0, len(nums) - 1, n)
        return nums[n - 1]

    def partitions(self, array, low, high):
        key = array[low]
        while low < high:
            while low < high and array[high] <= key:
                high -= 1
            if low < high:
                array[low] = array[high]

            while low < high and array[low] > key:
                low += 1
            if low < high:
                array[high] = array[low]

        array[low] = key
        return low


if __name__ == "__main__":
    # r = find_topk()
    # print(r)
    nums = [3, 1, 2, 4, 5]
    s = Solution()
    r = s.kthLargestElement(2, [1, 3, 4, 2])
    print(r)
