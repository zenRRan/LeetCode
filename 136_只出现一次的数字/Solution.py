#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 21:26
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
        return sum(set(nums)) * 2 - sum(nums)




data = [[2,2,1], [4,1,2,1,2]]
for elem in data:
    print(Solution().singleNumber(elem))