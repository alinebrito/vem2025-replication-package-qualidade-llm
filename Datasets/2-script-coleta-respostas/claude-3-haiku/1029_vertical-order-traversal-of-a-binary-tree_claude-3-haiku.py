class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        placement = {}
        queue = deque([(root, 0)])
        
        while queue:
            node, col = queue.popleft()
            if col not in placement:
                placement[col] = []
            placement[col].append(node.val)
            
            if node.left:
                queue.append((node.left, col - 1))
            if node.right:
                queue.append((node.right, col + 1))
        
        return [placement[col] for col in sorted(placement)]