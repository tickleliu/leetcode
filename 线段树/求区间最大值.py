#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 求区间最大值.py 
@time: 2020/6/28 20:56 
"""

from data_struct.segment_tree_node import SegmentTreeNode


class Solution:
    """
    @param a: the given number
    @param b: another number
    @return: the greatest common divisor of two numbers
    """

    def query_max(self, nums, start, end):
        root = SegmentTreeNode(0, len(nums) - 1)
        root.build(0, len(nums) - 1)
        self.modify(root, nums)
        r = self.query_helper(root, start, end)
        return r

    def modify(self, root, nums):
        if root == None:
            return self.MAX_NEG_INTEGER
        if root.end == root.start:
            root.data = nums[root.start]
            return nums[root.start]
        root.data = max(self.modify(root.left, nums), self.modify(root.right, nums))
        return root.data

    def query_helper(self, root, start, end):
        if root.start == root.end:
            return root.data
        if root.start >= start and root.end <= end:
            return root.data
        l_end = (root.start + root.end) // 2
        if start < l_end < end:
            l_data = self.query_helper(root.left, start, l_end)
            r_data = self.query_helper(root.right, l_end + 1, end)
            return max(l_data, r_data)
        elif l_end >= end:
            return self.query_helper(root.left, start, end)
        elif start >= l_end:
            return self.query_helper(root.right, start, end)


if __name__ == "__main__":
    s = Solution()
    nums = [5, 2, 3, 4, 1, 6, 7, 0]
    r = s.query_max(nums, 0, 3)
    print(r)
