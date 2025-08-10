class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = [0] * k
        count[0] = 1
        total = 0
        result = 0
        for num in nums:
            total += num
            remainder = total % k
            if remainder < 0:
                remainder += k
            result += count[remainder]
            count[remainder] += 1
        return result