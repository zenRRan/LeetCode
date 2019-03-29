#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 21:23
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == '':
            return ''
        if numRows == 1:
            return s
        arr = []
        for i in range(numRows):
            arr.append([' ' for _ in range(len(s))])
        action = 0  # 0down 1up
        i, j, k = 0, 0, 0
        max_len = len(s)
        while True:
            if action == 0:
                arr[i][j] = s[k]
                k += 1
                if k == max_len:
                    break
                if i == numRows-1:
                    action = 1
                    i -= 1
                    j += 1
                else:
                    i += 1
            else:
                arr[i][j] = s[k]
                k += 1
                if k == max_len:
                    break
                if i == 0:
                    action = 0
                    i += 1
                else:
                    i -= 1
                    j += 1
        new_str = ''
        for ii in range(numRows):
            for jj in range(j+1):
                if arr[ii][jj] != ' ':
                    new_str += arr[ii][jj]
            # new_str += '\n'
        return new_str

data = [["LEETCODEISHIRING", 3]]
for elem in data:
    print(Solution().convert(elem[0], elem[1]))
