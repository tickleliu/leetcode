#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 整数排序 II.py
@time: 2020/06/17 10:29

描述
给一组整数，请将其在原地按照升序排序。使用归并排序，快速排序，堆排序或者任何其他 O(n log n) 的排序算法。

例1：

输入：[3,2,1,4,5]，
输出：[1,2,3,4,5]。

例2：

输入：[2,3,1]，
输出：[1,2,3]。
"""


class Solution:
    """
    @param A: an integer array
    @return: nothing
    """

    def sortIntegers2(self, A: list):
        # write your code here
        def partition(arr, low, high):
            i = (low - 1)  # 最小元素索引
            pivot = arr[high]

            for j in range(low, high):

                # 当前元素小于或等于 pivot
                if arr[j] <= pivot:
                    i = i + 1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return (i + 1)

        # arr[] --> 排序数组
        # low  --> 起始索引
        # high  --> 结束索引

        # 快速排序函数
        def quickSort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)

                quickSort(arr, low, pi - 1)
                quickSort(arr, pi + 1, high)

        quickSort(A, 0, len(A) - 1)
        return A


if __name__ == "__main__":
    s = Solution()
    r = s.sortIntegers2([3, 2, 1, 4, 5])
    print(r)
