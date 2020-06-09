#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最大子数组 II.py 
@time: 2020/6/7 17:41

给定一个整数数组，找出两个 不重叠 子数组使得它们的和最大。
每个子数组的数字在数组中的位置应该是连续的。
返回最大的和。

样例
例1:

输入:
[1, 3, -1, 2, -1, 2]
输出:
7
解释:
最大的子数组为 [1, 3] 和 [2, -1, 2] 或者 [1, 3, -1, 2] 和 [2].
例2:

输入:
[5,4]
输出:
9
解释:
最大的子数组为 [5] 和 [4].
挑战
要求时间复杂度为 O(n)
"""


class Solution:
    """
    @param: nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxTwoSubArrays(self, nums):
        # write your code here
        MAX_INT = 99999999

        max_local = len(nums) * [0]
        max_local[0] = nums[0]
        for idx in range(1, len(nums)):
            cur_num = nums[idx]
            if cur_num + max_local[idx - 1] > cur_num:
                max_local[idx] = cur_num + max_local[idx - 1]
            else:
                max_local[idx] = cur_num

        max_local2 = len(nums) * [0]
        max_local2[-1] = nums[-1]
        for idx in range(len(nums) - 2, -1, -1):
            cur_num = nums[idx]
            if cur_num + max_local2[idx + 1] > cur_num:
                max_local2[idx] = cur_num + max_local2[idx + 1]
            else:
                max_local2[idx] = cur_num
        max_value = -MAX_INT
        max_global = [0] * len(nums)
        for idx in range(len(max_local)):
            if max_local[idx] > max_value:
                max_value = max_local[idx]
            max_global[idx] = max_value

        max_value = -MAX_INT
        max_global2 = [0] * len(nums)
        for idx in range(len(nums) - 1, -1, -1):
            if max_local2[idx] > max_value:
                max_value = max_local2[idx]
            max_global2[idx] = max_value

        max_sum = -MAX_INT
        max_global = max_global[0:len(max_global) - 1]
        max_global2 = max_global2[1:len(max_global2)]
        for max_value, max_value2 in zip(max_global, max_global2):
            if max_sum < max_value + max_value2:
                max_sum = max_value + max_value2

        return max_sum



if __name__ == "__main__":
    nums = [-1, -2, -3, -100, -1, -50]
    s = Solution()
    r = s.maxTwoSubArrays(nums)
    print(r)
