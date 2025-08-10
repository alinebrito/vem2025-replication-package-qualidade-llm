class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        stack = [root]
        result = []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            stack.extend(node.children[::-1])
        
        return result