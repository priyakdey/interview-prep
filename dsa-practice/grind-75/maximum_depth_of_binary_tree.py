# https://leetcode.com/problems/maximum-depth-of-binary-tree/


from typing import Optional


class TreeNode:
    """# Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        def depth_at_node(node: TreeNode) -> int:
            """Returns the depth of the node"""
            if node is None:
                return 0

            left_depth = depth_at_node(node.left)
            right_depth = depth_at_node(node.right)

            return 1 + max(left_depth, right_depth)

        return depth_at_node(root)
