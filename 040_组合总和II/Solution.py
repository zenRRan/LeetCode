#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 21:30
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def combinationSum2(self, candidates, target):
        self.reslist = []
        candidates.sort()
        self.DFS(candidates, target, 0, [])
        new_reslist = []
        for elem in self.reslist:
            if elem not in new_reslist:
                new_reslist.append(elem)
        return new_reslist

    def DFS(self, candidates, target, start, curlist):
        if target == 0:
            self.reslist.append(curlist)
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                return
            self.DFS(candidates, target - candidates[i], i+1, curlist + [candidates[i]])






data = [[[10,1,2,7,6,1,5], 8], [[2,5,2,1,2], 5]]
for elem in data:
    print(Solution().combinationSum2(elem[0], elem[1]))