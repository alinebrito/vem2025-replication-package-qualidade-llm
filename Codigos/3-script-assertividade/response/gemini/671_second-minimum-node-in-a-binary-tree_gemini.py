class Solution:
    def findSecondMinimumValue(self, root):
        self.min1 = root.val
        self.min2 = float('inf')
        self.dfs(root)
        return self.min2 if self.min2 < float('inf') else -1
    
    def dfs(self, node):
        if not node:
            return
        if self.min1 < node.val < self.min2:
            self.min2 = node.val
        elif node.val == self.min1:
            self.dfs(node.left)
            self.dfs(node.right)