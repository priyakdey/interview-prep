# You are given the root of a binary search tree (BST) and an integer val.
#
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.
#
# Example 1:
# Input: root = [4,2,7,1,3], val = 2
# Output: [2,1,3]
#
# Example 2:
# Input: root = [4,2,7,1,3], val = 5
# Output: []
#
# Constraints:
# The number of nodes in the tree is in the range [1, 5000].
# 1 <= Node.val <= 107
# root is a binary search tree.
# 1 <= val <= 107


from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root if root.val == val else None

        node = root
        while node is not None:
            if node.val == val:
                return node
            if val < node.val:
                node = node.left
            else:
                node = node.right

        return None

    # def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    #     if root is None:
    #         return None
    #
    #     if root.val == val:
    #         return root
    #
    #     if val < root.val:
    #         return self.searchBST(root.left, val)
    #     else:
    #         return self.searchBST(root.right, val)
