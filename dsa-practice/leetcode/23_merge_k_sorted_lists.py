# tag:favourite
# TODO: redo with Heap
# You are given an array of k linked-lists lists, each linked-list is sorted
# in ascending order.
#
# Merge all the linked-lists into one sorted linked-list and return it.
#
# Example 1:
# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6
#
# Example 2:
# Input: lists = []
# Output: []
#
# Example 3:
# Input: lists = [[]]
# Output: []
#
# Constraints:
# k == lists.length
# 0 <= k <= 104
# 0 <= lists[i].length <= 500
# -104 <= lists[i][j] <= 104
# lists[i] is sorted in ascending order.
# The sum of lists[i].length will not exceed 104.


from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        lists = list(filter(lambda n: n is not None, lists))

        values = []
        for _list in lists:
            curr = _list
            while curr is not None:
                values.append(curr.val)
                curr = curr.next

        values.sort()
        head = None
        curr = head
        for v in values:
            if head is None:
                head = ListNode(v)
                curr = head
            else:
                curr.next = ListNode(v)
                curr = curr.next

        return head
