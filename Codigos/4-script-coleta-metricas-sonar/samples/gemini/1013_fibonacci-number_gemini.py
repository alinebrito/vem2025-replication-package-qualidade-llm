class Solution:
    fib_nums = [0, 1]
    def fib(self, n: int) -> int:
        if n < len(self.fib_nums):
            return self.fib_nums[n]
        else:
            for i in range(len(self.fib_nums), n + 1):
                self.fib_nums.append(self.fib_nums[i - 1] + self.fib_nums[i - 2])
            return self.fib_nums[n]