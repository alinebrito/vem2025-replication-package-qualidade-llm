class Solution:
    def sumNumbers(self, root):
        self.res = 0
        def dfs(node, cur):
            if not node:
                return
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                self.res += cur
                return
            dfs(node.left, cur)
            dfs(node.right, cur)
        dfs(root, 0)
        return self.res