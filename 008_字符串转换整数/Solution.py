#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 20:54
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip()
        syb = 1
        ptr = 0
        res = 0
        if len(s) == 0:
            return 0
        if s[0] == '-':
            syb = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return 0
        while s[ptr].isnumeric():
            res = res * 10 + int(s[ptr])
            ptr += 1
            if ptr >= len(s):
                break
        res = res * syb
        if res > 2147483647:
            res =  2147483647
        elif res < -2147483648:
            res = -2147483648
        return res



data = ['--2', '0-1', '42', '      -42', '4193 with words', 'words and 987', '-91283472332']
for elem in data:
    print(Solution().myAtoi(str=elem))