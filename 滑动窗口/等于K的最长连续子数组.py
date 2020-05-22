#!/usr/bin/env python  
# encoding: utf-8  

"""
给定数组A = [1,1,3,2,1,0,2]，找出满足和小于等于5的最长连续子数组。
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 等于K的最长连续子数组.py 
@time: 2020/5/7 20:34 
"""


def sliding_window_maximum_length(nums=[1, 1, 3, 2, 1, 0, 2], k=3):
    right = 0
    max_len = 0
    sum = 0
    for left in range(0, len(nums)):
        while right < len(nums):
            if sum + nums[right] > k:
                sum = sum - nums[left]
                break
            else:
                sum += nums[right]
                right += 1
                if right - left > max_len:
                    max_len = right - left
    return max_len

if __name__ == "__main__":
    print(sliding_window_maximum_length())
