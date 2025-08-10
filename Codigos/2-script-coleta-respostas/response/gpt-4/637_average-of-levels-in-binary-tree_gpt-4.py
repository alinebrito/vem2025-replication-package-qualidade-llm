class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, ans = [root], []
        while q:
            level_sum, level_count = 0, len(q)
            for _ in range(level_count):
                node = q.pop(0)
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_sum / level_count)
        return ans