class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.count = 0
        self.result = None

        def inorder(node):
            if node:
                inorder(node.left)
                self.count += 1
                if self.count == self.k:
                    self.result = node.val
                inorder(node.right)

        inorder(root)
        return self.result