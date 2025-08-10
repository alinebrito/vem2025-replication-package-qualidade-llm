class Solution:
    def flatten(self, root: TreeNode) -> None:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        self.prev = None
        dfs(root)