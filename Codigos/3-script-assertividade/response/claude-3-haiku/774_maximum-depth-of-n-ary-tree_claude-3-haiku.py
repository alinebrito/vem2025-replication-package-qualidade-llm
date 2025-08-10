class Solution:
    def maxDepth(self, root):
        if not root: return 0
        depth = 0
        queue = [root]
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node.children:
                    queue.extend(node.children)
            depth += 1
        return depth