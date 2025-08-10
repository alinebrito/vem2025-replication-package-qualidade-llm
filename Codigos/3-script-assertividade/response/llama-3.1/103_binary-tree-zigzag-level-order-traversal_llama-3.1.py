class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result = []
        queue = [root]
        left_to_right = True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if left_to_right:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            left_to_right = not left_to_right