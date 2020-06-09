#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 二叉树最大路径和.py 
@time: 2020/6/7 8:33 
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def maxPathSum(self, root):
        # write your code here
        # 保存1：以root节点为终点的左侧最大路径，以root节点为终点的右侧最大路径，经过root节点的左侧和右侧做大路径
        result = []

        def bfs(root):
            if root is None:
                return 0
            else:
                left_val = bfs(root.left)
                right_val = bfs(root.right)
                val = max(left_val + root.val, right_val + root.val, root.val)
                result.append(val)
                result.append(root.val + left_val + right_val)
                return val

        bfs(root)
        return max(result)


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    tree_nodes = [TreeNode(val=num) for num in nums]
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
    s = Solution()
    s.maxPathSum(root)
