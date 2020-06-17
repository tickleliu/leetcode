#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 两数和 II-输入已排序的数组.py
@time: 2020/06/17 17:33

English
给定一个已经 按升序排列 的数组，找到两个数使他们加起来的和等于特定数。
函数应该返回这两个数的下标，index1必须小于index2。注意返回的值不是 0-based。

样例
例1:

输入: nums = [2, 7, 11, 15], target = 9
输出: [1, 2]
例2:

输入: nums = [2,3], target = 5
输出: [1, 2]

"""


class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))

    s = Solution()
    print(s.twoSum([2, 3], 5))
