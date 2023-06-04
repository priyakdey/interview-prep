# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        head = list1
        iter1, iter2 = list1, list2

        if list2.val <= list1.val:
            head = list2
            iter1, iter2 = list2, list1

        prev_node = None
        while iter1 is not None and iter2 is not None:
            if iter1.val <= iter2.val:
                prev_node = iter1
                iter1 = iter1.next
            else:
                iter2_next = iter2.next
                prev_node.next = iter2
                prev_node = iter2
                iter2.next = iter1
                iter2 = iter2_next

        if iter2 is not None:
            prev_node.next = iter2

        return head


soln = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


soln.mergeTwoLists(list1, list2)
