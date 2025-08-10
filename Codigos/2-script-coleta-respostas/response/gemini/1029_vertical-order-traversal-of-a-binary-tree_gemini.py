class Solution:
    def verticalTraversal(self, root):
        dic = {}
        self.helper(0,0,root,dic)
        ans = []
        for i in sorted(dic.keys()):
            temp = []
            for j in sorted(dic[i]):
                for k in sorted(j):
                    temp.append(k)
            ans.append(temp)
        return ans
    def helper(self, placement,level, root, dic):
        if(not root):
            return
        if(placement not in dic):
            dic[placement] = []
        if(len(dic[placement]) == level):
            dic[placement].append([])
        dic[placement][level].append(root.val)
        self.helper(placement - 1, level + 1, root.left, dic)
        self.helper(placement + 1, level + 1, root.right, dic)  