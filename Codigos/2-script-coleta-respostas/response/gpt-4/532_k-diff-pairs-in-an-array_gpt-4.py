class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0
        num_set = set(nums)
        cnt = 0
        if k == 0:
            for num in num_set:
                if nums.count(num) > 1:
                    cnt += 1
        else:
            for num in num_set:
                if num + k in num_set:
                    cnt += 1
        return cnt