class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for index, char in enumerate(s):
            if count[char] == 1:
                return index
        return -1