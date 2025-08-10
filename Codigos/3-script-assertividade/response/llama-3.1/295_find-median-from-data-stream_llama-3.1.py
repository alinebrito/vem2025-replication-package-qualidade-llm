class Solution:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if not self.small or num <= -self.small[0]:
            self.small.append(-num)
            self.small.sort()
        else:
            self.large.append(num)
            self.large.sort()
        if len(self.small) > len(self.large) + 1:
            self.large.append(-self.small.pop())
            self.large.sort()
        elif len(self.large) > len(self.small):
            self.small.append(-self.large.pop(0))
            self.small.sort()

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]