class Solution(object):
    def findBottomLeftValue(self, root):
        queue = [(root, 0)]
        leftmost_value = root.val  
        max_depth = 0
        
        while queue:
            node, depth = queue.pop(0)
            if depth > max_depth:
                max_depth = depth  
                leftmost_value = node.val  
            if node.right:
                queue.append((node.right, depth + 1))
            if node.left:
                queue.append((node.left, depth + 1))
                
        return leftmost_value  