# Given the head of a singly linked list, reverse the list, and return the reversed list.


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if head is None or head.next is None:
    #         return head
    #
    #     curr = head
    #     prev = None
    #     while curr.next is not None:
    #         _next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = _next
    #
    #     curr.next = prev
    #     head = curr
    #
    #     return head

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        prev = None
        while curr is not None:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        return prev
