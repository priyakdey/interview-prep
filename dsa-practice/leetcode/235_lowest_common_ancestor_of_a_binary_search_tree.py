# tag: favourite
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of
# two given nodes in the BST.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor is
# defined between two nodes p and q as the lowest node in T that has both p and q
# as descendants (where we allow a node to be a descendant of itself).”
#
# Example 1:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#
# Example 2:
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
#
# Example 3:
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#
# Constraints:
#
# The number of nodes in the tree is in the range [2, 105].
# -109 <= Node.val <= 109
# All Node.val are unique.
# p != q
# p and q will exist in the BST.


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        # 1.if we need to traverse in two directions: -> this is the LCA
        # 2. If we find the val == p or val == q -> found node is LCA, we should check both values
        #             -> thus dont care which directiorn is the other one
        # 3. if both less than curr node    -> travel left
        # 4. if both greater than curr node -> travel left

        if (
            root.left is None and root.right.left is None and root.right.right is None
        ) or (
            root.right is None and root.left.left is None and root.left.right is None
        ):
            return root

        # reassign p to be the node with the lower val and q the higher
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        curr = root
        while True:
            if curr.val == p.val:
                return curr
            if curr.val == q.val:
                return curr

            if p.val < curr.val and q.val > curr.val:
                return curr

            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
