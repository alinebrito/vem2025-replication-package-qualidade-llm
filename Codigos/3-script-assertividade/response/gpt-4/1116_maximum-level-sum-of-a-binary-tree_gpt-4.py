class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max, level, maxLevel = -float('inf'), 0, 0
        queue = [(root, 1)]
        while queue:
            current_sum, current_level = 0, queue[0][1]
            for _ in range(len(queue)):
                node, lvl = queue.pop(0)
                current_sum += node.val
                if node.left:
                    queue.append((node.left, lvl + 1))
                if node.right:
                    queue.append((node.right, lvl + 1))
            if current_sum > max:
                max = current_sum
                maxLevel = current_level
        return maxLevel