class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []
        current_level = [root]
        while current_level:
            next_level = []
            current_values = []
            for node in current_level:
                current_values.append(node.val)
                if node.children:
                    next_level.extend(node.children)
            result.append(current_values)
            current_level = next_level
        return result