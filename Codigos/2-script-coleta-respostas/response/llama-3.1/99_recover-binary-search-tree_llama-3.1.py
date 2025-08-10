class Solution:
    def recoverTree(self, root):
        self.first, self.second, self.prev = None, None, None
        self.inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def inorder(self, node):
        if not node:
            return
        self.inorder(node.left)
        if self.prev and self.prev.val > node.val:
            if not self.first:
                self.first = self.prev
            self.second = node
        self.prev = node
        self.inorder(node.right)