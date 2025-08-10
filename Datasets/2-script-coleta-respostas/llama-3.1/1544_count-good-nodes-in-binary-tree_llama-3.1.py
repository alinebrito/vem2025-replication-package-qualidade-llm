class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, val):
            if not root:
                return 0
            good = 1 if root.val >= val else 0
            val = max(val, root.val)
            return good + solve(root.left, val) + solve(root.right, val)
        
        return solve(root, root.val)