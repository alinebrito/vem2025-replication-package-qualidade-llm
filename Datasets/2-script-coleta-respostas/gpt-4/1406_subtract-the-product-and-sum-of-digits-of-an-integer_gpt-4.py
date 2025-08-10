class Solution(object):
    def subtractProductAndSum(self, n):
        product = 1  
        summation = 0  
        for digit in str(n):
            digit = int(digit)
            product *= digit  
            summation += digit  
        return product - summation  