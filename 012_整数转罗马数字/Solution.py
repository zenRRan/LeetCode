#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 21:46
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def intToRoman(self, num: int) -> str:
        c = {0: ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"),
             1: ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"),
             2: ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"),
             3: ("", "M", "MM", "MMM")}
        roman = []
        roman.append(c[3][int(num / 1000) % 10])
        roman.append(c[2][int(num / 100) % 10])
        roman.append(c[1][int(num / 10) % 10])
        roman.append(c[0][int(num) % 10])
        s = ''
        for i in roman:
            s = s + i
        return s


data = [3, 4, 9, 58, 1994]
for elem in data:
    print(Solution().intToRoman(elem))
