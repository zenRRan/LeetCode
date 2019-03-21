#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 21:36
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution-动态规划.py
# @Software: PyCharm


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) <= 1:
            return s

        flag = []
        length = len(s)
        for i in range(length):
            flag.append([False for _ in range(length)])
        for i in range(length):
            flag[i][i] = True
            flag[i][i-1] = True

        res_left, res_right = 0, 0

        for i in range(2, length+1):  # substring len
            for k in range(length-i+1):  # start of substring
                if s[k] == s[k+i-1] and flag[k+1][k+i-2]:
                    flag[k][k+i-1] = True
                    if res_right - res_left < i:
                        res_left = k
                        res_right = k+i-1

        return s[res_left:res_right+1]



data = ['ccc', 'babad', 'cbbd', 'a', 'ab', '']
for elem in data:
    print(Solution().longestPalindrome(s=elem))