class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse=True)
        used = [False] * len(nums)

        def backtrack(start: int, curr_sum: int, group_count: int) -> bool:
            if group_count == k:
                return True
            if curr_sum == target:
                return backtrack(0, 0, group_count + 1)
            for i in range(start, len(nums)):
                if not used[i] and curr_sum + nums[i] <= target:
                    used[i] = True
                    if backtrack(i + 1, curr_sum + nums[i], group_count):
                        return True
                    used[i] = False
            return False

        return backtrack(0, 0, 0)