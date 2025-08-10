class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        left, right = root, root
        left_height, right_height = 0, 0
        while left:
            left = left.left
            left_height += 1
        while right:
            right = right.right
            right_height += 1
        if left_height == right_height:
            return 2 ** left_height - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)