#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 21:16
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def generateParenthesis(self, n):
        self.res = []
        self.generateParenthesisIter('', n, n)
        return self.res

    def generateParenthesisIter(self, cur_str, r, l):
        if r == 0 and l == 0:
            self.res.append(cur_str)
        if l > 0:
            self.generateParenthesisIter(cur_str + '(', r, l - 1)
        if r > 0 and r > l:
            self.generateParenthesisIter(cur_str + ')', r - 1, l)


data = [3]
for elem in data:
    print(Solution().generateParenthesis(elem))






