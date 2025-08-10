class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        leftToRight = True
        while queue:
            level = []
            for i in range(len(queue)):
                curr = queue.pop(0)
                level.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            if not leftToRight:
                level.reverse()
            res.append(level)
            leftToRight = not leftToRight
        return res