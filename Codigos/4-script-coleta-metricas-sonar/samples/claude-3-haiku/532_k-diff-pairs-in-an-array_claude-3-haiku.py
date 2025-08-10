class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = 0
        seen = set()
        unique = set()
        for num in nums:
            if num - k in seen:
                if (num, num - k) not in unique:
                    cnt += 1
                    unique.add((num, num - k))
            if num + k in seen:
                if (num, num + k) not in unique:
                    cnt += 1
                    unique.add((num, num + k))
            seen.add(num)
        return cnt