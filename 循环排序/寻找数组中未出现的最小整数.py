#!/usr/bin/env python  
# encoding: utf-8  

"""
给定一个无序整型数组arr,找到数组中未出现的最小整数 。要求时间复杂度为O(N)空间复杂度为O(1)。
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 寻找数组中未出现的最小整数.py 
@time: 2020/5/20 21:18 
"""


def find_disappear_min_num(nums=[1, 4, 2, 3]):
    """
    思路：将数字表达为从0开始，那么缺失的最小数字一定位于0~len(nums)之间，
    若缺失的数字在0~len(nums)之外，那么nums数字必须连续，则答案为最大num+1
    将凡是超出在len（nums）中的元素修改为0，那么原始问题变为寻找0~len（nums）中的缺失元素,可以使用
    """
    min_num = 1000
    for i in range(len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]

    for i in range(len(nums)):
        nums[i] = nums[i] - min_num
        if nums[i] >= len(nums):
            nums[i] = 0

    l, r = 0, len(nums)

    while l < r:
        if nums[l] != nums[nums[l]]:
            nums[nums[l]], nums[l] = nums[l], nums[nums[l]]
        else:
            l = l + 1
    result = []
    for i, num in enumerate(nums):
        if i == 0:  # 第一个数肯定有
            continue
        if i != num:
            result.append(i + min_num)
    if len(result) == 0:
        return len(nums) + min_num
    return result


def find_disappear_max_num(nums=[1, 4, 2]):
    """
    按照上述思路，也可以处理最大缺失值，方法是将数字取相反数,转化为上述问题
    """
    for i in range(len(nums)):
        nums[i] = -nums[i]
    min_num = 1000
    max_num = 0
    for i in range(len(nums)):
        if nums[i] < min_num:
            min_num = nums[i]
        if nums[i] > max_num:
            max_num = nums[i]

    for i in range(len(nums)):
        nums[i] = nums[i] - min_num
        if nums[i] >= len(nums):
            nums[i] = 0

    l, r = 0, len(nums)

    while l < r:
        if nums[l] != nums[nums[l]]:
            nums[nums[l]], nums[l] = nums[l], nums[nums[l]]
        else:
            l = l + 1
    result = []
    for i, num in enumerate(nums):
        if i == 0:  # 第一个数肯定有
            continue
        if i != num:
            result.append(-(i + min_num))
    if len(result) == 0:
        return max_num - 1
    return result


if __name__ == "__main__":
    print(find_disappear_min_num())
    print(find_disappear_max_num())
