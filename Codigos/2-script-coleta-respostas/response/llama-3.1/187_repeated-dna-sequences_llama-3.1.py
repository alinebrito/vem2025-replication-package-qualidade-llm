class Solution:
    def findRepeatedDnaSequences(self, s):
        sequences = collections.defaultdict(int)
        for i in range(len(s) - 9):
            sequences[s[i:i+10]] += 1
        return [k for k, v in sequences.items() if v > 1]