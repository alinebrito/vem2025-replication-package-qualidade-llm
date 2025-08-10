class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root, val):
            if not root:
                return 0
            count = 1 if root.val >= val else 0
            val = max(val, root.val)
            count += solve(root.left, val)
            count += solve(root.right, val)
            return count
        return solve(root, -float('inf'))