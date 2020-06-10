#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 寻找第k大的数.py 
@time: 2020/6/2 21:49 
"""


def topk(nums=[7, 9, 5, 1, 6, 3, 4, 2], k=3):
    s = 0
    e = len(nums)
    r = partition(nums, s, e)
    while r != k:
        if r < k:
            r = partition(nums, r + 1, e)
        else:
            r = partition(nums, s, r)
    return nums


def partition(nums, s, e):
    if s == e:
        return s
    pivot = nums[s]
    l = s
    r = e
    while l < r:
        while l < r:
            r = r - 1
            if nums[r] >= pivot:
                pass
            else:
                nums[l] = nums[r]
                break

        while l < r:
            l = l + 1
            if nums[l] <= pivot:
                pass
            else:
                nums[r] = nums[l]
                break

    nums[r] = pivot
    return r


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here

        A.extend(B)
        A = sorted(A)
        median = len(A)
        if median % 2 == 0:
            median_indexs = median // 2 - 1, median // 2
        else:
            median_indexs = median // 2, median // 2

        return (A[median_indexs[0]] + A[median_indexs[1]]) / 2


if __name__ == "__main__":
    s = Solution()
    r = s.findMedianSortedArrays([1, 2, 3, 4, 5, 6], [2, 3, 4, 5])
    print(r)
