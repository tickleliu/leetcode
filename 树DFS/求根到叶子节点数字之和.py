#!/usr/bin/env python  
# encoding: utf-8  

"""
给定一个二叉树，它的每个结点都存放一个 0-9 的数字，每条从根到叶子节点的路径都代表一个数字。计算从根到叶子节点生成的所有数字串之和。
示例 1:

输入: [1,2,3]
    1
   / \
  2   3
输出: 25
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 求根到叶子节点数字之和.py 
@time: 2020/5/23 17:48 
"""
from data_struct.tree import Tree

sum = 0
result = []


def sum_tree_num(root):
    global result, sum
    if root.left == None and root.right == None:
        sum += int("".join(result))
        result = result[0:-1]
    else:
        if root.left is not None:
            result.append(root.left.data)
            sum_tree_num(root.left)
        if root.right is not None:
            result.append(root.right.data)
            sum_tree_num(root.right)
        result = result[0:-1]


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    tree_nodes = [Tree(data=str(num)) for num in nums]
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
    sum_tree_num(root)
    print(sum)
    print(137 + 138 + 14 + 25 + 26)
