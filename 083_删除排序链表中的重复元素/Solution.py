#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/29 19:20
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
        if head == None:
            return head
        first, end = head, head.next
        while end != None:
            if first.val != end.val:
                first.next = end
                first = end
                end = end.next
            else:
                end = end.next
        first.next = end
        return head





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

data = [[], [1], [1, 1, 2], [1, 1, 2, 3, 3]]
for elem in data:
    head = Solution().deleteDuplicates(buildList(elem))
    while head != None:
        print(head.val, end=' ')
        head = head.next
    print()


