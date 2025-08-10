class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return None
        queue = [root]
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if queue:
                return queue[0].val