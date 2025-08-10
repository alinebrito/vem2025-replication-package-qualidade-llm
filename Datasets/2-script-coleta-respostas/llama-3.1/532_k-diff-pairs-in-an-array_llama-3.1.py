class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        count = 0
        for num in num_set:
            if k == 0:
                if list(nums).count(num) > 1:
                    count += 1
            elif num + k in num_set:
                count += 1
        return count