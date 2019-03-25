#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 21:10
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        if s == '':
            return True

        if len(wordDict) == 1:
            if s == wordDict[0]:
                return True
            else:
                return False

        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        for i in range(len(s)+1):
            cur_str = s[:i+1]
            for j in range(i+1):
                if cur_str in wordDict and dp[j]:
                    dp[i+1] = 1
                cur_str = cur_str[1:]


        return dp[-1] == 1