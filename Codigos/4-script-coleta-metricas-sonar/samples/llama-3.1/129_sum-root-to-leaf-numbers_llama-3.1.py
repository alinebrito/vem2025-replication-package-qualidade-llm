class Solution:
    def sumNumbers(self, root):
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, path):
        if not node:
            return
        path = path * 10 + node.val if not node.left and not node.right:
            self.res += path
        else:
            self.dfs(node.left, path)
            self.dfs(node.right, path)