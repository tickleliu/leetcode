#!/usr/bin/env python  
# encoding: utf-8  

"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 指定范围反转链表.py 
@time: 2020/5/21 11:45 
"""

from data_struct.node import Node


def rever_chain(head, pre, e):
    if head is None or head.data > e:
        return pre, head
    tmp = head.next
    head.next = pre
    pre = head
    head = tmp
    return rever_chain(head, pre, e)


def rever_link_s_e(head, s, e):
    pre = head
    while pre.next.data < s:
        pre = pre.next
    tmp_head = pre.next
    revert_head, revert_end = rever_chain(tmp_head, None, e)
    tmp_head.next = revert_end
    pre.next = revert_head
    return head


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    nodes = [Node(num) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].append(nodes[i + 1])

    head = nodes[0]
    res = rever_link_s_e(head, 3, 6)
    while res is not None:
        print(res.data)
        res = res.next
