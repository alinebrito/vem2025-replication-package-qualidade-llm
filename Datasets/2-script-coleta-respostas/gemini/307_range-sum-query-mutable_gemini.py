class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)
        self.tree = [0] * (self.n * 2)
        self.buildTree()

    def buildTree(self):
        for i in range(self.n, 2 * self.n):
            self.tree[i] = self.nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, val):
        index += self.n
        self.tree[index] = val
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def sumRange(self, left, right):
        left += self.n
        right += self.n
        sum = 0
        while left <= right:
            if left % 2 == 1:
                sum += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return sum