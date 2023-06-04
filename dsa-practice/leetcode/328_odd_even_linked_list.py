# tag: favourite
# Given the head of a singly linked list, group all the nodes with odd indices
# together followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as
# it was in the input.
#
# You must solve the problem in O(1) extra space complexity and O(n) time complexity.
#
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]
#
# Example 2:
# Input: head = [2,1,3,5,6,4,7]
# Output: [2,3,6,7,1,5,4]


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenListWithExtraSapce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """This solution uses extra space"""
        if head is None or head.next is None:
            return head

        values = []
        curr = head
        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        curr = head
        for i in range(0, len(values), 2):
            curr.val = values[i]
            curr = curr.next

        for i in range(1, len(values), 2):
            curr.val = values[i]
            curr = curr.next

        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """This does constant space and should be faster since we iterate over once"""
        if head is None or head.next is None or head.next.next is None:
            return head

        even_ptr = head
        odd_ptr = head.next
        curr = head.next.next
        curr_idx = 2
        while curr is not None:
            if curr_idx % 2 == 0:
                even_ptr.next = curr
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = curr
                odd_ptr = odd_ptr.next
            curr = curr.next
            curr_idx += 1

        even_ptr.next = head.next
        return head
