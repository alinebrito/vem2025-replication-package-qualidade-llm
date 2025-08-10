class Solution:
    def convertToTitle(self, columnNumber):
        title = ""
        while columnNumber > 0:
            columnNumber -= 1
            title = chr(columnNumber % 26 + ord('A')) + title
            columnNumber //= 26
        return title