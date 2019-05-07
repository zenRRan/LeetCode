#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 20:53
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if abs(res - target) > abs(temp - target):
                    res = temp
                elif target < temp:
                    r -= 1
                else:
                    l += 1
        return res


data = [[[-1, 2, 1, -4], 1]]
for elem in data:
    print(Solution().threeSumClosest(elem[0], elem[1]))