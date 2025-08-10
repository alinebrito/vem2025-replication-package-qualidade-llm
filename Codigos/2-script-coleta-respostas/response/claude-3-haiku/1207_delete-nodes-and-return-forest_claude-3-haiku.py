class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        res = []
        
        def dfs(node, is_root):
            if not node:
                return None
            
            is_delete = node.val in to_delete_set
            if is_root and not is_delete:
                res.append(node)
            
            node.left = dfs(node.left, is_delete)
            node.right = dfs(node.right, is_delete)
            
            return None if is_delete else node
        
        dfs(root, True)
        return res