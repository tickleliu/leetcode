#!/usr/bin/env python  
# encoding: utf-8  

"""
给出一个链表，每 k 个节点为一组进行翻转，并返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例 :
给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 每k个一组翻转链表.py 
@time: 2020/5/21 12:55 
"""

from data_struct.node import Node


def rever_link_k(head, k):
    ph = head  # 当前头节点
    pre = None  # 当前轮次的上一节点
    is_head_find = False

    while ph != None:

        # 寻找新的尾节点指向的指针
        count = k
        pr = ph  # 保存前一节点，第一个前一节点设为段落结尾节点，ph保存当前节点
        while pr != None and count > 0:  # p->k
            count -= 1
            pr = pr.next

        if count != 0:  # 如果不够长的话，那么最后一段不反转
            break

        npre = ph  # 当前节点的头，将成为下一轮的pre
        # 反转前, ph当前段落头节点，pr为当前段落的下一个节点
        for i in range(k):
            tmp = ph.next
            ph.next = pr
            pr = ph
            ph = tmp

        # 反转后， pr为当前段落头节点，ph为当前段落的下一个节点, 也就是下一轮的head
        if pre is not None:
            pre.next = pr
        pre = npre

        if is_head_find is False:
            is_head_find = True
            head = pr
    return head


def rever_link_k2(head, k):
    ph = head  # 当前头节点
    pre = None  # 当前轮次的上一节点
    is_head_find = False

    count = 0
    pr = ph  # 保存前一节点，第一个前一节点设为段落结尾节点，ph保存当前节点

    while pr is not None:
        count += 1
        pr = pr.next
        if count % k == 0:
            npre = ph  # 当前节点的头，将成为下一轮的pre
            # 反转前, ph当前段落头节点，pr为当前段落的下一个节点
            for i in range(k):
                tmp = ph.next
                ph.next = pr
                pr = ph
                ph = tmp

            # 反转后， pr为当前段落头节点，ph为当前段落的下一个节点, 也就是下一轮的head
            if pre is not None:
                pre.next = pr
            pre = npre
            if is_head_find is False:
                is_head_find = True
                head = pr
            pr = ph
    return head


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6]
    nodes = [Node(num) for num in nums]
    for i in range(len(nodes) - 1):
        nodes[i].append(nodes[i + 1])

    head = nodes[0]
    res = rever_link_k2(head, 3)
    while res is not None:
        print(res.data)
        res = res.next
