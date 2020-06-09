#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: tickleliu  
@contact: tickleliu@163.com
@site: https://github.com/tickleliu 
@software: PyCharm 
@file: 两数之和.py 
@time: 2020/6/6 22:25 
"""


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        num_dict = {}
        for idx, num in enumerate(numbers):
            if num not in num_dict:
                num_dict[num] = []
            num_dict[num].append(idx)

        for num in num_dict:
            if target - num == num and len(num_dict[num]) >= 2:
                return num_dict[num][0:2]
            if target - num in num_dict and num_dict[target - num] > num_dict[num]:
                return [num_dict[num][0], num_dict[target - num][0]]


if __name__ == "__main__":
    s = Solution()
    r = s.twoSum([0, 4, 3, 0], 0)
    print(r)
