#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 9:18
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm



class Solution:
    def isValid(self, s: str) -> bool:
        stack_list = []
        for i, char in enumerate(s):
            if i == 0:
                stack_list.append(char)
            else:
                if stack_list != [] and stack_list[-1] == '(' and char == ')':
                    stack_list = stack_list[:-1]
                elif stack_list != [] and stack_list[-1] == '{' and char == '}':
                    stack_list = stack_list[:-1]
                elif stack_list != [] and stack_list[-1] == '[' and char == ']':
                    stack_list = stack_list[:-1]
                else:
                    stack_list.append(char)
        if stack_list == []:
            return True
        else:
            return False