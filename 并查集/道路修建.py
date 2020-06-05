#!/usr/bin/env python
# encoding: utf-8

"""
@version: v1.0
@author: mlliu
@contact: mlliu2@iflytek.com
@site: https://github.com/tickleliu
@software: PyCharm
@file: 道路修建.py
@time: 2020/06/04 16:56
可以想象一张地图上有很多点，有些点之间是有道路相互联通的，而有些点则没有。如果我们现在要从点A走向点B
们需要设计一个算法，让计算机依次读取这些数据，最后判断出其中任意两点是否连通。
"""


def link_area(G=[(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9), (5, 0), (7, 2), (6, 1), (6, 7)]):
    g = {}
    for item in G:
        id1, id2 = item
        if id1 not in g:
            g[id1] = set()
        g[id1].add(id2)

        if id2 not in g:
            g[id2] = set()
        g[id2].add(id1)

    def dfs(idx, g, visited, area):
        for n in g[idx]:
            if n not in visited:
                visited.append(n)
                area.append(n)
                dfs(n, g, visited, area)

    result = []
    visited = []
    for gn in g:
        if gn not in visited:
            area = [gn]
            visited.append(gn)
            dfs(gn, g, visited, area)
            result.append(area)
    return len(result) - 1


if __name__ == "__main__":
    link_area()
