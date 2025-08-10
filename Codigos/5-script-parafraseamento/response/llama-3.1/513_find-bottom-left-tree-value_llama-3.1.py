class Solution(object):
    def findBottomLeftValue(self, root):
        queue = [root]
        result = root.val
        while queue:
            level_size = len(queue)
            result = queue[0].val
            for _ in range(level_size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result