class Solution(object):
    def findBottomLeftValue(self, root):
        if not root:
            return None
        queue = [root]
        result = root.val
        while queue:
            level = []
            for node in queue:
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            if level:
                result = level[0].val
            queue = level
        return result