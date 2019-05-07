#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/12 21:54
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


class Solution:
    def isValidSudoku(self, board) -> bool:

        dic_row = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_col = [{}, {}, {}, {}, {}, {}, {}, {}, {}]
        dic_box = [{}, {}, {}, {}, {}, {}, {}, {}, {}]

        for i in range(len(board)):
            for j in range(len(board)):
                num = board[i][j]
                if num == ".":
                    continue
                if num not in dic_row[i] and num not in dic_col[j] and num not in dic_box[3 * (i // 3) + (j // 3)]:
                    dic_row[i][num] = 1
                    dic_col[j][num] = 1
                    dic_box[3 * (i // 3) + (j // 3)][num] = 1
                else:
                    return False

        return True
