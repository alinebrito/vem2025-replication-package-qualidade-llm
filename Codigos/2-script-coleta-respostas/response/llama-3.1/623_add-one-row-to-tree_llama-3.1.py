class Solution:
    def add(self, root, val, depth, curr):
        if depth == 1:
            return TreeNode(val, root, None)
        if not root:
            return None
        if curr == depth - 1:
            root.left = TreeNode(val, root.left, None)
            root.right = TreeNode(val, None, root.right)
        else:
            self.add(root.left, val, depth, curr + 1)
            self.add(root.right, val, depth, curr + 1)
        return root