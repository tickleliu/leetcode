#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: chain.py 
@time: 2020/5/12 19:43 
"""


class Node(object):
    def __init__(self, data, pnext=None):
        self.data = data
        self.next = pnext

    def __repr__(self):
        return str(self.data)

    def append(self, dataOrNode):
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        while node.next:
            node = node.next
        node.next = item
