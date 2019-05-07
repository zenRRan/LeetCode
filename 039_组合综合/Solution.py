#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/6 20:53
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def combinationSum(self, candidates, target):
        self.reslist = []
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        return self.reslist

    def DFS(self, candidates, target, start, curlist):
        if target == 0:
            self.reslist.append(curlist)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.DFS(candidates, target - candidates[i], i, curlist+[candidates[i]])







data = [[[2,3,6,7], 7]]
for elem in data:
    print(Solution().combinationSum(elem[0], elem[1]))