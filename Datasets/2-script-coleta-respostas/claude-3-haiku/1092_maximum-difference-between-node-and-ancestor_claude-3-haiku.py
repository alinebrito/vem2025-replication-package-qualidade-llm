class Solution(object):
    def maxAncestorDiff(self, root):
        def dfs(node, max_val, min_val):
            if not node:
                return max_val - min_val
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            left = dfs(node.left, max_val, min_val)
            right = dfs(node.right, max_val, min_val)
            return max(left, right)
        return dfs(root, root.val, root.val)