#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 旋转数组.py
@time: 2020/06/08 15:50

旋转数组定义：4,5,6,7,8,1,2,3
"""


class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]


if __name__ == "__main__":
    # r = rotate_array_bin_search([1, 2, 3, 4, 5, 6, 7])
    s = Solution()
    r = s.findMin([7, 8, 9, 4, 5])
    print(r)
