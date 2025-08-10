class Solution:
    def findRepeatedDnaSequences(self, s):
        sequences = {}
        result = set()
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in sequences:
                result.add(substring)
            else:
                sequences[substring] = 1
        return list(result)