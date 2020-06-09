#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 两个有序数列寻找中位数（K位数）.py 
@time: 2020/5/26 12:04 
"""


def median(num1=[1, 3, 5, 7], num2=[2, 4, 6, 8]):
    '''
    技巧：
    使用c1和c2将数组拆分，c1和c2应满足c1+c2=(m+n)/2
    a1，a2，a3 | c1 | a4，a5
    b1，b2，b3 | c2 | b4，b5
    比较a3和b4，b3和a4
    如果a3 < b4 and b3 < a4，寻找到正确的分割点
    否则a3>b4,那么c1左移动，c2右移动
    b3>a4，那么与上面相反

    '''
    m = len(num1)
    n = len(num2)
    if m < n:
        median(num2, num1)
    lo = 0
    hi = m * 2
    while lo <= hi:
        c1 = (lo + hi) // 2

        c2 = m + n - c1

        if c1 == 0:
            l1 = -9999
        else:
            l1 = num1[(c1 - 1) // 2]

        if c1 == 2 * m:
            r1 = 9999
        else:
            r1 = num1[c1 // 2]

        if c2 == 0:
            l2 = -9999
        else:
            l2 = num2[(c2 - 1) // 2]

        if c2 == 2 * n:
            r2 = 9999
        else:
            r2 = num2[c2 // 2]

        if l1 > r2:
            hi = c1 - 1
        elif l2 > r1:
            lo = c1 + 1
        else:
            break

    mid = (max(l1, l2) + min(r1, r2)) / 2
    return mid


def topk(num1=[1, 3, 5, 7], num2=[4, 6, 8, 10], k=1):
    m = len(num1)
    n = len(num2)
    if m < n:
        topk(num2, num1, k)
    lo = 0
    hi = 2 * k
    while lo <= hi:
        c1 = (lo + hi) // 2

        c2 = 2 * k - c1

        if c1 == 0:
            l1 = -9999
        else:
            l1 = num1[(c1 - 1) // 2]

        if c1 == 2 * m:
            r1 = 9999
        else:
            r1 = num1[c1 // 2]

        if c2 == 0:
            l2 = -9999
        else:
            l2 = num2[(c2 - 1) // 2]

        if c2 == 2 * n:
            r2 = 9999
        else:
            r2 = num2[c2 // 2]

        if l1 > r2:
            hi = c1 - 1
        elif l2 > r1:
            lo = c1 + 1
        else:
            break

    result = max(l1, l2)
    return result


if __name__ == "__main__":
    result = median(num1=[1, 2, 3, 4], num2=[5, 6, 7, 8, 9])
    # print(result)
    # result = topk()
    # print(result)
