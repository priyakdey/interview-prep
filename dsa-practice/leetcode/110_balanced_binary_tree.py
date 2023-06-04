# tag: favourite
# Given a binary tree, determine if it is height-balanced
#
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#
# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#
# Example 3:
# Input: root = []
# Output: true
#
# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

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

        def is_balanced_node(node: Optional[TreeNode]) -> Tuple[bool, int]:
            """Returns if the node is balanced and the height of this node"""
            if node is None:
                return (True, 0)

            left = is_balanced_node(node.left)
            right = is_balanced_node(node.right)

            # is_balanced says if the node is balanced
            # node is balanced if
            #   - left subtree is balanced
            #   - right subtree is balanced
            #   - height of left substree - height of right subtree <= 1
            is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return (is_balanced, 1 + max(left[1], right[1]))

        return is_balanced_node(root)[0]
