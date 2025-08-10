class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if not node:
                return