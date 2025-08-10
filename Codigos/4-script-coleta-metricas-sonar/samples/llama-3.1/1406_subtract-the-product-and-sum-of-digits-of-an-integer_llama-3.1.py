class Solution:
    def subtractProductAndSum(self, n):
        product = 1
        sum = 0
        for digit in str(n):
            product *= int(digit)
            sum += int(digit)
        return product - sum