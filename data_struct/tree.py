#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: tree.py 
@time: 2020/5/22 20:02 
"""


class Tree(object):
    def __init__(self, data, left=None, right=None):
        super(Tree, self).__init__()
        self.left = left
        self.right = right
        self.data = data

    def __str__(self):
        return str(self.data)
