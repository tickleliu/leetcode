#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 移动零.py
@time: 2020/06/16 17:39

描述
给一个数组 nums 写一个函数将 0 移动到数组的最后面，非零元素保持原数组的顺序
输入: nums = [0, 1, 0, 3, 12],
输出: [1, 3, 12, 0, 0].

输入: nums = [0, 0, 0, 3, 1],
输出: [3, 1, 0, 0, 0].
"""


class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """

    def moveZeroes(self, nums):
        # write your code here
        if not nums:
            return nums
        if len(nums) == 1:
            return nums
        left, right = 0, 0
        while right <= len(nums) - 1 and left <= len(nums) - 1:
            while left <= len(nums) - 1:
                if nums[left] == 0:
                    break
                else:
                    left = left + 1

            if right <= left:
                right = left + 1
            while right <= len(nums) - 1:
                if nums[right] != 0:
                    break
                else:
                    right = right + 1

            if right <= len(nums) - 1 and left <= len(nums) - 1 and nums[left] == 0 and nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]

            left += 1
            right += 1

        return nums


if __name__ == "__main__":
    s = Solution()
    nums = s.moveZeroes([0, 1, 0, 3, 12])
    print(nums)

    nums = s.moveZeroes([0, 0, 0, 3, 1])
    print(nums)

    nums = s.moveZeroes([0, 1])
    print(nums)

    nums = s.moveZeroes([0, 0])
    print(nums)

    nums = s.moveZeroes([-1, 2, -3, 0, 4, 0, 1, 0, 0, -2, 1])
    print(nums)
