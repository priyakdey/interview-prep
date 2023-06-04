# https://leetcode.com/problems/diameter-of-binary-tree/


from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_at_node(node: Optional[TreeNode]) -> int:
            if node.left is None and node.right is None:
                return 0

        max_diameter = 0

        def height(node: TreeNode) -> int:
            nonlocal max_diameter

            if node.left is None and node.right is None:
                return 0

            left_height, right_height = 0, 0
            if node.left is not None:
                left_height = 1 + height(node.left)

            if node.right is not None:
                right_height = 1 + height(node.right)

            diameter = left_height + right_height

            if diameter > max_diameter:
                max_diameter = diameter

            return max(left_height, right_height)

        height(root)
        return max_diameter
