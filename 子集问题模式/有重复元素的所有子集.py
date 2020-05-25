#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 有重复元素的所有子集.py 
@time: 2020/5/25 16:40 
"""

from copy import deepcopy


def power_set(nums=[1, 2, 3, 3]):
    result_set = [[]]
    pre_num = None
    for num in nums:
        count = 0
        total_set = len(result_set)
        while count < total_set:
            sub_set = result_set[count]
            count += 1

            if pre_num == num and ((len(sub_set) >= 1 and sub_set[-1] != pre_num) or (len(sub_set)==0)):  # 如果添加的元素和上面的不重合
                continue

            sub_set = deepcopy(sub_set)
            sub_set.append(num)
            result_set.append(sub_set)
        pre_num = num
    return result_set


if __name__ == "__main__":
    result_set = power_set()
    print(result_set)
