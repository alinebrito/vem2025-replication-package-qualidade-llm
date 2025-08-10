class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_length = 0

        def dfs(node):
            if not node:
                return 0, 0

            left_len, left_arrow = dfs(node.left)
            right_len, right_arrow = dfs(node.right)

            arrow_left = 0
            arrow_right = 0

            if node.left and node.left.val == node.val:
                arrow_left = left_len + 1
            if node.right and node.right.val == node.val:
                arrow_right = right_len + 1

            self.max_length = max(self.max_length, arrow_left + arrow_right)

            return max(arrow_left, arrow_right), max(arrow_left, arrow_right)

        dfs(root)
        return self.max_length