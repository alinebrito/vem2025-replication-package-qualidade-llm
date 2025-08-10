class Solution:
    def helper(self, placement, level, root, dic):
        if not root:
            return
        dic.setdefault(placement, []).append((level, root.val))
        self.helper(placement - 1, level + 1, root.left, dic)
        self.helper(placement + 1, level + 1, root.right, dic)

    def verticalTraversal(self, root):
        dic = {}
        self.helper(0, 0, root, dic)
        result = []
        for key in sorted(dic.keys()):
            result.append([val for _, val in sorted(dic[key])])
        return result