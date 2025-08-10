class Solution:
    def pathSum(self, root, targetSum):
        res = []
        
        def dfs(node, currentPath, currentSum):
            if not node:
                return
            currentPath.append(node.val)
            currentSum += node.val
            if not node.left and not node.right and currentSum == targetSum:
                res.append(list(currentPath))
            else:
                dfs(node.left, currentPath, currentSum)
                dfs(node.right, currentPath, currentSum)
            currentPath.pop()
        
        dfs(root, [], 0)
        return res