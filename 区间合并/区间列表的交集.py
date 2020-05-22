#!/usr/bin/env python  
# encoding: utf-8  

"""
输入：A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
注意：输入和所需的输出都是区间对象组成的列表，而不是数组或列表。
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 区间列表的交集.py 
@time: 2020/5/18 20:32 
"""


def over_lap(ax, ay, bx, by):
    if ax >= bx:
        tx, ty = ax, ay
        ax, ay = bx, by
        bx, by = tx, ty

    if ay >= bx and ay <= by:
        return [bx, ay]
    elif ay > by:
        return [bx, by]
    else:
        return []


def interval_intersection(A, B):
    C = []
    while True:
        if len(A) == 0 or len(B) == 0:
            break

        ax, ay = A[0]
        bx, by = B[0]
        c = over_lap(ax, ay, bx, by)
        if len(c) != 0:
            C.append(c)
        if ay > by:
            B = B[1:]
        else:
            A = A[1:]

    return C


import collections


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_dict = {}
        graph = collections.defaultdict(set)

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                email_dict[email] = account[0]
                graph[account[1]].add(email)
                graph[email].add(account[1])
        used_email = set()
        result = []
        for email in graph:
            if email not in used_email:
                used_email.add(email)
                stack = [email]
                emails = [email]
                while stack:
                    email = stack.pop()
                    for nei in graph[email]:
                        if nei not in used_email:
                            stack.append(nei)
                            emails.append(nei)
                            used_email.add(nei)
                item = [email_dict[emails[0]], emails]
                result.append(item)
        return result


if __name__ == "__main__":
    A = [[0, 2], [5, 10], [13, 23], [24, 25]]
    B = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(interval_intersection(A, B))
    solu = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    print(solu.accountsMerge(accounts))
