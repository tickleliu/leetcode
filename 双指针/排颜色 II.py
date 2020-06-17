#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 排颜色 II.py
@time: 2020/06/17 17:38

描述
给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。

样例
样例1

输入:
[3,2,2,1,4]
4
输出:
[1,2,2,3,4]
样例2

输入:
[2,1,1,2,2]
2
输出:
[1,1,2,2,2]
"""


class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """

    def sortColors2(self, colors, k):
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

        quickSort(colors, 0, len(colors) - 1)
        return colors

    def sortColors2_(self, nums, target):
        # dual pointer


        return nums


if __name__ == "__main__":
    s = Solution()
    r = s.sortColors2_([3, 2, 2, 1, 4], 4)
    print(r)
