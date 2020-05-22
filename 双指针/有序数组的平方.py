#!/usr/bin/env python  
# encoding: utf-8  

"""
题目描述：

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 有序数组的平方.py 
@time: 2020/5/9 16:41 
"""
import math


def sorted_squares(nums=[-4, -1, 0, 3, 10]):
    left = 0
    right = len(nums) - 1
    res = []
    if nums[0] * nums[-1] >= 0:
        if nums[0] < 0:
            left = len(nums) - 1
            right = len(nums)
        if nums[0] >= 0:
            left = -1
            right = 0

    else:
        for i in range(len(nums) - 1):
            if nums[i] * nums[i + 1] <= 0:
                left = i
                right = i + 1
                break

    while left >= 0 and right < len(nums):
        power_left = math.pow(nums[left], 2)
        power_right = math.pow(nums[right], 2)
        if power_left <= power_right:
            res.append(power_left)
            left -= 1
        else:
            res.append(power_right)
            right += 1
    assert left < 0 or right == len(nums)
    while left >= 0:
        power_left = math.pow(nums[left], 2)
        res.append(power_left)
        left -= 1
    while right < len(nums):
        power_right = math.pow(nums[right], 2)
        res.append(power_right)
        right += 1

    return res


def sorted_squares2(nums=[-4, -1, 0, 3, 10]):
    """
    取平方后，最小的一定是0，最大的可能位于两端某一个位置，因此无论原数组顺序，都应该按照降序优先输出平方结果
    """
    left = 0
    right = len(nums) - 1
    res = []
    while right >= left:
        power_left = math.pow(nums[left], 2)
        power_right = math.pow(nums[right], 2)
        if power_left >= power_right:
            res.append(power_left)
            left += 1
        else:
            res.append(power_right)
            right -= 1
    res.reverse()
    return res


if __name__ == "__main__":
    print(sorted_squares())
    print(sorted_squares(nums=[-7, -3, 2, 3, 11]))
    print(sorted_squares(nums=[-7, -3, -2]))
    print(sorted_squares(nums=[2, 3, 5]))

    print(sorted_squares2())
    print(sorted_squares2(nums=[-7, -3, 2, 3, 11]))
    print(sorted_squares2(nums=[-7, -3, -2]))
    print(sorted_squares2(nums=[2, 3, 5]))
