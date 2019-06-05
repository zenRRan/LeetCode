#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 21:34
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return (sum(set(nums)) * 3 - sum(nums)) / 2




data = [[2,2,3,2], [0,1,0,1,0,1,99]]
for elem in data:
    print(Solution().singleNumber(elem))