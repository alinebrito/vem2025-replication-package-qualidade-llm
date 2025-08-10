class Solution:
    def pathSum(self, root, sum):
        res = []
        self.dfs(root, sum, [], res)
        return res

    def dfs(self, root, sum, ls, res):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            ls.append(root.val)
            res.append(ls)
        self.dfs(root.left, sum - root.val, ls + [root.val], res)
        self.dfs(root.right, sum - root.val, ls + [root.val], res)