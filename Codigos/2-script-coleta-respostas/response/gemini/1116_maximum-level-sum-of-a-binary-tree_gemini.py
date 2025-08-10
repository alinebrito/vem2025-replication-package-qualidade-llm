class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        max, level, maxLevel = -float('inf'), 0, 0
        queue = [root]
        while queue:
            level += 1
            sum = 0
            for i in range(len(queue)):
                curr = queue.pop(0)
                sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if sum > max:
                max = sum
                maxLevel = level
        return maxLevel