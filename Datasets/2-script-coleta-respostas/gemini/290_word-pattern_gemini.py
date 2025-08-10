class Solution:
    def wordPattern(self, pattern, str):
        s = str.split()
        return len(set(zip(pattern, s))) == len(set(pattern)) == len(set(s)) and len(pattern) == len(s)