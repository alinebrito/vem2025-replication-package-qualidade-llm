class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.min_diff = float('inf')
        self.prev = None
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev:
                self.min_diff = min(self.min_diff, abs(node.val - self.prev.val))
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        return self.min_diff