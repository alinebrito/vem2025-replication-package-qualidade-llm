class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [w[0]]
        for i in range(1, len(w)):
            self.prefix_sum.append(self.prefix_sum[-1] + w[i])
        self.total_sum = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        target = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left