# Version python3.6
# -*- coding: utf-8 -*-
# @Time    : 2018/9/5 12:25 PM
# @Author  : zenRRan
# @Email   : zenrran@qq.com
# @File    : lengthOfLongestSubstring.py
# @Software: PyCharm Community Edition


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        str_list = list(s)
        cur_list = []
        max_len = 0
        i, j = 0, 0
        s_len = len(str_list)
        while i != s_len and j != s_len:
            if str_list[j] not in cur_list:
                cur_list.append(str_list[j])
                max_len = max(max_len, len(cur_list))
                j += 1
            else:
                max_len = max(max_len, len(cur_list))
                cur_list = cur_list[1:]
                i += 1
        return max_len

solution = Solution()
print(solution.lengthOfLongestSubstring('a'))