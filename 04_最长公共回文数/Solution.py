#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/20 12:50
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        longest_str = ''
        for i in range(len(s)):
            for j in range(i):
                cur_str = s[j:i+1]
                cur_str_len = len(cur_str)
                cur_max_len = 0
                flag = True
                for k in range(cur_str_len // 2 + 1):
                    if cur_str[k] == cur_str[-k-1]:
                        cur_max_len += 1
                    else:
                        flag = False
                        break
                if flag:
                    if max_len < len(cur_str):
                        max_len = len(cur_str)
                        longest_str = cur_str
        if longest_str == '' and s != '':
            longest_str = s[0]
        return longest_str

data = ['ccc', 'babad', 'cbbd', 'a', 'ab', '']
for elem in data:
    print(Solution().longestPalindrome(s=elem))