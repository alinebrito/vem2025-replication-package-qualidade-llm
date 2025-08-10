class Solution:
    def isCompleteTree(self, root):
        if not root:
            return True
        queue = deque([root])
        flag = False
        while queue:
            node = queue.popleft()
            if not node:
                flag = True
            else:
                if flag:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True 