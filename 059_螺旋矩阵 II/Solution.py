#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 21:36
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def generateMatrix(self, n):
        matrix = []
        for i in range(n):
            matrix.append([-1 for _ in range(n)])
        num = 0
        right = True
        down, left, up = False, False, False
        i, j = 0, 0
        while num <= n**2:
            num += 1
            if right:
                if i < n and j < n and matrix[i][j] == -1:
                    matrix[i][j] = num
                    j += 1
                else:
                    j -= 1
                    i += 1
                    right = False
                    down = True
            if down:
                if i < n and j < n and matrix[i][j] == -1:
                    matrix[i][j] = num
                    i += 1
                else:
                    i -= 1
                    j -= 1
                    down = False
                    left = True
            if left:
                if i < n and j > 0 and matrix[i][j] == -1:
                    matrix[i][j] = num
                    j -= 1
                else:
                    j += 1
                    i -= 1
                    left = False
                    up = True
            if up:
                if i > 0 and j < n and matrix[i][j] == -1:
                    matrix[i][j] = num
                    j -= 1
                else:
                    j += 1
                    i += 1
                    up = False
                    right = True
        return matrix









data = [3]
for elem in data:
    print(Solution().generateMatrix(elem))