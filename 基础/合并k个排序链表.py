#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 合并k个排序链表.py 
@time: 2020/6/6 22:41 
"""

from heapq import heappush, heappop


class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        # write your code here
        heap = []

        for idx, l in enumerate(lists):
            if l is not None:
                heappush(heap, [l.val, idx])
                lists[idx] = l.next
        if len(heap) == 0:
            return None

        result = []
        while len(heap) is not 0:
            num, idx = heappop(heap)
            result.append(num)
            if lists[idx] != None:
                heappush(heap, [lists[idx].val, idx])
                lists[idx] = lists[idx].next

        nodes = [ListNode(num) for num in result]
        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]
        return nodes[0]


if __name__ == "__main__":
    s = Solution()
    num_lists = [[2, 4], [-1]]
    lists = []
    for num_list in num_lists:
        nodes = [ListNode(num) for num in num_list]
        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]
        lists.append(nodes[0])
    s.mergeKLists(lists)
