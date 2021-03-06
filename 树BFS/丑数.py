#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 丑数.py
@time: 2020/06/03 17:07
"""



from heapq import heappush, heappop
class Solution(object):
    def nth_ugly_number(self, n):
        nums = [2, 3, 5]
        result = []
        heap = []
        heappush(heap, [1, 0])

        while len(result) < n:
            temp, idx = heappop(heap)
            result.append(temp)
            for i in range(idx, 3):
                heappush(heap, [nums[i] * temp, i])
        return result[-1]


if __name__ == "__main__":
    s = Solution()
    r = s.nth_ugly_number(10)
    print(r)
