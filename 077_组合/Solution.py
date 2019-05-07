#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 21:44
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def combine(self, n: int, k: int):
        res = []
        self.helper(range(1, n + 1), k, res, [])
        return res

    def helper(self, array, k, res, path):
        if k > len(array):
            return
        if k == 0:
            res.append(path)
        else:
            self.helper(array[1:], k - 1, res, path + [array[0]])
            self.helper(array[1:], k, res, path)




data = [[4, 2]]
for elem in data:
    print(Solution().combine(elem[0], elem[1]))
