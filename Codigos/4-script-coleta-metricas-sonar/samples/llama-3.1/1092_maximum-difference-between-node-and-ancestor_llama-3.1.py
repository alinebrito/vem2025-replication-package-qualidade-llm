class Solution:
    def maxAncestorDiff(self, root):
        def dfs(node, mn, mx):
            if not node:
                return mx - mn
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            return max(dfs(node.left, mn, mx), dfs(node.right, mn, mx))
        
        return dfs(root, root.val, root.val)