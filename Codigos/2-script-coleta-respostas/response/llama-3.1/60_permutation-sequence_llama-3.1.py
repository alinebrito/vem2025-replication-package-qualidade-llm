class Solution:
 def getPermutation(self, n, k):
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
 return n * factorial(n-1)

        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1

        while n > 0:
            n -= 1
            factorial_n = factorial(n)
            index, k = divmod(k, factorial_n)
            permutation += str(numbers[index])
            numbers.remove(numbers[index])

        return permutation