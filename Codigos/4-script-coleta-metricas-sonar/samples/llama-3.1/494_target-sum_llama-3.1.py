class Solution:
    def findTargetSumWays(self, nums, S):
        dp = {0: 1}
        for num in nums:
            temp = {}
            for s, count in dp.items():
                temp[s + num] = temp.get(s + num, 0) + count
                temp[s - num] = temp.get(s - num, 0) + count
            dp = temp
        return dp.get(S, 0)