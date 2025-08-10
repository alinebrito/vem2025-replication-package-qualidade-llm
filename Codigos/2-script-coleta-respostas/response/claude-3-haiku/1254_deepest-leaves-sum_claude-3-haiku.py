class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q, ans, qlen, curr = [root], 0, 0, 0
        while q:
            qlen = len(q)
            curr = 0
            for _ in range(qlen):
                node = q.pop(0)
                if not node.left and not node.right:
                    curr += node.val
                else:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            ans = curr
        return ans