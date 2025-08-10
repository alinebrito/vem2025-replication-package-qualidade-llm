class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        root_val = postorder.pop()
        root = TreeNode(root_val)
        inorder_index = inorder.index(root_val)
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        return root