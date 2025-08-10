class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.dfs(root, targetSum)
        return self.count
        
    def dfs(self, node, targetSum):
        if not node:
            return
        self.test(node, targetSum)
        self.dfs(node.left, targetSum)
        self.dfs(node.right, targetSum)
        
    def test(self, node, remainingSum):
        if not node:
            return
        if remainingSum == node.val:
            self.count += 1
        self.test(node.left, remainingSum - node.val)
        self.test(node.right, remainingSum - node.val)