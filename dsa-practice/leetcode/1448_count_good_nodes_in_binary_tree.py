# tag: favourite
# Given a binary tree root, a node X in the tree is named good if in the path from
# root to X there are no nodes with a value greater than X.
#
# Return the number of good nodes in the binary tree.
#
# Example 1:
# Input: root = [3,1,4,3,null,1,5]
# Output: 4
# Explanation: Nodes in blue are good.
# Root Node (3) is always a good node.
# Node 4 -> (3,4) is the maximum value in the path starting from the root.
# Node 5 -> (3,4,5) is the maximum value in the path
# Node 3 -> (3,1,3) is the maximum value in the path.
#
# Example 2:
# Input: root = [3,3,null,4,2]
# Output: 3
# Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
#
# Example 3:
# Input: root = [1]
# Output: 1
# Explanation: Root is considered as good.
#
# Constraints:
# The number of nodes in the binary tree is in the range [1, 10^5].
# Each node's value is between [-10^4, 10^4].


from typing import List, Optional


class TreeNode:
    """ "Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodesWithExtraSpace(self, root: TreeNode) -> int:
        """This solution uses extra space"""
        if root is None:
            return 1

        def dfs(
            node: Optional[TreeNode], max_value: int, good_nodes: List[int]
        ) -> None:
            if node is None:
                return

            if node.val >= max_value:
                max_value = node.val
                good_nodes.append(node.val)

            dfs(node.left, max_value, good_nodes)
            dfs(node.right, max_value, good_nodes)

        good_nodes = []
        dfs(root, root.val, good_nodes)
        return len(good_nodes)

    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 1

        def dfs(node: Optional[TreeNode], max_value: int) -> None:
            count = 0
            if node is None:
                return 0
            if node.val >= max_value:
                max_value = node.val
                count = 1

            return count + dfs(node.left, max_value) + dfs(node.right, max_value)

        return dfs(root, root.val)
