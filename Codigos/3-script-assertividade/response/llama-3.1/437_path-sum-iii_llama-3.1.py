class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, currentSum):
            if not node:
                return 0
            currentSum += node.val
            return (1 if currentSum == targetSum else 0) + dfs(node.left, currentSum) + dfs(node.right, currentSum)

        if not root:
            return 0
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)