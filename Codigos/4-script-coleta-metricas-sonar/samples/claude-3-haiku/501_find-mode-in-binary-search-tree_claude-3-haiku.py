class Solution:
    def findMode(self, root):
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.count[node.val] = self.count.get(node.val, 0) + 1
        self.dfs(node.right)
        self.max_count = max(self.max_count, self.count[node.val])
        self.modes = [k for k, v in self.count.items() if v == self.max_count]

    def findMode(self, root):
        self.count = {}
        self.max_count = 0
        self.modes = []
        self.dfs(root)
        return self.modes