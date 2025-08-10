class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0  
        num_count = {}
        for num in nums:
            complement = k - num  
            if num_count.get(complement, 0) > 0:
                count += 1  
                num_count[complement] -= 1  
            else:
                num_count[num] = num_count.get(num, 0) + 1  
        return count  