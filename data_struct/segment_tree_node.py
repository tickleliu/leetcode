#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: segment.py 
@time: 2020/6/28 17:41 
"""


class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
        self.data = None

    def build(self, start, end):
        self.help(self, start, end)

    def help(self, root, start, end):
        if start >= end:
            return
        l_start = start
        l_end = (start + end) // 2
        r_start = l_end + 1
        r_end = end
        root.left = SegmentTreeNode(l_start, l_end)
        root.right = SegmentTreeNode(r_start, r_end)
        self.help(root.left, l_start, l_end)
        self.help(root.right, r_start, r_end)
        return




if __name__ == "__main__":
    root = SegmentTreeNode(0, 7)
    root.build(0, 7)
    nums = [5, 2, 3, 4, 1, 6, 7, 0]
    root.modify(root, nums)
    print(root)
