# Version python3.6
# -*- coding: utf-8 -*-
# @Time    : 2018/9/4 8:16 AM
# @Author  : zenRRan
# @Email   : zenrran@qq.com
# @File    : twoSum.py
# @Software: PyCharm Community Edition

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, e1 in enumerate(nums):
            for j, e2 in enumerate(nums[i + 1:]):
                if e1 + e2 == target:
                    return [i, j + i + 1]
