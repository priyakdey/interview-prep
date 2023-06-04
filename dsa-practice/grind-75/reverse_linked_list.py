# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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

        head = prev
        return head
