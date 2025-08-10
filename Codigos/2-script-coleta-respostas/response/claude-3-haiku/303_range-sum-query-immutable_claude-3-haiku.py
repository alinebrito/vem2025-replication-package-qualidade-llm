class Solution:
class NumArray:
    def __init__(self, nums: List[int]):
        self.sum = []
        curr_sum = 0
        for num in nums:
            curr_sum += num
            self.sum.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sum[right]
        return self.sum[right] - self.sum[left - 1]