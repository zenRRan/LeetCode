#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/28 21:01
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm



class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '':
            return b
        if b == '':
            return a
        flag = 0
        len_a = len(a)
        len_b = len(b)
        length = max(len_a, len_b)
        a = (length - len(a)) * '0' + a
        b = (length - len(b)) * '0' + b
        res = ''
        for i in range(length):
            c = int(a[-1]) + int(b[-1]) + flag
            if c > 2:
                res += '1'
                flag = 1
            elif c > 1:
                res += '0'
                flag = 1
            else:
                res += str(c)
                flag = 0
            a = a[:-1]
            b = b[:-1]
        if flag == 1:
            res += '1'
        return res[::-1]


data = [['11', '1'], ['1010', '1011']]
for elem in data:
    print(Solution().addBinary(elem[0], elem[1]))






