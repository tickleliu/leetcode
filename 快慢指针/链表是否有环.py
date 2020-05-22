#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 链表是否有环.py 
@time: 2020/5/12 19:49 
"""
import sys

sys.path.append("快慢指针")
from chain import Node


def loop_chain(chain: Node):
    """
    判断链表是否存在环
    """
    slow = chain
    fast = chain

    while True:
        if slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        else:
            return False


def loop_chain_cross_point(chain: Node):
    """
    判断链表环交点的位置
    """
    assert loop_chain(chain)
    slow = chain
    fast = chain

    while True:
        if slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

    head = chain

    while True:
        if head == slow:
            return head
        else:
            head = head.next
            slow = slow.next


def loop_chain_length(chain: Node):
    """
    判断带环链表长度，环的长度
    """
    assert loop_chain(chain)
    slow = chain
    fast = chain

    while True:
        if slow is not None and fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

    head = chain

    while True:
        if head == slow:
            break
        else:
            head = head.next
            slow = slow.next

    loop_length = 0
    ptr = head
    while True:
        ptr = ptr.next
        loop_length += 1
        if ptr == head:
            break
    length = loop_length
    ptr = chain
    while True:
        ptr = ptr.next
        length += 1
        if ptr == head:
            break
    return length, loop_length


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5]
    nodes = [Node(num) for num in nums]
    head = nodes[0]
    for id in range(1, len(nodes)):
        node_pre = nodes[id - 1]
        node_cur = nodes[id]
        node_pre.next = node_cur

    nodes[5].next = nodes[3]
    print(loop_chain(head))
    print(loop_chain_cross_point(head))
    print(loop_chain_length(head))
