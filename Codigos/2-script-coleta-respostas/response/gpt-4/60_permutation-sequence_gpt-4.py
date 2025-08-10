class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n + 1))
        k -= 1
        factorial = 1
        for i in range(1, n):
            factorial *= i
        permutation = []
        for i in range(n):
            index = k // factorial
            permutation.append(str(numbers[index]))
            numbers.pop(index)
            k %= factorial
            if i < n - 1:
                factorial //= (n - 1 - i)
        return ''.join(permutation)