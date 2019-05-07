#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 21:13
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
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)
        first = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next
        if l1 == None:
            head.next = l2
        elif l2 == None:
            head.next = l1
        return first.next

        # if l1 == None:
        #     return l2
        # if l2 == None:
        #     return l1
        # _l1, _l2 = l1, l2
        # # merge_list_node = l1 if l1.val >= l2.val else l2
        # on_l1 = False
        # merge_list_node = None
        # head = merge_list_node
        # while True:
        #     if l1.val <= l2.val:
        #         if merge_list_node == None:
        #             on_l1 = True
        #             merge_list_node = l1
        #             head = merge_list_node
        #             _l1 = _l1.next
        #         else:
        #             if not on_l1:
        #                 _l2 = _l2.next
        #                 on_l1 = True
        #             merge_list_node.next = l1
        #             merge_list_node = merge_list_node.next
        #
        #     else:
        #         if merge_list_node == None:
        #             merge_list_node = l2
        #             head = merge_list_node
        #         else:
        #             merge_list_node.next = l2
        #             merge_list_node = merge_list_node.next
        #         _l2 = _l2.next
        #
        #     if _l1 == None:
        #         merge_list_node.next = _l2
        #         break
        #     if _l2 == None:
        #         merge_list_node.next = _l1
        #         break
        # return head






def build_listnote(l):
    before_node = None
    begin_node = None
    for elem in l:
        new_node = ListNode(elem)
        if before_node == None:
            before_node = new_node
            begin_node = new_node
        else:
            before_node.next = new_node
            before_node = before_node.next
    return begin_node

def print_listnode(l):
    if l == None:
        print('no data', end='')
        return
    while True:
        print(l.val, end=' ')
        l = l.next
        if l == None:
            break
    print()

data = [[[1, 2, 4], [1, 3, 4]]]
for elem in data:
    list_node1 = build_listnote(elem[0])
    print_listnode(list_node1)
    list_node2 = build_listnote(elem[1])
    print_listnode(list_node2)
    merge_list_node = Solution().mergeTwoLists(list_node1, list_node2)
    print_listnode(merge_list_node)
