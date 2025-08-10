class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            if node.left and node.val == node.left.val:
                left += 1
            else:
                left = 0
            if node.right and node.val == node.right.val:
                right += 1
            else:
                right = 0
            self.ans = max(self.ans, left + right)
            return max(left, right)

        dfs(root)
        return self.ans