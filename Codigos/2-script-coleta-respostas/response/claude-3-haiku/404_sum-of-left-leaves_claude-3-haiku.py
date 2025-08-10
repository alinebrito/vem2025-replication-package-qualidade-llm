class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_sum = self.sumOfLeftLeaves(root.left)
        right_sum = self.sumOfLeftLeaves(root.right)
        if root.left and not root.left.left and not root.left.right:
            return left_sum + root.left.val
        return left_sum + right_sum