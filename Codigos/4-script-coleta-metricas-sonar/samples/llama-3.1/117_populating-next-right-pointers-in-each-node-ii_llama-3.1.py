class Solution:
    def connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i < level_size - 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)