class Solution:
    def sumNumbers1(self, root):
        def dfs(node, current_sum):
            if not node:
                return 0
            current_sum = current_sum * 10 + node.val
            if not node.left and not node.right:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        return dfs(root, 0)