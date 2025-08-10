class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.prefix_sum = [0] * len(w)
        self.prefix_sum[0] = w[0]
        for i in range(1, len(w)):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + w[i]

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1])
        left, right = 0, len(self.prefix_sum) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix_sum[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left