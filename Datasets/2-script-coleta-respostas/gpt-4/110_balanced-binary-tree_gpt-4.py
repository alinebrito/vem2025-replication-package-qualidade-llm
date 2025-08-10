class Solution:
    def isBalanced(self, root):
        return (self.Height(root) >= 0)

    def Height(self, node):
        if not node:
            return 0
        left_height = self.Height(node.left)
        right_height = self.Height(node.right)
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1