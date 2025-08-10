class Solution:
    def addDigits(self, num):
        while num > 9:
            num = sum(int(digit) for digit in str(num))
        return num