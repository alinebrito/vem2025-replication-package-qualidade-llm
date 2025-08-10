class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        elif not root.children:
            return 1 else:
            return 1 + max(self.maxDepth(child) for child in root.children)