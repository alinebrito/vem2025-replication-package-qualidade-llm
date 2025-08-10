class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue, level = [], [root], 0
        while queue:
            level_res = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            if level % 2 == 1: level_res.reverse()
            res.append(level_res)
            level += 1
        return res