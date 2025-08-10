class Solution:
    def add(self, root, val, depth, curr=1):
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        if not root:
            return None
        if curr == depth - 1:
            new_left = TreeNode(val)
            new_right = TreeNode(val)
            new_left.left = root.left
            new_right.right = root.right
            root.left = new_left
            root.right = new_right
        else:
            self.add(root.left, val, depth, curr + 1)
            self.add(root.right, val, depth, curr + 1)
        return root