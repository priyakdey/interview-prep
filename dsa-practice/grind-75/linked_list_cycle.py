# https://leetcode.com/problems/linked-list-cycle/description/

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if head is None or head.next is None:
        #     return False
        #
        # visited_nodes = set()
        # curr = head
        # has_cycle = False
        #
        # while curr is not None:
        #     if curr in visited_nodes:
        #         has_cycle = True
        #         break
        #     visited_nodes.add(curr)
        #     curr = curr.next
        #
        # return has_cycle

        # Flyod's cycle detection algorithm in O(1) space
        if head is None or head.next is None:
            return False

        def next_node(node: Optional[ListNode]) -> Optional[ListNode]:
            if node is None:
                return None

            return node.next

        slow_pointer = head  # starts at 1 st node
        fast_pointer = next_node(head)  # starts at 2nd node

        while fast_pointer != slow_pointer and fast_pointer is not None:
            slow_pointer = next_node(slow_pointer)
            fast_pointer = next_node(next_node(fast_pointer))

        return fast_pointer == slow_pointer
