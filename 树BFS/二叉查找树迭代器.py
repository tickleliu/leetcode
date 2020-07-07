#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 二叉查找树迭代器.py 
@time: 2020/7/6 15:11 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        # do intialization if necessary
        self.stack = []

    """
    @return: True if there has next node, or false
    """

    def hasNext(self, ):
        # write your code here
        return len(self.stack)

    """
    @return: return next node
    """

    def next(self, ):
        # write your code here
        n = self.stack.pop()
        if n.right is not None:
            self.addLeftNode(n.right)
        return n

    def addLeftNode(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left


if __name__ == "__main__":
    pass
