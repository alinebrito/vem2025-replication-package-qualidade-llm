class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = [0] * 26
        count2 = [0] * 26
        for c in word1:
            count1[ord(c) - ord('a')] += 1
        for c in word2:
            count2[ord(c) - ord('a')] += 1
        if set(count1) != set(count2):
            return False
        return sorted(count1) == sorted(count2)