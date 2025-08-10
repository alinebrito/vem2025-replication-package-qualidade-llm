class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder:
            return None  
        root = preorder[0]
        root_index = inorder.index(root)
        left_inorder = inorder[:root_index]
        right_inorder = inorder[root_index + 1:]
        left_preorder = preorder[1:root_index + 1]
        right_preorder = preorder[root_index + 1:]
        root_node = TreeNode(root)
        root_node.left = self.buildTree(left_preorder, left_inorder)
        root_node.right = self.buildTree(right_preorder, right_inorder)
        return root_node  