class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max_sum, max_level, level = -float('inf'), 0, 0
        queue = [root]
        
        while queue:
            level += 1
            level_sum = sum(node.val for node in queue)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            queue = [child for node in queue for child in (node.left, node.right) if child]
        
        return max_level