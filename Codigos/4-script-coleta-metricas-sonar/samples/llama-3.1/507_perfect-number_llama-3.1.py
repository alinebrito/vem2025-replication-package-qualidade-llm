class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        divisors = [i for i in range(1, num) if num % i == 0]
        return sum(divisors) == num