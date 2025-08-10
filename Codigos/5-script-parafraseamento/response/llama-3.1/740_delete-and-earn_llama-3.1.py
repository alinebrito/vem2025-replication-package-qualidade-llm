class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = {}
        for num in nums:
            if num in count:
                count[num] += num
            else:
                count[num] = num
        keys = sorted(count.keys())
        dp = [0]*len(keys)
        dp[0] = count[keys[0]]
        if len(keys) > 1:
            dp[1] = max(count[keys[0]], count[keys[1]])
        for i in range(2, len(keys)):
            dp[i] = max(dp[i-1], dp[i-2] + count[keys[i]])
        return dp[-1]