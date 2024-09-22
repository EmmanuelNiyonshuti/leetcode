#!/usr/bin/env python3
"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
"""
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        returns the nodes that can be seen from the right side view of a binary tree
        using BFS (level-order traversal) by processing nodes at each level.
        Args:
            root - root of a tree.
        Return:
            list.
        """
        result = []
        queue = deque([root])
        while queue:
            right_most = None
            queue_len = len(queue)
            for _ in range(queue_len):
                node = queue.popleft()
                if node:
                    right_most = node
                    queue.append(node.left)
                    queue.append(node.right)
            if right_most:
                result.append(right_most.val)
        return result

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    sln = Solution()
    res = sln.rightSideView(root)
    print(res)
