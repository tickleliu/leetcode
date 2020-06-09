#!/usr/bin/env python
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 最长上升子序列.py 
@time: 2020/6/7 9:49

样例 1:
	输入:  [5,4,1,2,3]
	输出:  3

	解释:
	LIS 是 [1,2,3]


样例 2:
	输入: [4,2,4,5,3,7]
	输出:  4

	解释:
	LIS 是 [2,4,5,7]

"""


class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if len(nums) == 0:
            return 0
        cur_max_length = [0] * len(nums)
        cur_max_length[0] = 1
        result = 1
        for idx in range(1, len(nums)):
            max_length = 1
            for jdx in range(idx - 1, -1, -1):
                if nums[idx] >= nums[jdx]:
                    if cur_max_length[jdx] + 1 > max_length:
                        max_length = cur_max_length[jdx] + 1
            cur_max_length[idx] = max_length
            if max_length > result:
                result = max_length
        return result


if __name__ == "__main__":
    s = Solution()
    r = s.longestIncreasingSubsequence([4, 2, 4, 5, 3, 7])
    print(r)
