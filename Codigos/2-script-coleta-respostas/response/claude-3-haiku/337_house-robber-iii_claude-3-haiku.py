class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return [0, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            rob_node = node.val + left[1] + right[1]
            not_rob_node = max(left) + max(right)
            
            return [rob_node, not_rob_node]
        
        return max(dfs(root))