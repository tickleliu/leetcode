#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 二叉树的直径.py 
@time: 2020/5/31 18:21
题目：
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

      1
     / \
    2   3
   / \
  4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]

"""

from data_struct.tree import Tree


def calc_height(root):
    right = height(root.right)
    left = height(root.left)
    return right + left


def height(root):
    if root is None:
        return 0

    right_height = height(root.right)
    right_height = right_height + 1
    left_height = height(root.left)
    left_height = left_height + 1

    return max(right_height, left_height)


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
    result = calc_height(root)
    print(result)
