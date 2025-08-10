class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = None
        self.second = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.first is None and self.prev.val >= node.val:
                self.first = self.prev
            if self.first and self.prev.val >= node.val:
                self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val