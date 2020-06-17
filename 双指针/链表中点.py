#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 链表中点.py
@time: 2020/06/16 17:18
"""

"""
Definition of ListNode
"""


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here
        if not head:
            return None
        p, q = head, head

        while q.next is not None and q.next.next is not None:
            p = p.next
            q = q.next.next

        return p


if __name__ == "__main__":
    nums = [0, 1, 2]
    nodes = [ListNode(num) for num in nums]
    head = nodes[0]
    for id in range(1, len(nodes)):
        node_pre = nodes[id - 1]
        node_cur = nodes[id]
        node_pre.next = node_cur

    s = Solution()
    r = s.middleNode(head)
    print(r)
