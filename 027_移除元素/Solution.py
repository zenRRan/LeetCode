#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:36
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def removeElement(self, nums, val):
        totle_len = len(nums)
        val_num = 0
        for elem in nums:
            if elem == val:
                val_num += 1

        for elem in range(val_num):
            nums.remove(val)
        return totle_len - val_num



data = [[[3,2,2,3], 2], [[0,1,2,2,3,0,4,2], 2]]
for elem in data:
    print(Solution().removeElement(elem[0], elem[1]))