#!/usr/bin/env python
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 二分查找.py 
@time: 2020/5/26 8:58 
"""


def search(nums=[0, 1, 2, 3, 4, 5, 6], k=5):
    left = 0
    right = len(nums) - 1
    result = None
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == k:
            result = mid
            break
        elif nums[mid] < k:
            left = mid + 1
        elif nums[mid] > k:
            right = mid - 1

    return result


if __name__ == "__main__":
    print(search())
