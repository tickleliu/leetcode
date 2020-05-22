#!/usr/bin/env python  
# encoding: utf-8  

"""
问题描述：
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数,这个重复数字可能出现不止一次，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:

输入: [3,1,3,4,2]
输出: 3
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 寻找重复的数字.py 
@time: 2020/5/20 20:09 
"""


def find_duplicate(nums=[4, 3, 5, 2, 8, 2, 2, 1]):
    l, r = 0, len(nums) - 1
    while l <= r:
        a = nums[l]
        b = nums[nums[l] - 1]
        if nums[l] != nums[nums[l] - 1]:
            nums[nums[l] - 1], nums[l] = nums[l], nums[nums[l] - 1]
        else:
            l += 1
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return nums[i]


def find_duplicate2(nums=[1, 3, 4, 2, 2]):
    '''
    duplicate once
    '''
    sum_num = 0
    max_num = 0
    for num in nums:
        if num > max_num:
            max_num = num
        sum_num += num

    return int(sum_num - (1 + max_num) * max_num / 2)


if __name__ == "__main__":
    print(find_duplicate())
    print(find_duplicate([3, 1, 3, 4, 2]))

    print(find_duplicate2())
    print(find_duplicate2([3, 1, 3, 4, 2]))
