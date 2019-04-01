#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 21:08
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def letterCombinations(self, digits):
        if digits == '':
            return []
        dic = {2: ['a', 'b', 'c'],
               3: ['d', 'e', 'f'],
               4: ['g', 'h', 'i'],
               5: ['j', 'k', 'l'],
               6: ['m', 'n', 'o'],
               7: ['p', 'q', 'r', 's'],
               8: ['t', 'u', 'v'],
               9: ['w', 'x', 'y', 'z']}
        cur_str = []
        if len(digits) == 1:
            return dic[int(digits[0])]
        result = self.letterCombinations(digits[1:])
        for r in result:
            for j in dic[int(digits[0])]:
                cur_str.append(j + r)
        return cur_str


data = ['234']
for elem in data:
    print(Solution().letterCombinations(elem))