class Solution:
    def decodeString(self, s):
        stack = []
        curNum = 0
        curString = ''
        for char in s:
            if char.isdigit():
                curNum = curNum * 10 + int(char)
            elif char == '[':
                stack.append((curString, curNum))
                curString, curNum = '', 0
            elif char == ']':
                lastString, num = stack.pop()
                curString = lastString + curString * num
            else:
                curString += char
        return curString