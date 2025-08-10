class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        def dfs(node):
            if not node:
                return 
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)
        dfs(root)