class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)

        return helper(root, float('-inf'), float('inf'))