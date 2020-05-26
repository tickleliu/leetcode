#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 统计排序数组数字出现次数.py 
@time: 2020/5/26 9:09 
"""


def search_left(nums, k):
    # 寻找最左侧等于k的序号
    # 当mid==k时，调整右侧指针，指向mid-1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < k:
            left = mid + 1
        elif nums[mid] >= k:
            right = mid - 1

    return left


def search_right(nums, k=3):
    # 寻找最右侧等于k的序号
    # 当mid==k时，调整左侧指针，指向mid-1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] <= k:
            left = mid + 1
        elif nums[mid] > k:
            right = mid - 1

    return right


def count_sorted_list_k(nums, k):
    left = search_left(nums, k)
    right = search_right(nums, k)
    print(left, right)


if __name__ == "__main__":
    count_sorted_list_k(nums=[0, 1, 2, 3, 3, 3, 5], k=3)
