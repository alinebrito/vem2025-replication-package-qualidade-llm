class Solution:
    def getPermutation(self, n, k):
        numbers = list(range(1, n+1))
        k -= 1
        result = []
        factorial = [1] * (n+1)
        for i in range(1, n+1):
            factorial[i] = factorial[i-1] * i
        for i in range(n):
            index = k // factorial[n-i-1]
            result.append(str(numbers[index]))
            numbers.pop(index)
            k -= index * factorial[n-i-1]
        return ''.join(result)