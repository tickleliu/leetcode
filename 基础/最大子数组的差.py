#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最大子数组的差.py 
@time: 2020/6/7 16:26 
"""

import math


class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two substrings
    """

    def maxDiffSubArrays(self, nums):
        # write your code here
        MAX_INT = 99999999

        def help(nums):
            max_local = len(nums) * [0]
            max_local[0] = nums[0]
            for idx in range(1, len(nums)):
                cur_num = nums[idx]
                if cur_num + max_local[idx - 1] > cur_num:
                    max_local[idx] = cur_num + max_local[idx - 1]
                else:
                    max_local[idx] = cur_num

            min_local = len(nums) * [0]
            min_local[-1] = nums[-1]
            for idx in range(len(nums) - 2, -1, -1):
                cur_num = nums[idx]
                if cur_num + min_local[idx + 1] < cur_num:
                    min_local[idx] = cur_num + min_local[idx + 1]
                else:
                    min_local[idx] = cur_num
            max_value = -MAX_INT
            max_global = [0] * len(nums)
            for idx in range(len(max_local)):
                if max_local[idx] > max_value:
                    max_value = max_local[idx]
                max_global[idx] = max_value
            min_value = MAX_INT
            min_global = [0] * len(nums)
            for idx in range(len(nums) - 1, -1, -1):
                if min_local[idx] < min_value:
                    min_value = min_local[idx]
                min_global[idx] = min_value

            max_diff = 0
            max_global = max_global[0:len(max_global) - 1]
            min_global = min_global[1:len(min_global)]
            for max_value, min_value in zip(max_global, min_global):
                if max_diff < math.fabs(max_value - min_value):
                    max_diff = math.fabs(max_value - min_value)

            return int(max_diff)

        max1 = help(nums)
        nums.reverse()
        max2 = help(nums)
        return max(max1, max2)


if __name__ == "__main__":
    nums = [-5, -4]
    s = Solution()
    r = s.maxDiffSubArrays(nums)
    print(r)
