#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 滑动窗口中位数.py 
@time: 2020/5/24 11:18
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.
"""

from heapq import heappush, heappop, heapreplace


def find_median(nums):
    big = []  # 小顶堆，存放较大的元素
    little = []  # 大顶堆，存放较小的元素
    for num in nums:
        if len(big) < len(nums) // 2:
            heappush(big, num)
        else:
            if big[0] < num:
                temp_num = heappop(big)
                heappush(big, num)
                heappush(little, -temp_num)
            else:
                heappush(little, -num)

    if len(nums) % 2 == 0:
        median = (big[0] - little[0]) / 2
    else:
        median = -little[0]

    return median


def sliding_window_find_median(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3):
    medians = []

    for i in range(0, len(nums) - k + 1):
        medians.append(find_median(nums[i:i + k]))

    return medians


if __name__ == "__main__":
    medians = sliding_window_find_median()
    print(medians)
