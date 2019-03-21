# Version python3.6
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 10:25 PM
# @Author  : zenRRan
# @Email   : zenrran@qq.com
# @File    : addTwoNumbers.py
# @Software: PyCharm Community Edition


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        # if l1.val == 0:
        #     head = l2
        #     return head
        # elif l2.val == 0:
        #     head = l1
        #     return head

        new_list = None
        flag = 0
        # last_flag = 0
        while True:
            while l1 is not None and l2 is not None:
                s = l1.val + l2.val + flag
                flag = 0
                if s > 9:
                    flag = 1
                    s -= 10
                if new_list == None:
                    new_list = ListNode(s)
                    head = new_list
                else:
                    new_list.next = ListNode(s)
                    new_list = new_list.next
                l1 = l1.next
                l2 = l2.next
            if l1 is None and l2 is not None:
                while l2 is not None:
                    if flag == 1:
                        s = l2.val + flag
                        flag = 0
                        if s > 9:
                            flag = 1
                            s -= 10
                        new_list.next = ListNode(s)
                        new_list = new_list.next
                        l2 = l2.next
                    else:
                        new_list.next = l2
                        return head

            elif l2 is None and l1 is not None:
                while l1 is not None:
                    if flag == 1:
                        s = l1.val + flag
                        flag = 0
                        if s > 9:
                            flag = 1
                            s -= 10
                        new_list.next = ListNode(s)
                        new_list = new_list.next
                        l1 = l1.next
                    else:
                        new_list.next = l1
                        return head
            else:
                if flag == 1:
                    s = flag
                    new_list.next = ListNode(s)
                return head


l1 = ListNode(1)
l1.next = ListNode(8)
l1.next.next = ListNode(3)

l2 = ListNode(7)
l2.next = ListNode(1)
# l2.next.next = ListNode(4)

solution = Solution()
new_list = solution.addTwoNumbers(l1=l1, l2=l2)
while new_list is not None:
    print(new_list.val, end='')
    new_list = new_list.next


