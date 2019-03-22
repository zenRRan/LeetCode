#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 21:31
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm

class Solution:
    def frequencySort(self, s: str) -> str:
        count_dic = {}
        for char in s:
            if char not in count_dic:
                count_dic[char] = 1
            else:
                count_dic[char] += 1
        count_tuple = []
        for key in count_dic.keys():
            count_tuple.append((key, count_dic[key]))
        count_tuple_list = sorted(count_tuple, key= lambda char_count: char_count[1], reverse=True)
        new_str = ''
        for char, count in count_tuple_list:
            new_str += char * count
        return new_str


data = ['tree', 'cccaaa', 'Aabb']
for elem in data:
    print(Solution().frequencySort(s=elem))