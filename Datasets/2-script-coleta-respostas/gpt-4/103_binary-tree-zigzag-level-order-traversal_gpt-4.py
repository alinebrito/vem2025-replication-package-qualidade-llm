class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        result, current_level, left_to_right = [], [root], True  
        while current_level:
            level_values = [node.val for node in current_level]
            if not left_to_right:
                level_values.reverse()
            result.append(level_values)
            next_level = []
            for node in current_level:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            current_level = next_level  
            left_to_right = not left_to_right  
        return result  