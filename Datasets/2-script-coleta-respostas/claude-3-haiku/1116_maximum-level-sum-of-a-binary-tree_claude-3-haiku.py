class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max, level, maxLevel = -float('inf'), 0, 0
        queue = [root]
        while queue:
            levelSum = sum(node.val for node in queue)
            if levelSum > max:
                max, maxLevel = levelSum, level + 1
            level += 1
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return maxLevel