#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最大连续子数组乘机.py 
@time: 2020/6/7 8:51 
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    MAX_INT = 999999

    def maxProduct(self, nums):
        max_pre = nums[0]
        min_pre = nums[0]
        result = max_pre
        for idx in range(1, len(nums)):
            num = nums[idx]
            temp_max_pre = max(num, max_pre * num, min_pre * num)
            temp_min_pre = min(num, max_pre * num, min_pre * num)
            max_pre = temp_max_pre
            min_pre = temp_min_pre
            if max_pre > result:
                result = max_pre
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.maxProduct([-4, -3, -2])
    print(r)
