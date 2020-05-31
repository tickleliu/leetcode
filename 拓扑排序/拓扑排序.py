#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 拓扑排序.py 
@time: 2020/5/31 18:03 
"""


def top_sort(G):
    result = []
    while len(G) != 0:
        for key in G:
            if len(G[key]) == 0:
                result.append(key)
                break
        del G[key]
        for t_key in G:
            if key in G[t_key]:
                G[t_key] = G[t_key].replace(key, "")
    result.reverse()
    return result


if __name__ == "__main__":
    g = {
        'a': 'bce',
        'b': 'd',
        'c': 'd',
        'd': '',
        'e': 'cd'
    }

    r = top_sort(g)
    print(r)
