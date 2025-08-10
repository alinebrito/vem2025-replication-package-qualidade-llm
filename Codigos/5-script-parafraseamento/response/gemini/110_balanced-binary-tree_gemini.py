class Solution:
    def isBalanced(self, root):
        return (self.Height(root) >= 0)

    def Height(self, root):
        if not root:
            return 0
        left = self.Height(root.left)
        right = self.Height(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else: