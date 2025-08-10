class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def solve(root,val):
            if not root:
                return 0
            res=0
            if root.val>=val:
                res=1
            val=max(val,root.val)
            return res+solve(root.left,val)+solve(root.right,val)
        return solve(root,root.val)