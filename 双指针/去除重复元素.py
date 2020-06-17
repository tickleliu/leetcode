#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 去除重复元素.py
@time: 2020/06/17 9:23

描述
中文
English
给一个整数数组，去除重复的元素。

你应该做这些事

1.在原数组上操作
2.将去除重复之后的元素放在数组的开头
3.返回去除重复元素之后的元素个数

输入:
nums = [1,3,1,4,4,2]
输出:
[1,3,4,2,?,?]
4

解释:
1. 将重复的整数移动到 nums 的尾部 => nums = [1,3,4,2,?,?].
2. 返回 nums 中唯一整数的数量  => 4.
事实上我们并不关心你把什么放在了 ? 处, 只关心没有重复整数的部分.

输入:
nums = [1,2,3]
输出:
[1,2,3]

3
"""


class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums: list):
        # write your code here
        if not nums:
            return 0
        nums.sort()
        left = 0
        right = 1
        while right <= len(nums) - 1:
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1

        return left + 1


if __name__ == "__main__":
    s = Solution()
    print(s.deduplication([1, 3, 1, 4, 4, 2]))
