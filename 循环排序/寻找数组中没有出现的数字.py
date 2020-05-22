#!/usr/bin/env python  
# encoding: utf-8  

"""
设一个数组里面的元素范围是1<=a[i]<=n(n是数组的size)，里面的元素只可能出现一次或两次，找到这个数组中没有出现的数字。例如：
输入为
[4,3,2,7,8,2,3,1]
输出为
[5,6]
@version: v1.0
@author: tickleliu
@contact: tickleliu@163.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 需要数组中没有出现的数字.py
@time: 2020/5/20 20:18
"""


def find_disapper_num(nums=[4, 3, 2, 7, 8, 2, 3, 1]):
    l, r = 0, len(nums)
    while l < r:
        if nums[l] != nums[nums[l] - 1]:
            """
            两种情况下判断成立：1 nums[l-1]=l，或者两个不同位置保存的数字相同
            """
            num_1 = nums[nums[l] - 1]
            nums[nums[l] - 1] = nums[l]
            nums[l] = num_1
        else:
            l += 1

    result = []
    for i, num in enumerate(nums):
        if num != i + 1:
            result.append(i + 1)

    return result


if __name__ == "__main__":
    print(find_disapper_num())
