class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q, ans, qlen, curr = [root], 0, 0, 0
        while len(q) != 0:
            qlen = len(q)
            curr = 0
            for i in range(qlen):
                node = q.pop(0)
                curr += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans = curr
        return ans