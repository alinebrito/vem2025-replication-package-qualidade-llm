class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        n = len(nums)
        taken = [False] * n

        def backtrack(count: int, curr_sum: int, start: int) -> bool:
            if count == k - 1:
                return True
            if curr_sum == target:
                return backtrack(count + 1, 0, 0)
            if curr_sum > target:
                return False
            for i in range(start, n):
                if not taken[i]:
                    taken[i] = True
                    if backtrack(count, curr_sum + nums[i], i + 1):
                        return True
                    taken[i] = False
            return False

        return backtrack(0, 0, 0)