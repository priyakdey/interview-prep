# You are given an integer array nums with no duplicates.
# A maximum binary tree can be built recursively from nums using the following algorithm:
#
# Create a root node whose value is the maximum value in nums.
# Recursively build the left subtree on the subarray prefix to the left of the maximum value.
# Recursively build the right subtree on the subarray suffix to the right of the maximum value.
# Return the maximum binary tree built from nums.
#
# Example 1:
# Input: nums = [3,2,1,6,0,5]
# Output: [6,3,5,null,2,0,null,null,1]
# Explanation: The recursive calls are as follow:
# - The largest value in [3,2,1,6,0,5] is 6. Left prefix is [3,2,1] and right suffix is [0,5].
#     - The largest value in [3,2,1] is 3. Left prefix is [] and right suffix is [2,1].
#         - Empty array, so no child.
#         - The largest value in [2,1] is 2. Left prefix is [] and right suffix is [1].
#             - Empty array, so no child.
#             - Only one element, so child is a node with value 1.
#     - The largest value in [0,5] is 5. Left prefix is [0] and right suffix is [].
#         - Only one element, so child is a node with value 0.
#         - Empty array, so no child.
#
# Example 2:
# Input: nums = [3,2,1]
# Output: [3,null,2,null,1]
#
# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000
# All integers in nums are unique.

from typing import List, Tuple, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        def max_and_index(arr: List[int]) -> Tuple[int, int]:
            """Returns a tuple in the form (index_of_max_element, max_element)"""
            return max(enumerate(arr), key=lambda x: x[1])

        def create_children(
            parent: "TreeNode", left: List[int], right: List[int]
        ) -> None:
            """create the left and right children for the parent node"""
            if len(left) == 0 and len(right) == 0:
                return

            if len(left) != 0:
                index, val = max_and_index(left)
                parent.left = TreeNode(val)
                create_children(parent.left, left[0:index], left[index + 1 :])

            if len(right) != 0:
                index, val = max_and_index(right)
                parent.right = TreeNode(val)
                create_children(parent.right, right[0:index], right[index + 1 :])

        # create the head first
        index, value = max_and_index(nums)
        head = TreeNode(value)
        left, right = nums[0:index], nums[index + 1 :]
        # create the children
        create_children(head, left, right)

        return head
