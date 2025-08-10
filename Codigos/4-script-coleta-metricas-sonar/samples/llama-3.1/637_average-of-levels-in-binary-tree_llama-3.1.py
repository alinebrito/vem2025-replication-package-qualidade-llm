class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        q, ans = [root], []
        while q:
            level_sum, level_count = 0, 0
            for _ in range(len(q)):
                node = q.pop(0)
                level_sum += node.val
                level_count += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_sum / level_count)
        return ans