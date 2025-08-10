class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        max_size = 0  
        max_index = -1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1  
                    prev[i] = j  
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        
        answer = []
        while max_index != -1:
            answer.append(nums[max_index])
            max_index = prev[max_index]
        
        return answer[::-1]