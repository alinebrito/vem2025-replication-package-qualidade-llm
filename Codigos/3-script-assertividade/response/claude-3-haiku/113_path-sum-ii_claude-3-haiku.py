class Solution:
    def pathSum(self, root, targetSum):
        res = []
        self.dfs(root, targetSum, [], res)
        return res

    def dfs(self, node, target, path, res):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and sum(path) == target:
            res.append(path[:])
        self.dfs(node.left, target, path, res)
        self.dfs(node.right, target, path, res)
        path.pop()