class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        current_level = [root]
        while current_level:
            next_level = []
            current_vals = []
            for node in current_level:
                current_vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.append(current_vals)
            current_level = next_level
        return result