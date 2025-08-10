class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def dfs(node):
            if not node:
                return None
            node.val = 1 if node.val in to_delete else 0
            if node.val == 0:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
                return node
            if node.left and node.left.val == 0:
                res.append(node.left)
                dfs(node.left)
            if node.right and node.right.val == 0:
                res.append(node.right)
                dfs(node.right)
            return node
        dfs(root)
        if root and root.val != 0:
            res.append(root)
        return res