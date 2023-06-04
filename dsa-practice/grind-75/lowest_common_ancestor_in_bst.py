# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        smaller, greater = p, q
        if p.val > q.val:
            smaller, greater = q, p

        lca_node = root
        while lca_node != smaller and lca_node != greater:
            if smaller.val < lca_node.val and greater.val > lca_node.val:
                break

            if smaller.val > lca_node.val and greater.val > lca_node.val:
                lca_node = lca_node.right
            if smaller.val < lca_node.val and greater.val < lca_node.val:
                lca_node = lca_node.left

        return lca_node
