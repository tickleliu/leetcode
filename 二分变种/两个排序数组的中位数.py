#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 两个排序数组的中位数.py 
@time: 2020/6/28 11:23

两个排序的数组A和B分别含有m和n个数，找到两个排序数组的中位数，要求时间复杂度应为O(log (m+n))。

样例
样例1

输入:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
输出: 3.5
样例2

输入:
A = [1,2,3]
B = [4,5]
输出: 3
挑战
时间复杂度为O(log n)

说明
中位数的定义：

这里的中位数等同于数学定义里的中位数。
中位数是排序后数组的中间值。
如果有数组中有n个数且n是奇数，则中位数为A[(n-1)/2]A[(n−1)/2]。

"""


class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, num1, num2):
        # write your code here
        num_length = len(num1) + len(num2)

        if num_length % 2 == 1:
            return self.findTopK(num1, 0, num2, 0, num_length // 2 + 1)
        else:
            return (self.findTopK(num1, 0, num2, 0, num_length // 2 + 1) + self.findTopK(num1, 0, num2, 0,
                                                                                         num_length // 2)) / 2

    def findTopK(self, A, AStart, B, BStart, k):
        MAX_INTEGER = 9999
        if k == 1:
            return min(A[AStart], B[BStart])
        if AStart >= len(A):
            return B[k - 1]
        if BStart >= len(B):
            return A[k - 1]
        a = A[AStart + k // 2 - 1] if AStart + k // 2 - 1 <= len(A) - 1 else MAX_INTEGER
        b = B[BStart + k // 2 - 1] if BStart + k // 2 - 1 <= len(B) - 1 else MAX_INTEGER

        if a > b:
            return self.findTopK(A, AStart, B, BStart + k // 2, k - k // 2)
        else:
            return self.findTopK(A, AStart + k // 2, B, BStart, k - k // 2)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    B = [2, 3, 4, 5]

    s = Solution()
    print(s.findMedianSortedArrays(A, B))
