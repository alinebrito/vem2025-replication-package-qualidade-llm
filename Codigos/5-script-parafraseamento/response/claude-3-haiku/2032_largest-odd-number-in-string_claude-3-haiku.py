class Solution:
    def largestOddNumber(self, num):
        for i in range(len(num), -1, -1):
            if int(num[i-1]) % 2 != 0:
                return num[:i]