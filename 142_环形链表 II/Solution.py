#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 20:12
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return None
        slow = head
        fast = head

        while slow.next != fast.next.next:
            slow = slow.next
            fast = fast.next.next

        entry = head
        while entry.next != slow.next:
            entry = entry.next
            slow = slow.next

        return entry.next





data = [[1, 3, 4, 2, 2], [3, 1, 3, 4, 2]]
for elem in data:
    print(Solution().findDuplicate(elem))