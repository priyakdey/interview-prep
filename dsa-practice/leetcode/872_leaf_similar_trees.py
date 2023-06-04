# tag: favourite
# Consider all the leaves of a binary tree, from left to right order,
# the values of those leaves form a leaf value sequence.
#
#
# Example 1:
# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true
#
# Example 2:
# Input: root1 = [1,2,3], root2 = [1,3,2]
# Output: false
#
# Constraints:
# The number of nodes in each tree will be in the range [1, 200].
# Both of the given trees will have values in the range [0, 200].


from typing import List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True

        if (root1.left is None and root1.right is None) and (
            root2.left is None and root2.right is None
        ):
            return root1.val == root2.val

        def dfs(node: Optional[TreeNode], leaves: List[int]) -> None:
            if node.left is None and node.right is None:
                leaves.append(node.val)
                return

            if node.left is not None:
                dfs(node.left, leaves)
            if node.right is not None:
                dfs(node.right, leaves)

        root1_leaves, root2_leaves = [], []

        dfs(root1, root1_leaves)
        dfs(root2, root2_leaves)

        print(root1_leaves, root2_leaves)

        return root1_leaves == root2_leaves
