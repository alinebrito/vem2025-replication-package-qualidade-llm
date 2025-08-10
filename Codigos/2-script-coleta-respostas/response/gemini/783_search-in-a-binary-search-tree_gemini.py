class Solution:
    def searchBST(self, root, val):
        def rec(root):
            if not root:
                return None
            if root.val == val:
                return root
            elif root.val > val:
                return rec(root.left)
            else:
                return rec(root.right)
        return rec(root)