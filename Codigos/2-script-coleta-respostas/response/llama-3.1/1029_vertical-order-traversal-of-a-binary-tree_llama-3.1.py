class Solution:
    def verticalTraversal(self, root):
        dic = {}
        self.helper(dic, 0, root, 0)
        res = []
        for key in sorted(dic.keys()):
            res.append(sorted(dic[key]))
        return res

    def helper(self, dic, placement, level, root, col):
        if(not root):
            return
        if(col not in dic):
            dic[col] = []
        dic[col].append((level, root.val))
        self.helper(dic, placement + 1, level + 1, root.left, col - 1)
        self.helper(dic, placement + 1, level + 1, root.right, col + 1)