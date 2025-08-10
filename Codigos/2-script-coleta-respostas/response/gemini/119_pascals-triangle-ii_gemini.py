class Solution:
    def getRow(self, r):
        ans = [1]*(r+1)
        for i in range(1,r):
            for j in range(i,0,-1):
                ans[j] += ans[j-1]
        return ans