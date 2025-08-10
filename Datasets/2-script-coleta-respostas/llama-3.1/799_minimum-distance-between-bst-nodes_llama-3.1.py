class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.prev = -1
        self.min_diff = float('inf')
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev != -1:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)
        
        inorder(root)
        return self.min_diff