class Solution:
    def largestValues(self, root):
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            size = len(queue)
            max_val = float('-inf')
            for _ in range(size):
                node = queue.pop(0)
                max_val = max(max_val, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(max_val)
        return result
