#!/usr/bin/env python  
# encoding: utf-8  

"""
3-sum问题：统计一个不重复数组中3个数相加为0的组合。
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 3sum.py 
@time: 2020/5/9 17:15 
"""


def three_sum(nums=[-6, 0, 1, 2, 3, 4, 5, 6, 8, 21], k=0):
    min_num = nums[0]
    max_num = nums[-1]
    bucket = [0] * (max_num - min_num + 1)
    res = []
    for num in nums:
        bucket[num - min_num] = 1

    for i in range(0, len(nums) - 1):
        for j in range(i, len(nums)):
            index_j = nums[j] - min_num
            sum = nums[i] + nums[j]
            if k - sum <= max_num and k - sum >= min_num:
                if bucket[k - sum - min_num] == 1 and k - sum - min_num > index_j:  # 如果缺失的数字存在并且在前两位后面
                    res.append([nums[i], nums[j], k - nums[i] - nums[j]])
    return res


def two_sum(nums=[-6, 0, 1, 2, 3, 4, 5, 6, 8, 21], k=20):
    left = 0
    right = len(nums) - 1
    temp = nums[left] + nums[right]
    is_break = False
    while temp > k:
        right -= 1
        if left >= right:
            right += 1
            break
        temp = nums[left] + nums[right]
    while temp < k:
        left += 1
        if left >= right:
            left -= 1
            break
        temp = nums[left] + nums[right]
    if temp == k:
        return [nums[left], nums[right]]

    return [nums[left], nums[right]]


if __name__ == "__main__":
    print(two_sum())
