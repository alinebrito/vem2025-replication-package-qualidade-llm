class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1
        sum_digits = 0
        while n > 0:
            digit = n % 10
            product *= digit
            sum_digits += digit
            n //= 10
        return product - sum_digits