class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total = 0

        def dfs(node):
            if node:
                dfs(node.right)
                self.total += node.val
                node.val = self.total
                dfs(node.left)

 dfs(root)
        return root