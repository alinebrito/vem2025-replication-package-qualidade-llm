class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k nums.sort(reverse=True)
        k_sets = [0] * k
        def dfs(i):
            if i == len(nums):
                return True
            for j in range(k):
                if k_sets[j] + nums[i] <= target:
                    k_sets[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    k_sets[j] -= nums[i]
            return False
        return dfs(0)