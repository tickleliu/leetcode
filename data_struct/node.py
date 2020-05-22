#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: Node.py 
@time: 2020/5/21 11:45 
"""


class Node():
    def __init__(self, data):
        super(Node, self).__init__()
        self.data = data
        self.next = None

    def append(self, node):
        self.next = node


if __name__ == "__main__":
    pass
