class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, ans = [root], []
        while q:
            level_sum, level_size = 0, len(q)
            for i in range(level_size):
                node = q.pop(0)
                if node:
                    level_sum += node.val
                    if node.left: q.append(node.left)
                    if node.right: q.append(node.right)
            ans.append(level_sum / level_size)
        return ans