#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 树的之字形遍历.py 
@time: 2020/5/22 20:28 
"""

from data_struct.tree import Tree


def level_traversal_z(root):
    stack = [root]
    print(root.data)
    print()
    count = 1
    while len(stack) != 0:
        new_stack = []
        for tree_node in stack:
            if count % 2 == 0:
                if tree_node.left is not None:
                    print(tree_node.left.data)
                    new_stack.append(tree_node.left)
                if tree_node.right is not None:
                    print(tree_node.right.data)
                    new_stack.append(tree_node.right)
            else:
                if tree_node.right is not None:
                    print(tree_node.right.data)
                    new_stack.append(tree_node.right)
                if tree_node.left is not None:
                    print(tree_node.left.data)
                    new_stack.append(tree_node.left)
        print()
        count += 1
        new_stack.reverse()
        stack = new_stack


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
    print(level_traversal_z(root))
