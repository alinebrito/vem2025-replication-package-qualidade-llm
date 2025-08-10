class Solution:
    def Height(self, root):
        if not root:
            return 0
        return 1 + max(self.Height(root.left), self.Height(root.right))

    def isBalanced(self, root):
        return (self.Height(root) >= 0)