# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a
# single digit. Add the two numbers and return the sum as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
#
# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
#
# Example 3:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
#
# Constraints:
# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros


from typing import Optional


class ListNode:
    """Definition for singly-linked list"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if l1 is None or l2 is None:
            raise Exception("Cannot add an empty list")

        summ = l1.val + l2.val
        carry = summ // 10
        summ = summ % 10

        head = ListNode(summ)

        curr = head
        curr1, curr2 = l1.next, l2.next
        while curr1 is not None and curr2 is not None:
            summ = curr1.val + curr2.val + carry
            carry = summ // 10
            summ = summ % 10
            curr.next = ListNode(summ)
            curr = curr.next
            curr1 = curr1.next
            curr2 = curr2.next

        while curr1 is not None:
            summ = curr1.val + carry
            carry = summ // 10
            summ = summ % 10
            curr.next = ListNode(summ)
            curr = curr.next
            curr1 = curr1.next

        while curr2 is not None:
            summ = curr2.val + carry
            carry = summ // 10
            summ = summ % 10
            curr.next = ListNode(summ)
            curr = curr.next
            curr2 = curr2.next

        if carry == 1:
            curr.next = ListNode(1)

        return head
