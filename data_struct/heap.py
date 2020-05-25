#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: heap.py 
@time: 2020/5/24 10:50 
"""


class Heap():

    def __init__(self, reversed=False):
        super(Heap, self).__init__()
        self.nums = []
        self.reversed = reversed

    def push(self, num):
        child_idx = len(self.nums)
        self.nums.append(num)
        parent_idx = len(self.nums) // 2
        while child_idx != parent_idx:
            if (self.nums[parent_idx] > self.nums[child_idx] and self.reversed is False) \
                    or (self.nums[parent_idx] < self.nums[child_idx] and self.reversed is True):  # swap
                temp = self.nums[parent_idx]
                self.nums[parent_idx] = self.nums[child_idx]
                self.nums[child_idx] = temp
            child_idx = parent_idx
            parent_idx = parent_idx // 2

    def get(self):
        return self.nums[0]


if __name__ == "__main__":
    nums = [0, 3, 7, 1, 8, 6]
    h = Heap(reversed=True)
    for num in nums:
        h.push(num)
    print()
