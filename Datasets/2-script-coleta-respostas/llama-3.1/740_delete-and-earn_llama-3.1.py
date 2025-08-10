class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += num
            else:
                count[num] = num
        
        keys = sorted(count.keys())
        dp = [0] * len(keys)
        dp[0] = count[keys[0]]
        for i in range(1, len(keys)):
            if keys[i] - keys[i-1] > 1:
                dp[i] = max(dp[i-1], dp[i-1] + count[keys[i]])
            else:
                dp[i] = max(dp[i-1], count[keys[i]])
        
        return dp[-1]