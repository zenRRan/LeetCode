#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 9:16
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_list = list(str(x))
        x_list.reverse()
        x_reversed = ''.join(x_list)
        if str(x) == x_reversed:
            return True
        else:
            return False