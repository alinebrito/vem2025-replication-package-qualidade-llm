class Solution(object):
    def subtractProductAndSum(self, n):
        sum, pro = 0, 1
        while n > 0:
            digit = n % 10
            sum += digit
            pro *= digit
            n //= 10
        return pro - sum