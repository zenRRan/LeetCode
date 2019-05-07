#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 21:29
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip().split()
        if s == []:
            return 0
        return len(s[-1])







data = ['Hello World   ', '    ']
for elem in data:
    print(Solution().lengthOfLastWord(elem))