class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([root])
        has_null = False
        while queue:
            node = queue.popleft()
            if node is None:
                has_null = True
            else:
                if has_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True