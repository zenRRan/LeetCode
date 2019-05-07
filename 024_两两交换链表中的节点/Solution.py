#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 21:38
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        cur = ListNode(0)
        cur.next = head
        first = cur
        while cur.next and cur.next.next:
            n1 = cur.next
            n2 = n1.next
            nxt = n2.next
            n1.next = nxt
            n2.next = n1
            cur.next = n2

            cur = n1
        return first.next