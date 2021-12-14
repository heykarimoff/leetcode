# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time: O(n)
# Space: O(n)
class Solution1:
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


# Time: O(n)
# Space: O(1)


class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        #
        return sum(self.dfs(root, low, high))

    def dfs(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root:
            yield root.val
            yield from self.dfs(root.left, low, high)
            yield from self.dfs(root.right, low, high)


def dfs(root: Optional[TreeNode]) -> int:
    if root:
        yield root.val
        yield from self.dfs(root.left)
        yield from self.dfs(root.right)
