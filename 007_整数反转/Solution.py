#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 21:17
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x == 0 or x < -2e31 or x > 2e31 - 1:
            return 0
        if x < 0:
            neg = True
            x = -x
        str_x = str(x)
        str_x = str_x[::-1]
        # solve 0
        str_x_list = list(str_x)
        new_list = []
        for i, elem in enumerate(str_x_list):
            if elem == '0':
                continue
            else:
                new_list = str_x_list[i:]
                break
        new_x = int(''.join(new_list))
        # solve neg
        if neg:
             new_x = -new_x
        if new_x < -2147483648 or new_x > 2147483647:
            return 0
        else:
            return new_x








data = [123, -123, 120, 0, 1534236469]
for elem in data:
    print(Solution().reverse(x=elem))