class Solution:
    def preorder(self, root):
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res += self.preorder(child)
        return res