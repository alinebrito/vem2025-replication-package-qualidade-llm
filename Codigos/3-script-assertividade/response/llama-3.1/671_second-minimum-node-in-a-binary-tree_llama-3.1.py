class Solution:
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if not node:
                return float('inf')
            return min(dfs(node.left), dfs(node.right)) if node.left else node.val

        val = dfs(root)
        if val == root.val:
            return -1
        return val