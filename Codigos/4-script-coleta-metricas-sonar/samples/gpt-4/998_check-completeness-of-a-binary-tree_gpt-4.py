class Solution:
    def isCompleteTree(self, root):
        if not root:
            return True
        queue = deque([root])
        end = False
        while queue:
            node = queue.popleft()
            if not node:
                end = True
            else:
                if end:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True