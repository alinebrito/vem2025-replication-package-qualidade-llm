class Solution:
    def addDigits(self, num):
        while num > 9:
            num = sum(int(d) for d in str(num))
        return num