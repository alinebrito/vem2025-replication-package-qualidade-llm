class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R)
            return 1 + max(L, R)
        depth(root)