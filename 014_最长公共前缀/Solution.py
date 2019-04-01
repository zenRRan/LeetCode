#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 21:49
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        if len(strs) == 0:
            return ""
        for each in zip(*strs):
            print(each)
            if len(set(each)) == 1:
                res += each[0]
            else:
                return res
        return res





data = [["flower","flow","flight"]]
for elem in data:
    print(Solution().longestCommonPrefix(strs=elem))