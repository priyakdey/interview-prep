# tag: favourite
# Given the root of a binary tree and an integer targetSum, return the number of
# paths where the sum of the values along the path equals targetSum.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
#
# Example 1:
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
#
# Example 2:
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
#
# Constraints:
# The number of nodes in the tree is in the range [0, 1000].
# -109 <= Node.val <= 109
# -1000 <= targetSum <= 1000


from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1 if root.val == targetSum else 0

        def check_sum_for_paths(node: Optional[TreeNode], prefix_sum: int) -> int:
            if node is None:
                return 0

            total_paths = 0
            prefix_sum += node.val
            if prefix_sum == targetSum:
                total_paths = 1

            return (
                total_paths
                + check_sum_for_paths(node.left, prefix_sum)
                + check_sum_for_paths(node.right, prefix_sum)
            )

        total_paths = 0
        stack = [root]
        while len(stack) != 0:
            _node = stack[-1]
            total_paths += check_sum_for_paths(_node, 0)
            if _node is not None:
                stack.insert(0, _node.left)
                stack.insert(0, _node.right)
            del stack[-1]

        return total_paths
