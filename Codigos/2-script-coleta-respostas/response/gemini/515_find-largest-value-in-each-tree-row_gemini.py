class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        maxes = []
        queue = [root]
        while queue:
            level_size = len(queue)
            level_max = float('-inf')
            for _ in range(level_size):
                node = queue.pop(0)
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            maxes.append(level_max)
        return maxes