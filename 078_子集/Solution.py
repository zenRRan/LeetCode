#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 21:45
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def subsets(self, nums):
        self.res = []

        def dfs(nums, temp, i):
            self.res.append(temp[:])
            for i in range(i, len(nums)):
                temp.append(nums[i])
                dfs(nums, temp, i + 1)
                temp.pop()

        dfs(nums, [], 0)
        return self.res






data = [[1, 2, 3]]
for elem in data:
    print(Solution().subsets(elem))