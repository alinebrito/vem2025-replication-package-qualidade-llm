class Solution:
    def pathSum(self, root, sum):
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, node, target, path, res):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and target == node.val:
            res.append(path[:])
        self.dfs(node.left, target - node.val, path, res)
        self.dfs(node.right, target - node.val, path, res)
        path.pop()