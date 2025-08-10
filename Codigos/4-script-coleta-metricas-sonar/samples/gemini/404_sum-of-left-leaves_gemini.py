class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                return node.left.val + dfs(node.right)
            return dfs(node.left) + dfs(node.right)
        return dfs(root)