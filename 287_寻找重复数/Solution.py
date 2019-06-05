#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 19:08
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def findDuplicate(self, nums) -> int:
        if len(nums) == 1:
            return -1
        slow = nums[0]
        fast = nums[slow]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        entry = 0
        while entry != slow:
            entry = nums[entry]
            slow = nums[slow]
        return slow












data = [[1, 3, 4, 2, 2], [3, 1, 3, 4, 2]]
for elem in data:
    print(Solution().findDuplicate(elem))



