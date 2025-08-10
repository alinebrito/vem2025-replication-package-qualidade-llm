class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)
            left = dfs(node.left)
            right = dfs(node.right)
            return (node.val + left[1] + right[1], left[0] + right[0])
        return max(dfs(root))