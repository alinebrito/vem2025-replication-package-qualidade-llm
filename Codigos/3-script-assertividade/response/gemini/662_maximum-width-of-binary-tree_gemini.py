class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [(root, 0)]
        max_width = 1
        while queue:
            next_level = []
            for node, pos in queue:
                if node.left:
                    next_level.append((node.left, 2 * pos))
                if node.right:
                    next_level.append((node.right, 2 * pos + 1))
            if next_level:
                max_width = max(max_width, next_level[-1][1] - next_level[0][1] + 1)
            queue = next_level
        return max_width