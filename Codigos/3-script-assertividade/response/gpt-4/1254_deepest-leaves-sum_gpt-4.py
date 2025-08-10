class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q, ans, qlen, curr = [root], 0, 0, 0