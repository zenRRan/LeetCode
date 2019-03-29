#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 21:37
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm



class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        if not height or len(height) == 1:
            return 0
        res = (r - l) * (height[l] if height[l] < height[r] else height[r])

        while l < r:
            if height[l] < height[r]:
                res = res if res > height[l] * (r - l) else height[l] * (r - l)
                l += 1
            else:
                res = res if res > height[r] * (r - l) else height[r] * (r - l)
                r -= 1
        return res