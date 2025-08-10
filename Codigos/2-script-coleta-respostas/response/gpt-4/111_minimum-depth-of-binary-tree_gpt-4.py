class Solution:
    def minDepth1(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth1(root.right)
        if not root.right:
            return 1 + self.minDepth1(root.left)
        return 1 + min(self.minDepth1(root.left), self.minDepth1(root.right))