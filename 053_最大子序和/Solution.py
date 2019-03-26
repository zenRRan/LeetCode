#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 20:41
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def maxSubArray(self, nums):
        sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            sum += nums[i]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
            i += 1
        return max_sum



data = [[-2, 1, -3, 4, -1, 2, 1, -5, 4]]
for elem in data:
    print(Solution().maxSubArray(nums=elem))