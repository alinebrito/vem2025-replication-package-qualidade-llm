class Solution:
    def recursive(self, root, val):
        def rec(root):
            if not root:
                return None
            if root.val == val:
                return root
            elif val < root.val:
                return rec(root.left)
            else:
                return rec(root.right)
        return rec(root)