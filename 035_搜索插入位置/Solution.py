#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:53
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def searchInsert(self, nums, target):
        index = 0
        for i, elem in enumerate(nums):
            if target <= elem:
                return i
        return len(nums)





data = [[[1,3,5,6], 5], [[1,3,5,6], 2], [[1,3,5,6], 7], [[1,3,5,6], 0]]
for elem in data:
    print(Solution().searchInsert(elem[0], elem[1]))