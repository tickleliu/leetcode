#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 交叉字符串.py 
@time: 2020/6/7 17:50

给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。

样例
样例 1：

输入:
"aabcc"
"dbbca"
"aadbbcbcac"
输出:
true
样例 2：

输入:
""
""
"1"
输出:
false
样例 3：

输入:
"aabcc"
"dbbca"
"aadbbbaccc"
输出:
false
挑战
要求时间复杂度为O(n2)或者更好

"""


class Solution:
    """
    @param s1: A string
    @param s2: A string
    @param s3: A string
    @return: Determine whether s3 is formed by interleaving of s1 and s2
    """

    def isInterleave(self, s1, s2, s3):
        # write your code here
        if len(s1) + len(s2) != len(s3):
            return False
        compare_matrix = [[False] * (len(s1) + 1) for _ in range(len(s2) + 1)]
        compare_matrix[0][0] = True
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1] and compare_matrix[0][i - 1]:
                compare_matrix[0][i] = True

        for i in range(1, len(s2) + 1):
            if s2[i - 1] == s3[i - 1] and compare_matrix[i - 1][0]:
                compare_matrix[i][0] = True

        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                s1_flag = compare_matrix[i - 1][j]
                s2_flag = compare_matrix[i][j - 1]
                if s1_flag and s2[i - 1] == s3[i + j - 1]:
                    compare_matrix[i][j] = True
                elif s2_flag and s1[j - 1] == s3[i + j - 1]:
                    compare_matrix[i][j] = True

        return compare_matrix[-1][-1]


if __name__ == "__main__":
    s = Solution()
    r = s.isInterleave("aaba", "dbbca", "aabdbbcac")
    print(r)
