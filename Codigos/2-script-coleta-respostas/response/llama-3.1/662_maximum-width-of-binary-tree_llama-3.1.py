class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        max_width = 0
        level = [(root, 0)]
        
        while level:
            max_width = max(max_width, level[-1][1] - level[0][1] + 1)
            level = [(child, 2 * idx + i) for node, idx in level for i, child in enumerate((node.left, node.right)) if child]
        
        return max_width