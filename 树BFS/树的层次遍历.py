#!/usr/bin/env python
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 树的层次遍历.py 
@time: 2020/5/22 20:15 
"""

from data_struct.tree import Tree


def level_traversal(root):
    stack = [root]
    while len(stack) != 0:
        tree_node = stack.pop(0)
        print(tree_node.data)
        if tree_node.left is not None:
            stack.append(tree_node.left)
        if tree_node.left is not None:
            stack.append(tree_node.right)


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
