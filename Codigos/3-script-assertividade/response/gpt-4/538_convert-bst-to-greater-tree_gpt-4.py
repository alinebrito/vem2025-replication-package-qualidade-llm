class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, total):
            nonlocal total
            if not node:
                return
            dfs(node.right, total)
            total += node.val
            node.val = total
            dfs(node.left, total)
        
        total = 0
        dfs(root, total)
        
        return root