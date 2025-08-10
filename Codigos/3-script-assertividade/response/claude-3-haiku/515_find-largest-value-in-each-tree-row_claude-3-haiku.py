class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            level_max = float('-inf')
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level_max)
        
        return result