class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)
        return all(a == b for a, b in zip(dfs(root1), dfs(root2)))