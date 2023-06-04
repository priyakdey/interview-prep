# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list. The list should be made by splicing
# together the nodes of the first two lists.
#
# Return the head of the merged linked list.
#
#
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# Input: list1 = [], list2 = []
# Output: []
#
# Example 3:
# Input: list1 = [], list2 = [0]
# Output: [0]
#
# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


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

        head = None
        _iter = None
        iter1, iter2 = list1, list2

        while iter1 is not None and iter2 is not None:
            if iter1.val < iter2.val:
                if head is None:
                    head = ListNode(iter1.val)
                    _iter = head
                else:
                    _iter.next = ListNode(iter1.val)
                    _iter = _iter.next
                iter1 = iter1.next
            else:
                if head is None:
                    head = ListNode(iter2.val)
                    _iter = head
                else:
                    _iter.next = ListNode(iter2.val)
                    _iter = _iter.next
                iter2 = iter2.next

        while iter1 is not None:
            _iter.next = ListNode(iter1.val)
            _iter = _iter.next
            iter1 = iter1.next

        while iter2 is not None:
            _iter.next = ListNode(iter2.val)
            _iter = _iter.next
            iter2 = iter2.next

        return head
