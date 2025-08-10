class Solution:
    def findMode(self, root):
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.modes = []
        self.dfs(root)
        return self.modes

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        if node.val == self.prev:
            self.count += 1
        else:
            self.count = 1
            self.prev = node.val
        if self.count == self.max_count:
            self.modes.append(node.val)
        elif self.count > self.max_count:
            self.max_count = self.count
            self.modes = [node.val]
        self.dfs(node.right)