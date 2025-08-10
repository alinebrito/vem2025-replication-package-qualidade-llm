class Solution:
    def plusOne(self, digits):
        num = 0
        for digit in digits:
            num = num * 10 + digit
        return [int(x) for x in str(num + 1)]