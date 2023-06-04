# Given the root of a binary search tree (BST) with duplicates, return all the
# mode(s) (i.e., the most frequently occurred element) in it.
#
# If the tree has more than one mode, return them in any order.
#
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than or equal to the node's key.
# The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
# Example 1:
# Input: root = [1,null,2,2]
# Output: [2]
#
# Example 2:
# Input: root = [0]
# Output: [0]
#
# Constraints:
#
# The number of nodes in the tree is in the range [1, 104].
# -105 <= Node.val <= 105
#
#
# Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).


from typing import Dict, List, Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [root.val]

        freq_tracker = {}
        modes = []

        def dfs(node: Optional[TreeNode], freq_tracker: Dict[int, int]) -> None:
            if node is None:
                return

            if node.val in freq_tracker:
                freq_tracker[node.val] += 1
            else:
                freq_tracker[node.val] = 1

            dfs(node.left, freq_tracker)
            dfs(node.right, freq_tracker)

        dfs(root, freq_tracker)

        max_val = max(freq_tracker.values())
        for k, v in freq_tracker.items():
            if v == max_val:
                modes.append(k)

        return modes
