#!/usr/bin/env python  
# encoding: utf-8  

"""
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 二叉树中和为某一值的路径.py 
@time: 2020/5/23 18:04

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

from data_struct.tree import Tree

result = []


def sum_tree_num(root, k):
    global result
    if root.left == None and root.right == None:
        if sum(result) == k:
            print(result)
        result = result[0:-1]
    else:
        if root.left is not None:
            result.append(root.left.data)
            sum_tree_num(root.left, k)
        if root.right is not None:
            result.append(root.right.data)
            sum_tree_num(root.right, k)
        result = result[0:-1]


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    tree_nodes = [Tree(data=num) for num in nums]
    root = tree_nodes[0]
    use_nodes = [tree_nodes.pop(0)]
    while len(tree_nodes):
        tree_node = use_nodes.pop(0)
        left_node = tree_nodes.pop(0)
        right_node = tree_nodes.pop(0)
        tree_node.left = left_node
        tree_node.right = right_node
        use_nodes.append(left_node)
        use_nodes.append(right_node)
    result.append(root.data)
    sum_tree_num(root, 5)
