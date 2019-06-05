#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 15:42
# @Author  : zenRRan
# @Version : python3.7 
# @File    : Solution.py
# @Software: PyCharm


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        cur = head
        h = ListNode(0)
        h.next = head
        pre = h
        while cur:
            flag = False
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
                flag = True
            if flag is False:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return h.next





def buildList(List):
    last_node = None
    head = None
    for i, elem in enumerate(List):
        if i == 0:
            node = ListNode(elem)
            last_node = node
            head = last_node
        else:
            last_node.next = ListNode(elem)
            last_node = last_node.next
    return head

data = [[1, 1, 2], [], [1], [1, 1, 2, 3, 3], [1, 2, 3, 3, 4, 4, 5], [1, 1, 1, 2, 3]]
for elem in data:
    head = Solution().deleteDuplicates(buildList(elem))
    while head != None:
        print(head.val, end=' ')
        head = head.next
    print()
