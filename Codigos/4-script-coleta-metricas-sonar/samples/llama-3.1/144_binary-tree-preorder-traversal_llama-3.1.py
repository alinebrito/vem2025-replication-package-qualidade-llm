class Solution:
    def preorderTraversal(self, root):
        ret = []
        self.dfs(root, ret)
        return ret

    def dfs(self, node, ret):
        if node:
            ret.append(node.val)
            self.dfs(node.left, ret)
            self.dfs(node.right, ret)