#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/31 21:49
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_s = [elem for elem in s.lower() if elem >= '0' and elem <= '9' or elem >= 'a' and elem <= 'z']
        if new_s == []:
            return True
        length = len(new_s)
        if length % 2 == 0:
            first = new_s[:length // 2]
            end = new_s[length // 2:]
            return first == end
        else:
            first = new_s[:length // 2]
            end = new_s[length // 2 + 1::-1]
            return first == end





data = ["A man, a plan, a canal: Panama", "race a car"]
for elem in data:
    print(Solution().isPalindrome(elem))