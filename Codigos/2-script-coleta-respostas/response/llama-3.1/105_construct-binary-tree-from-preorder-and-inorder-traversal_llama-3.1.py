class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None

        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])

        return root