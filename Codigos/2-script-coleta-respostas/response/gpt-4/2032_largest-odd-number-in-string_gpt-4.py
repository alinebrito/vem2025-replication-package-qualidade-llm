class Solution:
    def largestOddNumber(self, num: str) -> str:
        for char in reversed(num):
            if int(char) % 2 != 0:
                return num[:len(num) - num.index(char)]
        return ""