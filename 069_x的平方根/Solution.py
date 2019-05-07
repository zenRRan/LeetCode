#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 21:41
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l = 1
        r = x
        while l <= r:
            m = (l+r) // 2
            if m**2 <= x < (m+1)**2:
                return m
            if m**2 < x:
                l = m
            else:
                r = m












data = [4, 8, 1, 2147395599]
for elem in data:
    print(Solution().mySqrt(elem))