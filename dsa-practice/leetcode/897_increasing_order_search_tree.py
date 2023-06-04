# tag: favourite
# Given the root of a binary search tree, rearrange the tree in
# in-order so that the leftmost node in the tree is now the root of the tree,
# and every node has no left child and only one right child.
#
# Example 1:
# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
# Example 2:
# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
#
# Constraints:
# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000


from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None or (root.left is None and root.right is None):
            return root

        def inOrderDFS(node: Optional[TreeNode], nodes: List[TreeNode]) -> None:
            if node is None:
                return

            inOrderDFS(node.left, nodes)
            nodes.append(node)
            inOrderDFS(node.right, nodes)

        nodes = []
        inOrderDFS(root, nodes)

        for i in range(1, len(nodes)):
            nodes[i - 1].right = nodes[i]
            nodes[i].left = None

        nodes[0].left = None
        nodes[-1].right = None
        nodes[-1].left = None

        return nodes[0]
