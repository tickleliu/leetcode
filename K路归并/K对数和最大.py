#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: K对数和最大.py 
@time: 2020/5/28 10:36

给定两个以升序排列的整形数组 nums1 和 nums2, 以及一个整数 k。

定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2。

找到和最小的 k 对数字 (u1,v1), (u2,v2) ... (uk,vk)。

示例 1:

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
示例 2:

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
示例 3:

输入: nums1 = [1,2], nums2 = [3], k = 3
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]

"""
from queue import PriorityQueue


def k_small_pairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2):
    heap = PriorityQueue(k)
    for num1 in nums1:
        for num2 in nums2:
            sum = num1 + num2
            if not heap.full():
                heap.put([-sum, num1, num2])
            else:
                _sum, _num1, _num2 = heap.get()
                _sum = -_sum
                if num1 + num2 < sum:
                    heap.put([-num1 - num2, num1, num2])
                else:
                    heap.put([-_sum, _num1, _num2])

    result = []
    while not heap.empty():
        sum, num1, num2 = heap.get()
        result.append([num1, num2])
    result.reverse()
    return result


def k_small_pairs2(nums1=[1, 1, 2, 4, 5, 6], nums2=[1, 2, 3], k=2):
    """
    将原始数组转化为len（nums1）个队列
    (1,1),(1,2),(1,3)
    (1,1),(1,2),(1,3)
    (2,1),(2,2),(2,3)
    执行k路合并
    """
    heap = PriorityQueue(k)
    for idx, num in enumerate(nums1[0:k]):
        heap.put([num + nums2[0], idx, 0])
    result = []
    while True:
        sum, num1_idx, num2_idx = heap.get()
        result.append([nums1[num1_idx], nums2[num2_idx]])

        if len(result) == k:
            break

        num2_idx = num2_idx + 1
        if num2_idx < len(nums2):
            sum = nums1[num1_idx] + nums2[num2_idx]
            heap.put([sum, num1_idx, num2_idx])

    return result


if __name__ == "__main__":
    r = k_small_pairs2()
    print(r)
