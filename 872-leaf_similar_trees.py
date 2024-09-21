#!/usr/bin/env python3

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, leaves):
            if not node:
                return
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.left, leaves)
            dfs(node.right, leaves)
        leaves1, leaves2 = [], []
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2

if __name__ == "__main__":
    root1 = TreeNode(3)
    root1.right = TreeNode(1)
    root1.left = TreeNode(5)
    root1.right.right = TreeNode(8)
    root1.right.left = TreeNode(9)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)

    root2 = TreeNode(3)
    root2.right = TreeNode(1)
    root2.left = TreeNode(5)
    root2.left.right = TreeNode(7)
    root2.left.left = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)

    sln = Solution()
    print(sln.leafSimilar(root1, root2))
