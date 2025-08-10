class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = collections.defaultdict(int)
        for i in range(len(s) - 9):
            sequences[s[i:i+10]] += 1
        return [seq for seq, count in sequences.items() if count > 1]