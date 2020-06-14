#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 山峰.py 
@time: 2020/6/14 10:51 
"""


class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """

    def mountainSequence(self, nums):
        # write your code here
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            left, right = mid - 1, mid + 1

            if left < 0:
                break

            if right > len(nums) - 1:
                break

            if nums[mid] > nums[left] and nums[mid] > nums[right]:
                return nums[mid]

            if nums[mid] >= nums[left] and nums[mid] <= nums[right]:
                start = mid

            else:
                end = mid

        if nums[end] > nums[start]:
            return nums[end]
        else:
            return nums[start]


if __name__ == "__main__":
    s = Solution()
    r = s.mountainSequence(nums=[1, 2, 4, 8, 6, 3])
    print(r)

    r = s.mountainSequence(nums=[10, 9, 8, 7])
    print(r)
