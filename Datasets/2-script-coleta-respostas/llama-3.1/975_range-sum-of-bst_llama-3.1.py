class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            if low <= node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
            else:
                return dfs(node.left) + dfs(node.right)
        
        return dfs(root)