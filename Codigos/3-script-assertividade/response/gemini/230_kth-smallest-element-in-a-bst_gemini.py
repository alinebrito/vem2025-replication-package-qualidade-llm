class Solution:
    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.dfs(root)
        return self.res

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.dfs(node.right)