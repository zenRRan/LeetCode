#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 21:34
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n + 1)
        res[0] = 0
        res[1] = 1
        res[2] = 2
        for i in range(3, n+1):
            res[i] += res[i-1] + res[i-2]
        return res[n]




data = [2, 3]
for elem in data:
    print(Solution().climbStairs(elem))