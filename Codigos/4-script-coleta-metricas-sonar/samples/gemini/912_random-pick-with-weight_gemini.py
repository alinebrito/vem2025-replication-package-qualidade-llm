class Solution:
    def __init__(self, w: List[int]):
        self.w = w
        self.n = len(w)
        self.s = sum(w)
        for i in range(1, self.n):
            self.w[i] += self.w[i - 1]

    def pickIndex(self) -> int:
        x = random.randint(1, self.s)
        l, r = 0, self.n - 1
        while l < r:
            mid = (l + r) // 2
            if self.w[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l