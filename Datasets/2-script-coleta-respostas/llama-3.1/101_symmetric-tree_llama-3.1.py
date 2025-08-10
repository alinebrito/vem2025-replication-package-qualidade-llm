class Solution:
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)

    def isSymmetric(self, root):
        return not root or self.isMirror(root.left, root.right)