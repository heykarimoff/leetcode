# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # in-order traverse binary search tree
        # for each node if low <= val <= high: total += val

        return sum(self.traverse(root, low, high))

    def traverse(self, root, low, high):
        res = []
        if root:
            res = self.traverse(root.left, low, high)
            if low <= root.val <= high:
                res.append(root.val)
            res = res + self.traverse(root.right, low, high)
        return res
