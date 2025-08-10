class Solution:
    def getPermutation(self, n, k):
            numbers = range(1, n+1)
            fact = [1] * n
            for i in range(1, n):
                fact[i] = i * fact[i-1]
            k -= 1
            res = ""
            for i in range(n, 0, -1):
                index = k // fact[i-1]
                k %= fact[i-1]
                res += str(numbers[index])
                numbers.pop(index)
            return res