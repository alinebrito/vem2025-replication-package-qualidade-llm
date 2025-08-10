class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            max_value = float('-inf')
            next_queue = []
            for node in queue:
                max_value = max(max_value, node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            result.append(max_value)
            queue = next_queue
        return result