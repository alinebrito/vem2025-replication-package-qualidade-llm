class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0 or right == 0:
            return max(left, right) + 1
        else:
            return min(left, right) + 1