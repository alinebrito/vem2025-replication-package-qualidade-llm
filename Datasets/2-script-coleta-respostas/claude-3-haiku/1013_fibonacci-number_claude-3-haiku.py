class Solution:
    def fib(self, n: int) -> int:
        fib_nums = [0, 1]
        if n < 2:
            return fib_nums[n]
        for i in range(2, n+1):
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        return fib_nums[n]