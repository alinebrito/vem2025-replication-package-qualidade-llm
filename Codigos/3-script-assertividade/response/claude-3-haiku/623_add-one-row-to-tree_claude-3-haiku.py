class Solution:
    def add_row(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, curr_depth):
            if not node:
                return
            
            if curr_depth == depth - 1:
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                new_left.left = node.left
                new_right.right = node.right
                node.left = new_left
                node.right = new_right
            else:
                dfs(node.left, curr_depth + 1)
                dfs(node.right, curr_depth + 1)
        
        dfs(root, 1)
        return root