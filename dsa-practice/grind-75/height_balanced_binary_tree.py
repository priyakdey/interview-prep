# https://leetcode.com/problems/balanced-binary-tree/


from typing import Optional, Tuple


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None or (root.left is None and root.right is None):
            return True

        def is_node_height_balanced(node: Optional[TreeNode]) -> Tuple[int, bool]:
            if node is None:
                return (1, True)

            left = is_node_height_balanced(node.left)
            right = is_node_height_balanced(node.right)

            is_height_balanced = left[1] and right[1] and abs(left[0] - right[0]) <= 1
            height = 1 + max(left[0], right[0])
            return (height, is_height_balanced)

        _, is_tree_height_balanced = is_node_height_balanced(root)
        return is_tree_height_balanced
