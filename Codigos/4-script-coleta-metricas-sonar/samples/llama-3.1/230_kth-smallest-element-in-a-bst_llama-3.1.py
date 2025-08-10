class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            if node:
                inorder(node.left)
                self.k -= 1
 if self.k == 0:
                    self.res = node.val
                    return
                inorder(node.right)

        self.k = k
        self.res = None
        inorder(root)
        return self.res