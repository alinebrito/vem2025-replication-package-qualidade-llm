class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)

        vals = []
        inorder(root)
        dummy = TreeNode(0)
        current = dummy
        for val in vals:
            current.right = TreeNode(val)
            current = current.right
        return dummy.right