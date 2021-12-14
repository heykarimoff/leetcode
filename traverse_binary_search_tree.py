# Recursive


def dfs(root):
    if root:
        yield root.val
        yield from dfs(root.left)
        yield from dfs(root.right)
