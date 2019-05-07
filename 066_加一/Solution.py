#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 21:05
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def plusOne(self, digits):
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        flag = True
        digits[-1] = 0
        length = len(digits) - 1
        for i in range(len(digits)):
            if i == 0:
                continue
            if digits[length - i] == 9:
                digits[length - i] = 0
            else:
                digits[length - i] += 1
                flag = False
                break
        if flag:
            return [1] + digits
        else:
            return digits


data = [[1,2,3], [1,9,9], [9,9]]
for elem in data:
    print(Solution().plusOne(elem))

