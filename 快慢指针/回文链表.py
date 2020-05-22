#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 回文链表.py 
@time: 2020/5/12 20:45 
"""
import sys

sys.path.append("快慢指针")
from chain import Node


def rever_chain(head, pre):
    if head is None:
        return pre
    tmp = head.next
    head.next = pre
    pre = head
    head = tmp
    return rever_chain(head, pre)


def palindrome(head):
    fast = head
    slow = head
    while True:
        if fast is None or fast.next is None:
            break
        else:
            slow = slow.next
            fast = fast.next.next
    temp_head = slow
    temp_head = rever_chain(temp_head, None)

    while temp_head is not None and head is not None:
        if temp_head.data == head.data:
            temp_head = temp_head.next
            head = head.next
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 1, 0]
    nodes = [Node(num) for num in nums]
    head = nodes[0]
    for id in range(1, len(nodes)):
        node_pre = nodes[id - 1]
        node_cur = nodes[id]
        node_pre.next = node_cur

    print(palindrome(head))
