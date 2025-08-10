class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q, ans = [root], 0
        while q:
            ans = 0
            qlen = len(q)
            for _ in range(qlen):
                curr = q.pop(0)
                ans += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return ans