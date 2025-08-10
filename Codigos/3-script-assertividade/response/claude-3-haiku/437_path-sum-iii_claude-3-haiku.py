class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

    def dfs(self, node: Optional[TreeNode], target: int) -> int:
        if not node:
            return 0
        count = 0
        if node.val == target:
            count += 1
        count += self.dfs(node.left, target - node.val)
        count += self.dfs(node.right, target - node.val)
        return count