class Solution:
    def addOneRow(self, root, val, depth):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        if depth == 2:
            left_node = TreeNode(val)
            right_node = TreeNode(val)
            left_node.left = root.left
            right_node.right = root.right
            root.left = left_node
            root.right = right_node
            return root

        if root:
            root.left = self.addOneRow(root.left, val, depth - 1)
            root.right = self.addOneRow(root.right, val, depth - 1)
        return root