# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root

        def swap_substree(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            left, right = node.left, node.right
            node.left = right
            node.right = left

            swap_substree(node.left)
            swap_substree(node.right)

        swap_substree(root)
        return root
